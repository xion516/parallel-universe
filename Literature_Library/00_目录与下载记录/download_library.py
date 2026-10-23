from pathlib import Path
from html.parser import HTMLParser
import concurrent.futures, hashlib, html, io, json, logging, re, shutil, sys, threading, time, unicodedata
import urllib.request, urllib.parse
from datetime import datetime, timezone
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parent
CATALOG=PROJECT/"Literature_Review/2026-10-22/literature_catalog.json"
META=ROOT/"00_目录与下载记录"
META.mkdir(parents=True,exist_ok=True)
logging.getLogger("pypdf").setLevel(logging.ERROR)
GROUPS={
"语言与地缘政治":"01_语言与地缘政治",
"用户身份与隐含线索":"02_用户身份与隐含线索",
"提问框架与来源框架":"03_提问框架与来源框架",
"迎合与用户追问":"04_迎合与用户追问",
"检索、搜索与信息环境":"05_检索搜索与信息环境",
"跨模型与测量基础":"06_跨模型与测量基础",
"人类后果、调解与资源冲突":"07_人类后果调解与资源冲突",
"机构评测与PPT引用校验":"08_机构评测报告",
}
FIXED={"L07":"2601.12164v6","F04":"2602.23971v4","F05":"2609.07448v2"}
LOCAL={"L15":"awwad_2026.pdf","F03":"kaur_2025.pdf","F07":"bisbee_2026.pdf"}
EXTRA={"L13":["https://openreview.net/pdf?id=zl16jLb91v"],"M04":["https://proceedings.mlr.press/v202/santurkar23a/santurkar23a.pdf"],"M07":["https://papers.nips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf"],"M10":["https://arxiv.org/pdf/2601.07398v2"]}
LOCK=threading.Lock()
HOST_LOCKS={}
RECORDS=json.loads(CATALOG.read_text(encoding="utf-8"))["records"]
MANIFEST=META/"download_manifest.json"
STATE=json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
OVERRIDES_FILE=META/"source_overrides.json"
OVERRIDES=json.loads(OVERRIDES_FILE.read_text(encoding="utf-8")) if OVERRIDES_FILE.exists() else {}
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"
STOP={"the","and","with","from","large","language","models","model","through","across","towards","into","their","that","this","what","how","for","its","llms"}
def now():return datetime.now(timezone.utc).isoformat()
def norm(s):
 return " ".join(re.findall(r"[a-z0-9]+",unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower()))
def tokens(s):return {x for x in norm(s).split() if len(x)>2 and x not in STOP}
def identity(title,text):
 ts=tokens(title);fs=tokens(text)
 return round(len(ts&fs)/max(1,len(ts)),3)
def stem(r):
 t=re.sub(r'[<>:"/\\|?*\x00-\x1f]',' ',r["title"])
 t=re.sub(r"\s+"," ",t).strip(" .")
 return r["id"]+"_"+str(r["year"])+"_"+t[:125].rstrip(" .")
def fetch(url):
 host=urllib.parse.urlparse(url).netloc
 with LOCK:
  sem=HOST_LOCKS.setdefault(host,threading.Semaphore(2))
 with sem:
  req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"application/pdf,text/html,application/xml;q=0.9,*/*;q=0.8"})
  started=time.monotonic()
  with urllib.request.urlopen(req,timeout=25) as response:
   parts=[];total=0
   while True:
    b=response.read(262144)
    if not b:break
    parts.append(b);total+=len(b)
    if total>85_000_000:raise ValueError("response exceeds 85MB limit")
    if time.monotonic()-started>100:raise TimeoutError("download time limit exceeded")
   return b"".join(parts),response.url,response.headers.get("Content-Type","")
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.links=[];self.skip=0;self.out=[];self.meta={};self.article=0;self.main=0;self.article_text=[];self.main_text=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag in ("script","style"):self.skip+=1
  if tag=="article":self.article+=1
  if tag=="main":self.main+=1
  if tag in ("p","div","h1","h2","h3","h4","li","tr","br"):self.add("\n")
  if tag in ("a","link","iframe","embed"):
   u=d.get("href") or d.get("src")
   if u:self.links.append((u,d.get("type","")))
  if tag=="meta":
   k=(d.get("name") or d.get("property") or "").lower()
   v=d.get("content","")
   if k:self.meta[k]=v
   if "pdf" in k and v:self.links.insert(0,(v,"application/pdf"))
 def handle_endtag(self,tag):
  if tag in ("script","style") and self.skip:self.skip-=1
  if tag=="article":self.article=max(0,self.article-1)
  if tag=="main":self.main=max(0,self.main-1)
  if tag in ("p","div","h1","h2","h3","h4","li","tr"):self.add("\n")
 def add(self,s):
  if not self.skip:
   self.out.append(s)
   if self.article:self.article_text.append(s)
   if self.main:self.main_text.append(s)
 def handle_data(self,s):self.add(s)
 def text(self):
  for seq in (self.article_text,self.main_text,self.out):
   s="\n".join(" ".join(x.split()) for x in "".join(seq).splitlines() if x.strip())
   if len(s)>3500:return s
  return s
