from pathlib import Path
import concurrent.futures, hashlib, io, json, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pypdf import PdfReader

ROOT=Path(__file__).parent
SOURCES=[
("awwad_2026","https://aclanthology.org/2026.politicalnlp-1.23.pdf","pdf"),
("kaur_2025","https://aclanthology.org/2025.findings-emnlp.1241.pdf","pdf"),
("bisbee_2026","https://www.jamesbisbee.com/assets/pdf/ai_pandering_2_25_2026.pdf","pdf"),
("bang_2024","https://aclanthology.org/2024.acl-long.600.pdf","pdf"),
("nadeem_2026","https://aclanthology.org/2026.acl-long.1689.pdf","pdf"),
("papaioannou_2026","https://link.springer.com/article/10.1007/s43681-026-01138-8","html"),
("germani_2025","https://pmc.ncbi.nlm.nih.gov/articles/PMC13142764/","html"),
("smirnov_2026","https://arxiv.org/html/2601.12164v6","html"),
("polibias_2026","https://arxiv.org/html/2608.06123v1","html"),
("framingqa_2026","https://arxiv.org/html/2609.07448v2","html"),
("dubois_2026","https://arxiv.org/html/2602.23971v4","html"),
("elfes_2026","https://arxiv.org/html/2601.07398v2","html"),
("yoo_2025","https://aclanthology.org/2025.emnlp-main.856.pdf","pdf"),
("guey_2026","https://arxiv.org/html/2503.23688v2","html"),
]
class Text(HTMLParser):
 def __init__(self):
  super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ("script","style"):self.skip+=1
  if not self.skip and tag in ("p","div","section","h1","h2","h3","h4","li","tr","br"):self.out.append("\n")
 def handle_endtag(self,tag):
  if tag in ("script","style") and self.skip:self.skip-=1
  if not self.skip and tag in ("p","div","section","h1","h2","h3","h4","li","tr"):self.out.append("\n")
 def handle_data(self,s):
  if not self.skip:self.out.append(s)
def fetch(spec):
 name,url,kind=spec
 try:
  req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (research literature reading)"})
  with urllib.request.urlopen(req,timeout=40) as response:
   blob=response.read();final=response.url
  if kind=="pdf":
   if not blob.startswith(b"%PDF"):raise ValueError("Not a PDF response")
   (ROOT/"sources"/(name+".pdf")).write_bytes(blob)
   reader=PdfReader(io.BytesIO(blob))
   txt="\n".join("\n=== PDF PAGE "+str(i+1)+" ===\n"+(page.extract_text() or "") for i,page in enumerate(reader.pages))
  else:
   parser=Text();parser.feed(blob.decode("utf-8",errors="replace"))
   txt="\n".join(" ".join(line.split()) for line in "".join(parser.out).splitlines() if line.strip())
  target=ROOT/"sources"/(name+".txt")
  target.write_text(txt,encoding="utf-8")
  return {"id":name,"requested_url":url,"resolved_url":final,"kind":kind,"bytes":len(blob),"sha256":hashlib.sha256(blob).hexdigest(),"text_chars":len(txt),"text_path":str(target),"fetched_utc":datetime.now(timezone.utc).isoformat()}
 except Exception as exc:return {"id":name,"requested_url":url,"error":str(exc)}
if __name__=="__main__":
 (ROOT/"sources").mkdir(parents=True,exist_ok=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(fetch,SOURCES))
 (ROOT/"source_manifest.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
 for result in results:print(json.dumps(result,ensure_ascii=True))

