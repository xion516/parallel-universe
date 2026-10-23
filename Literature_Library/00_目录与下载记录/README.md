# 目录与下载记录

- `catalog_80_snapshot.json`：本次下载所依据的原始80条目录快照；原目录未修改。
- `library_catalog_80.json`：合并本地文件、版本和来源信息的80条机器可读目录。
- `download_manifest.json`：每条文献的文件路径、下载地址、状态、页数和SHA256。
- `download_attempts.jsonl`：逐次下载尝试与失败原因。
- `pdf_identity_audit.json`：最终PDF/网页身份与文件核验记录。
- `validation.json`：最终数量、重复文件、链接和原目录一致性检查。
- `temporary_download_cleanup.json`：临时文件与误命中候选的哈希记录；这些候选文件已移除，不属于文献库。
- `R02_crossref.json`、`F06_crossref.json`：出版社提交的Crossref元数据。
- `source_overrides.json`：公开作者稿/机构库等候选下载来源。
- `download_library.py`：按原始ID重试下载；不会主动替换已取得的文件。
- `finalize_library.py`：生成记录卡、分类目录及最终验证信息。

下载状态与发表状态分别记录。论文PDF数不包含机构报告附录；未取得全文的条目没有伪装成PDF或以摘要代替全文。