def pdf_info(blob,r):
 if not blob.lstrip().startswith(b"%PDF"):raise ValueError("not a PDF (HTML/challenge/landing page rejected)")
 reader=PdfReader(io.BytesIO(blob),strict=False)
 if reader.is_encrypted:
  if reader.decrypt("")==0:raise ValueError("encrypted PDF")
 pages=len(reader.pages)
 text="\n".join(reader.pages[i].extract_text() or "" for i in range(min(3,pages)))
 score=identity(r["title"],text[:1800])
 if pages==0:raise ValueError("zero pages")
 if score<0.72:raise ValueError("PDF title not verified near document heading; token overlap="+str(score))
 return pages,text,score
def save_pdf(r,blob,url,version):
 pages,text,score=pdf_info(blob,r)
 folder=ROOT/GROUPS[r["dimension"]];folder.mkdir(exist_ok=True)
 path=folder/(stem(r)+".pdf")
 if path.exists() and path.read_bytes()!=blob:
  raise ValueError("existing different file protected")
 path.write_bytes(blob)
 return {"status":"pdf_downloaded","path":str(path.relative_to(ROOT)),"download_url":url,"version":version,"pages":pages,"bytes":len(blob),"sha256":hashlib.sha256(blob).hexdigest(),"title_match_score":score,"identity_check":"title token overlap in first 3 pages","downloaded_utc":now()}
def log_attempt(r,url,result):
 with LOCK:
  with (META/"download_attempts.jsonl").open("a",encoding="utf-8") as f:f.write(json.dumps({"id":r["id"],"url":url,"result":result,"utc":now()},ensure_ascii=False)+"\n")
def version_for(url):
 if "arxiv.org" in url:return "arXiv preprint; see source URL for version"
 if "openreview.net" in url:return "conference/review manuscript from OpenReview"
 return "publisher or author-hosted full text; inspect record notes"
def candidates_from_url(url,r):
 out=[]
 if "aclanthology.org" in url and not url.endswith(".pdf"):out.append(url.rstrip("/")+".pdf")
 if "arxiv.org/abs/" in url:
  aid=FIXED.get(r["id"],url.split("/abs/")[-1]);out.append("https://arxiv.org/pdf/"+aid)
 if "nature.com/articles/" in url:out.append(url.split("?")[0].rstrip("/")+".pdf")
 doi=url.split("doi.org/")[-1] if "doi.org/" in url else ""
 if doi.startswith("10.1007/"):out.append("https://link.springer.com/content/pdf/"+doi+".pdf")
 if "link.springer.com/article/" in url:out.append(url.replace("/article/","/content/pdf/").split("?")[0]+".pdf")
 if doi.startswith("10.1038/"):out.append("https://www.nature.com/articles/"+doi.split("/",1)[1]+".pdf")
 if doi.startswith("10.1057/"):out.append("https://www.nature.com/articles/"+doi.split("/",1)[1]+".pdf")
 if doi.startswith("10.1371/"):out.append("https://journals.plos.org/plosone/article/file?id="+doi+"&type=printable")
 if doi.startswith("10.1145/"):out.append("https://dl.acm.org/doi/pdf/"+doi)
 if doi.startswith("10.1126/"):out.append("https://www.science.org/doi/pdf/"+doi)
 if doi.startswith("10.1073/"):out.append("https://www.pnas.org/doi/pdf/"+doi)
 if "papers.nips.cc" in url:out.append(url.replace("/hash/","/file/").replace("-Abstract-","-Paper-").replace(".html",".pdf"))
 if "/view/" in url and "aaai.org" in url:pass
 if url.lower().split("?")[0].endswith(".pdf"):out.insert(0,url)
 return list(dict.fromkeys(out))
