from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from urllib.parse import urlparse
import hashlib, html, json, os, re, subprocess, sys, xml.etree.ElementTree as ET
import download_library as d

ROOT, META = d.ROOT, d.META
STATUS = {"pdf_downloaded": "PDF全文已下载", "html_fulltext": "机构报告网页全文已归档", "pending_fulltext": "待补全文"}
SPECIAL = {
 "R01": "作者网站公开的 CHI 会议排版稿",
 "R03": "作者接受稿（作者网站；机构库亦列为 Accepted author manuscript）",
 "R04": "作者网站公开的 ICTIR 会议排版稿",
 "R06": "期刊正式 PDF；韩文正文，附英文标题和摘要",
 "R12": "机构库公开的 IEEE Access 正式发表版",
 "I07": "作者网站公开的 PNAS 正式发表版",
 "M11": "大学课程网站公开的期刊排版扫描件",
 "M12": "作者网站公开的期刊排版稿；PDF另附目录页",
 "M13": "大学课程网站公开的 Science 正式发表版",
 "M14": "作者网站公开的 Econometrica 正式发表版",
 "M15": "作者网站公开的 CHI 会议排版稿",
 "M18": "作者网站公开的 penultimate draft（接近定稿的作者稿）；引用正式发表版",
 "H01": "公开副本的 Science 正式发表版；1页研究摘要加9页研究正文",
 "H03": "公开副本的 Science 正式发表版；含研究摘要页",
 "H04": "LSE机构库的作者接受稿，含封面和补充材料，共139页",
 "H05": "Wharton作者公开稿；正文注明 definitive version will be published in Science；含补充材料",
 "F07": "作者网站工作论文，文件日期2026-02-25；非期刊正式版",
 "F01": "arXiv预印本（题名含 evaluation bias）；另存正式发表的完整XML正文",
}
NOTES = {
 "F01": "PDF题名为 Source framing triggers systematic evaluation bias in Large Language Models；与正式发表题名有差异。以同一作者、相同研究和正式发表XML核对身份；细读或引用正式结果时优先查看本地正式发表XML/正文文本。",
 "R01": "原目录题名写作 Effect；本次按下载稿题名校正为 Effects，保留原始目录快照。",
 "R02": "本次通过出版社提交的Crossref记录核实SIGIR 2026正式发表、DOI及页码；更新了原目录仅有作者仓库接收声明的状态。全文下载仍受ACM访问错误阻挡。",
 "R03": "年份沿用作者机构库的2025会议年份；该机构库的版权字段标2026。正式引用时请核对所采用的会议年份/卷册年份。机构库：https://researchportal.tuni.fi/en/publications/refarag-re-ranking-forbias-mitigation-inretrieval-augmented-gener/",
 "R06": "全文为韩文，不是英语正文。身份通过首页英文标题、作者和DOI 10.5626/JOK.2026.53.9.824核对。",
 "F06": "DOI与作者/会议元数据已核实；出版社请求返回403，浏览器停留在安全验证页面；作者主页未提供可下载全文。没有把摘要计作全文。",
 "H05": "Science于2026-06-11发布Editorial Expression of Concern；不是撤稿。具体通知DOI：10.1126/science.aej2383；PubMed：https://pubmed.ncbi.nlm.nih.gov/42275523/ 。本地文件为2024年作者稿，不能视为后续修订分析的最终版本。",
 "L15": "有关结果解释的细节请结合项目现有framing深读报告核对；下载归档不等于重新完成结果评审。",
 "D01": "该条是Anthropic机构网页报告。另有2页Appendix PDF，单独标为附录，不把附录计作主报告全文。",
 "D02": "该条是OpenAI机构网页报告；不是同行评议论文。原始HTML可能依赖在线样式，离线阅读可使用同目录TXT。",
}
TAGS = {
 "F01": ["来源身份框架", "同文异源", "模型评判"],
 "F02": ["国际冲突", "框架操纵"],
 "F03": ["论证框架", "迎合"],
 "F04": ["问题与断言", "迎合"],
 "F05": ["问题框架组合", "测量"],
 "F06": ["等价框架", "下游任务"],
 "F07": ["对话框架", "政治现实分化"],
 "L14": ["历史叙事框架", "跨语言"],
 "L15": ["输出框架", "跨语言转移"],
 "M08": ["媒体框架语料", "人工标注"],
 "M09": ["媒体框架语料", "跨国泛化"],
 "M11": ["框架理论", "选择与凸显"],
 "M12": ["框架理论", "综述"],
 "M13": ["等价框架", "人类决策"],
 "I01": ["推断用户身份", "迎合"],
}

def write_json(path, obj):
 path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

def link(label, path):
 return f"[{label}](<{Path(path).resolve().as_posix()}>)"

def write_markdown(path, content):
 # Resolve each generated link relative to its own document for GitHub/clones.
 def relative(match):
  target = Path(match.group(1))
  if not target.is_absolute(): return match.group(0)
  return "](<" + Path(os.path.relpath(target, path.parent)).as_posix() + ">)"
 path.write_text(re.sub(r'\]\(<([^>\n]+)>\)', relative, content), encoding="utf-8")

def cell(s):
 return str(s).replace("|", "\\|").replace("\n", " ")

def version(r, v):
 if r["id"] in SPECIAL: return SPECIAL[r["id"]]
 if v["status"] == "pending_fulltext": return "尚未取得全文，未指定本地版本"
 if v["status"] == "html_fulltext": return "机构原始网页报告（HTML及TXT）；非同行评议论文"
 if "arxiv.org" in v.get("download_url", ""): return "arXiv预印本；与正式发表版是否一致未逐字比对"
 if any(s in v.get("download_url", "") for s in ("aclanthology.org", "nature.com", "springer.com", "plos.org", "aaai.org", "mlr.press", "proceedings.iclr.cc", "papers.nips.cc")):
  return "出版社/正式论文集PDF"
 return "公开全文PDF；文件来源见下载链接"