def links_from_page(blob,url,r):
 p=Page();p.feed(blob.decode("utf-8",errors="replace"))
 out=[]
 for u,typ in p.links:
  a=urllib.parse.urljoin(url,html.unescape(u))
  if a.startswith(("http://","https://")) and (".pdf" in a.lower() or "application/pdf" in typ or "arxiv.org/abs/" in a or "/download/" in a):
   out.extend(candidates_from_url(a,r) or [a])
 return list(dict.fromkeys(out)),p
def collect(r):
 rid=r["id"]
 old=STATE.get(rid)
 if old and old.get("status") in ("pdf_downloaded","html_fulltext") and (ROOT/old.get("path","")).is_file():
  return rid,old
 urls=OVERRIDES.get(rid,[])+EXTRA.get(rid,[])+candidates_from_url(r["primary_url"],r)
 tried=set();last=[];pages=[]
 if rid in LOCAL:
  p=PROJECT/"Literature_Review/2026-10-22/framing_deep_dive/sources"/LOCAL[rid]
  if p.exists():
   try:
    result=save_pdf(r,p.read_bytes(),r["primary_url"],"reused validated source PDF from framing review")
    log_attempt(r,str(p),"reused local PDF");return rid,result
   except Exception as e:last.append(str(e))
 def try_urls(items):
  for url in items:
   if url in tried:continue
   tried.add(url)
   try:
    blob,final,ct=fetch(url)
    if blob.lstrip().startswith(b"%PDF"):
     result=save_pdf(r,blob,final,version_for(url))
     log_attempt(r,url,"PDF validated");return result
    if "html" in ct or blob.lstrip().startswith(b"<"):
     links,page=links_from_page(blob,final,r)
     pages.append((blob,final,page))
     for u in links[:8]:
      if u not in tried and u not in urls:urls.append(u)
     log_attempt(r,url,"HTML landing page; links extracted")
    else:log_attempt(r,url,"non-PDF response: "+ct)
   except Exception as e:
    err=str(e)[:250];last.append(err);log_attempt(r,url,err)
  return None
 result=try_urls(list(urls))
 if result:return rid,result
 result=try_urls([r["primary_url"]])
 if result:return rid,result
 result=try_urls([u for u in urls if u not in tried] if not rid.startswith("D") else [])
 if result:return rid,result
 if rid.startswith("D"):
  for blob,final,p in pages:
   txt=p.text()
   if len(txt)>6500 and identity(r["title"],txt[:18000])>.4 and "just a moment" not in txt[:300].lower():
    folder=ROOT/GROUPS[r["dimension"]];folder.mkdir(exist_ok=True)
    target=folder/(stem(r)+".html");target.write_bytes(blob)
    textfile=target.with_suffix(".txt");textfile.write_text(txt,encoding="utf-8")
    return rid,{"status":"html_fulltext","path":str(target.relative_to(ROOT)),"text_path":str(textfile.relative_to(ROOT)),"download_url":final,"version":"original institutional web report; not a journal paper","bytes":len(blob),"sha256":hashlib.sha256(blob).hexdigest(),"text_chars":len(txt),"downloaded_utc":now()}
 return rid,{"status":"pending_fulltext","errors":last[-5:],"attempted_urls":sorted(tried),"landing_urls":[u for _,u,_ in pages],"updated_utc":now()}
def checkpoint():
 MANIFEST.write_text(json.dumps(STATE,ensure_ascii=False,indent=2),encoding="utf-8")
def main():
 shutil.copy2(CATALOG,META/"catalog_80_snapshot.json")
 selected=set(sys.argv[1:])
 tasks=[r for r in RECORDS if not selected or r["id"] in selected]
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  pending={pool.submit(collect,r):r for r in tasks}
  for f in concurrent.futures.as_completed(pending):
   r=pending[f]
   try:rid,result=f.result()
   except Exception as e:rid,result=r["id"],{"status":"pending_fulltext","errors":[str(e)]}
   STATE[rid]=result;checkpoint()
   print(json.dumps({"id":rid,"status":result["status"],"pages":result.get("pages"),"errors":result.get("errors",[])},ensure_ascii=True),flush=True)
 print("COUNTS",json.dumps({s:sum(x.get("status")==s for x in STATE.values()) for s in {x.get("status") for x in STATE.values()}}),flush=True)
if __name__=="__main__":
 sys.stdout.reconfigure(encoding="utf-8");main()