def main():
 sys.stdout.reconfigure(encoding="utf-8")
 records = json.loads((META/"catalog_80_snapshot.json").read_text(encoding="utf-8"))["records"]
 state = json.loads(d.MANIFEST.read_text(encoding="utf-8"))
 assert len(records) == len(state) == len({r["id"] for r in records}) == 80
 # Preserve the institutional appendix separately from the main web report.
 r = next(r for r in records if r["id"] == "D01")
 appendix = ROOT/d.GROUPS[r["dimension"]]/(d.stem(r)+".pdf")
 appendix_target = appendix.with_stem(appendix.stem+"_Appendix")
 if appendix.exists() and not appendix_target.exists(): appendix.rename(appendix_target)
 if appendix_target.exists():
  state["D01"]["supplements"] = [{"path": str(appendix_target.relative_to(ROOT)), "description": "独立附录，2页，不计作主报告全文", "pages": 2, "download_url": "https://www-cdn.anthropic.com/bb224ffec0bd87a4f885bd30b187606064a86ea5.pdf", "sha256": hashlib.sha256(appendix_target.read_bytes()).hexdigest()}]
 audits, enriched, hashes = [], [], {}
 for original in records:
  r = dict(original); rid = r["id"]; v = state[rid]
  if rid == "R01":
   r["original_catalog_title"] = r["title"]
   r["title"] = "Generative Echo Chamber? Effects of LLM-Powered Search Systems on Diverse Information Seeking"
  if rid == "R02":
   cr = json.loads((META/"R02_crossref.json").read_text(encoding="utf-8"))
   r["original_catalog_publication_status"] = r["publication_status"]
   r["venue"] = "SIGIR 2026, pp. "+cr.get("page", "2242–2252")
   r["publication_status"] = "已发表（本次Crossref核实出版社提交的元数据）"
   r["doi"] = cr["DOI"]; r["publisher_url"] = "https://doi.org/"+cr["DOI"]
  folder = ROOT/d.GROUPS[r["dimension"]]; folder.mkdir(exist_ok=True)
  card_path = (ROOT/v["path"]).with_suffix(".md") if v.get("path") else folder/(d.stem(r)+".md")
  v["record_path"] = str(card_path.relative_to(ROOT)); v["version_zh"] = version(r, v)
  if v["status"] == "pdf_downloaded":
   path = ROOT/v["path"]; data = path.read_bytes(); sha = hashlib.sha256(data).hexdigest()
   assert sha == v["sha256"] and data.startswith(b"%PDF"), rid
   assert sha not in hashes, f"duplicate PDFs: {rid}, {hashes.get(sha)}"
   hashes[sha] = rid
   rd = d.PdfReader(path); assert len(rd.pages) == v["pages"]
   first = rd.pages[0].extract_text() or ""; score = d.identity(r["title"], first[:1800])
   compact = "".join(first.split())
   if rid == "R06":
    assert "10.5626/JOK.2026.53.9.824" in compact and "TheImpactofRetrievedDocumentBias" in compact
    evidence = "首页DOI及去空格后的英文标题一致（韩文期刊的英文标题无正常空格）"
   elif rid == "L14":
    assert "10.1007/s43681-026-01138-8" in first and d.identity(r["title"], first) >= .9
    evidence = "首页DOI和完整题名一致；双栏PDF提取顺序使题名位于首页文本末尾"
   else:
    assert score >= .72, (rid, score)
    evidence = "首页标题区题名关键词匹配通过；实际PDF页数和SHA256通过"
   v["identity_check"] = evidence
   text_path = path.with_suffix(".txt")
   extracted = subprocess.run([r"C:\Users\David\anaconda3\Library\bin\pdftotext.exe", "-layout", "-enc", "UTF-8", str(path), "-"], capture_output=True, timeout=45, check=True).stdout.decode("utf-8", errors="replace")
   text_path.write_text("本文件为PDF自动提取文本，仅供检索；排版、图表和页码请以PDF为准。\n"+r["title"]+"\n\n"+extracted, encoding="utf-8")
   v["text_path"] = str(text_path.relative_to(ROOT))
   audits.append({"id": rid, "pages": len(rd.pages), "heading_score": score, "evidence": evidence, "sha256": sha, "first_page_excerpt": first[:400]})
   if "arxiv.org" in v.get("download_url", ""):
    m = re.search(r"arXiv:\s*([0-9.]+v\d+)", first)
    if m: v["arxiv_version_from_pdf"] = m.group(1)
  elif v["status"] == "html_fulltext":
   data = (ROOT/v["path"]).read_bytes(); assert hashlib.sha256(data).hexdigest() == v["sha256"]
   text = (ROOT/v["text_path"]).read_text(encoding="utf-8")
   assert len(text)>10000 and r["title"].lower() in text.lower(), rid
   audits.append({"id": rid, "format": "HTML", "text_chars": len(text), "sha256": v["sha256"], "evidence": "机构原始页面及正文TXT；题名、正文长度核对通过"})
  else:
   assert rid in ("F06", "R02"), rid
   v["reason_zh"] = "ACM下载请求返回HTTP403；浏览器安全验证未能完成；未在作者公开渠道找到可下载全文。无法判定为付费墙。"
   v["followup_zh"] = "可通过学校ACM订阅/馆际互借取得，或由研究者联系作者获取作者接受稿。"
  if v.get("formal_fulltext_xml_path"):
   xp = ROOT/v["formal_fulltext_xml_path"]; tree = ET.parse(xp)
   assert tree.findtext(".//article-id[@pub-id-type='doi']") == "10.1126/sciadv.adz2924"
   lines = ["正式发表XML正文的纯文本提取；图表、公式及版式请核对XML/正式期刊版本。", r["title"]]
   for block in tree.getroot():
    lines.append("\n"+block.tag.upper()+"\n")
    for e in block.iter():
     if e.tag in ("article-title", "title", "p", "table-wrap", "fig", "ref"):
      lines.append(" ".join("".join(e.itertext()).split()))
   txt = xp.with_name(xp.stem+"_published_fulltext.txt"); txt.write_text("\n\n".join(lines), encoding="utf-8")
   v["formal_fulltext_text_path"] = str(txt.relative_to(ROOT)); v["formal_fulltext_xml_sha256"] = hashlib.sha256(xp.read_bytes()).hexdigest()
  v["notes_zh"] = NOTES.get(rid, "")
  r["tags_zh"] = TAGS.get(rid, [r["dimension"]]); r["download"] = v
  lines = [f"# {rid} · {r['title']}", "", f"作者：{r['authors_display']}", "", f"年份：{r['year']}  \n发表场所：{r['venue']}  \n发表状态：{r['publication_status']}", "", f"分类：{r['dimension']}  \n阅读优先级：{r['reading_priority']}  \n标签：{' / '.join(r['tags_zh'])}", "", f"全文状态：**{STATUS[v['status']]}**  \n本地版本：{v['version_zh']}", ""]
  if v.get("path"):
   lines.extend([link("打开本地全文", ROOT/v["path"]), "", link("检索用纯文本", ROOT/v["text_path"]), ""])
  else: lines.extend([v["reason_zh"], "", v["followup_zh"], ""])
  if v.get("formal_fulltext_xml_path"):
   lines.extend([link("正式发表完整XML正文", ROOT/v["formal_fulltext_xml_path"])+" · "+link("正式发表正文TXT", ROOT/v["formal_fulltext_text_path"]), "", f"正式全文来源：[{v['formal_fulltext_xml_url']}]({v['formal_fulltext_xml_url']})", ""])
  for s in v.get("supplements", []): lines.extend([link(s["description"], ROOT/s["path"]), ""])
  lines.extend(["## 来源", "", f"[原始目录来源]({r['primary_url']})", ""])
  if r.get("publisher_url"): lines.extend([f"[本次核实的出版社DOI]({r['publisher_url']})", ""])
  if v.get("download_url"): lines.extend([f"[实际下载来源]({v['download_url']})", ""])
  if v.get("pages"): lines.extend([f"PDF实际页数：{v['pages']}（可能包含封面、摘要页和补充材料）", ""])
  if v.get("sha256"): lines.extend([f"SHA256：`{v['sha256']}`", ""])
  lines.extend(["## 原目录研究说明", "", r["study_summary_zh"], "", "与项目的关系："+r["relationship_to_project_zh"], "", "原目录核验深度："+r["verification_depth_zh"], "", "上述说明沿用前期文献目录；本次归档核验文件身份与可用性，不代表已逐篇重新评审全部结果。", ""])
  if v["notes_zh"]: lines.extend(["## 版本与引用备注", "", v["notes_zh"], ""])
  write_markdown(card_path, "\n".join(lines)); enriched.append(r)
  print(rid, v["status"], flush=True)
 counts = Counter(v["status"] for v in state.values())
 framing_sections = [
  ("直接研究提问、来源或对话框架", ["F01", "F02", "F03", "F04", "F05", "F06", "F07"]),
  ("跨语言输出与历史叙事框架", ["L14", "L15"]),
  ("框架识别、语料和理论基础", ["M08", "M09", "M11", "M12", "M13"]),
  ("推断提问者身份的相邻机制", ["I01"]),
 ]
 by_id = {r["id"]: r for r in enriched}
 frame = ["# Framing阅读入口", "", "这是原80条文献中的主题交叉索引，不增加文献条目。F06尚未取得全文；其余条目可从下方进入本地文件。", ""]
 for title, ids in framing_sections:
  frame.extend(["## "+title, "", "| ID | 研究 | 状态/版本 |", "|---|---|---|"])
  for rid in ids:
   r = by_id[rid]; v = r["download"]
   frame.append(f"| {rid} | {link(cell(r['title']), ROOT/v['record_path'])} | {STATUS[v['status']]}；{cell(v['version_zh'])} |")
  frame.append("")
 frame.extend(["项目已有的framing深读材料另存于 Literature_Review/2026-10-22/framing_deep_dive；其中后续补充的其他论文不计入本次80条归档。", ""])
 write_markdown(ROOT/"FRAMING阅读入口.md", "\n".join(frame))
 index = ["# 80条文献完整索引", "", "归档日期：2026-10-22。78条学术论文/工作论文 + 2条机构报告。全文取得情况与发表状态分开记录。", "", f"PDF全文{counts['pdf_downloaded']}；机构报告HTML全文{counts['html_fulltext']}；待补全文{counts['pending_fulltext']}。", "", "| ID | 年份 | 作者 | 题名与记录 | 分类 | 发表场所 | 全文 | 版本 | 优先级 |", "|---|---:|---|---|---|---|---|---|---|"]
 for r in enriched:
  v=r["download"]
  index.append(f"| {r['id']} | {r['year']} | {cell(r['authors_display'])} | {link(cell(r['title']), ROOT/v['record_path'])} | {cell(r['dimension'])} | {cell(r['venue'])} | {STATUS[v['status']]} | {cell(v['version_zh'])} | {r['reading_priority']} |")
 write_markdown(ROOT/"文献总目录_80条.md", "\n".join(index)+"\n")
 readme = ["# Parallel Universe 文献库", "", "对应前期文献目录的80条记录：78条学术论文/工作论文、2条机构评测报告。保留原L/I/F/S/R/G/M/H/D编号，并按8类存放。", "", f"**已取得{counts['pdf_downloaded']}篇论文PDF、{counts['html_fulltext']}份机构报告网页全文；{counts['pending_fulltext']}篇待补全文。** 另有1份Anthropic报告附录，单独标记，不计入论文PDF数。", "", link("80条完整目录", ROOT/"文献总目录_80条.md")+" · "+link("Framing阅读入口", ROOT/"FRAMING阅读入口.md")+" · "+link("待补全文清单", ROOT/"待补全文清单.md"), "", "## 分类目录", "", "| 分类 | 条目 | 已取PDF | 网页全文 | 待补 |", "|---|---:|---:|---:|---:|"]
 for group, dirname in d.GROUPS.items():
  subset = [r for r in enriched if r["dimension"] == group]; c = Counter(r["download"]["status"] for r in subset)
  readme.append(f"| {link(group, ROOT/dirname/'README.md')} | {len(subset)} | {c['pdf_downloaded']} | {c['html_fulltext']} | {c['pending_fulltext']} |")
  lines = ["# "+group, "", f"共{len(subset)}条：PDF {c['pdf_downloaded']}；网页全文 {c['html_fulltext']}；待补 {c['pending_fulltext']}。", "", link("返回文献库入口", ROOT/"README.md"), "", "| ID | 年份 | 作者 | 题名与记录 | 本地全文 | 优先级 |", "|---|---:|---|---|---|---|"]
  for r in subset:
   v=r["download"]; full=link("PDF" if v["status"]=="pdf_downloaded" else "HTML", ROOT/v["path"]) if v.get("path") else "待补全文"
   lines.append(f"| {r['id']} | {r['year']} | {cell(r['authors_display'])} | {link(cell(r['title']), ROOT/v['record_path'])} | {full} | {r['reading_priority']} |")
  write_markdown(ROOT/dirname/"README.md", "\n".join(lines)+"\n")
 readme.extend(["", "## 使用方法与版本", "", "每条文献有独立MD记录，包含作者、年份、发表场所、研究主题、与项目关系、阅读优先级、实际下载链接、版本及文件校验信息。论文PDF旁附自动提取的TXT，便于本地全文搜索；版式、图表和引文页码以PDF为准。", "", "从arXiv取得的文件标为预印本，即使同一研究后来已正式发表，也不自动称为出版社最终版。R03/H04是作者接受稿，M18是作者接近定稿的版本，H05是作者公开稿。F01另有正式发表的完整XML和正文TXT，可与预印本PDF对照。", "", "H05有2026-06-11的Editorial Expression of Concern，记录页已附通知链接。D01/D02为机构网页报告，不是同行评议论文。", "", "## 核验范围", "", "全部已归档PDF经过文件格式、实际页数、首页标题或DOI、SHA256和重复文件核对；两份网页报告保存原HTML与完整正文TXT。该文件核验不等于对80篇研究结果进行新的逐篇证据评审。", "", "原始研究文件及前期目录保留不变；本目录是新建的下载归档。原目录快照、逐次下载记录、合并后的机器可读目录和最终验证结果保存在00_目录与下载记录。", "", "归档日期：2026-10-22。"])
 write_markdown(ROOT/"README.md", "\n".join(readme)+"\n")
 gap = ["# 待补全文清单", "", "仅列尚未取得论文完整正文的条目。摘要、作者主页、代码仓库和元数据不计作全文。", ""]
 for r in enriched:
  v=r["download"]
  if v["status"] != "pending_fulltext": continue
  gap.extend([f"## {r['id']} · {r['title']}", "", f"{r['authors_display']} · {r['year']} · {r['venue']}", "", link("本地记录", ROOT/v["record_path"]), "", f"[出版社/DOI]({r.get('publisher_url',r['primary_url'])})", "", v["reason_zh"], "", "后续获取途径："+v["followup_zh"], ""])
 gap.extend(["这两条保留在原分类中，可通过现有ID补入文件；无需重新编号。", ""])
 write_markdown(ROOT/"待补全文清单.md", "\n".join(gap))
 write_json(d.MANIFEST, state)
 write_json(META/"library_catalog_80.json", {"archive_date": "2026-10-22", "counts": dict(counts), "records": enriched})
 write_json(META/"pdf_identity_audit.json", audits)
 # Remove only our temporary candidate binaries, retaining their hashes as audit evidence.
 excluded=[]
 candidates=list(META.glob("*candidate*.pdf"))+list(META.glob("F01_arxiv.pdf"))+list((META/"quarantine").glob("*.pdf"))
 for path in candidates:
  assert path.resolve().is_relative_to(META.resolve())
  data=path.read_bytes(); entry={"temporary_filename":str(path.relative_to(META)), "sha256":hashlib.sha256(data).hexdigest(), "bytes":len(data)}
  try:
   rd=d.PdfReader(path);entry["pages"]=len(rd.pages);entry["first_page_excerpt"]=(rd.pages[0].extract_text() or "")[:400]
  except Exception: entry["note"]="invalid/non-PDF temporary response"
  excluded.append(entry);path.unlink()
 if excluded: write_json(META/"temporary_download_cleanup.json", excluded)
 source_bytes=d.CATALOG.read_bytes();snapshot_bytes=(META/"catalog_80_snapshot.json").read_bytes();assert source_bytes == snapshot_bytes
 validation={"validated_utc":datetime.now(timezone.utc).isoformat(), "record_count":80, "unique_id_count":80, "primary_pdf_count":counts['pdf_downloaded'], "primary_pdf_unique_sha256_count":len(hashes), "institutional_html_fulltext_count":counts['html_fulltext'], "pending_fulltext_ids":[r['id'] for r in enriched if r['download']['status']=='pending_fulltext'], "standalone_appendix_pdf_count":1, "all_pdf_headers_pages_titles_or_dois_and_hashes_checked":True, "original_catalog_unchanged_against_snapshot":True, "original_catalog_sha256":hashlib.sha256(source_bytes).hexdigest(), "pdf_actual_pages_total":sum(v.get('pages',0) for v in state.values()), "main_fulltext_bytes":sum(v.get('bytes',0) for v in state.values())}
 write_json(META/"validation.json",validation)
 print(json.dumps(validation,ensure_ascii=False),flush=True)

if __name__ == "__main__": main()
