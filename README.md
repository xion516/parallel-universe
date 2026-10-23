# Parallel Universe

研究同一AI如何随提问语言、用户身份、本土政治框架、联网检索和用户追问，对国际冲突形成不同回答与叙事。

## 阅读入口

| 材料 | 内容 |
|---|---|
| [项目原始资料](<Basic Idea/>) | 研究构想PPT与会议逐字稿 |
| [文献版图与创新性初筛](<Literature_Review/2026-10-22/README.md>) | H1—H5文献地图；第2节按维度比较直接近邻研究 |
| [80条完整文献目录](<Literature_Review/2026-10-22/literature_catalog.md>) | 作者、出处、发表状态、与项目关系及核验层级 |
| [文献全文库](<Literature_Library/>) | 分类论文PDF、机构报告、正文提取与下载/验证记录 |
| [Framing正文核查](<Literature_Review/2026-10-22/framing_deep_dive/README.md>) | 研究问题、测量、结果、贡献主张及正文核查 |
| [Results与不一致测量](<Literature_Review/2026-10-23/results_measurement/README.md>) | 16项直接相关研究的结果变量与测量验证 |
| [逐篇测量与Results核查](<Literature_Review/2026-10-23/results_measurement/逐篇测量与Results核查.md>) | 逐篇方法、结果和验证细节 |
| [Elfes叙事角色与分化测量详解](<Literature_Review/2026-10-23/results_measurement/Elfes_叙事角色与分化测量详解.md>) | 行动者角色、叙事重叠、分化测量和验证 |
| [Dawei Xiong的阶段性判断（独立署名）](<Research_Notes/2026-10-23_Dawei_Xiong_研究判断.md>) | 保留本人对创新性、验证与发表方向的原文判断 |
| [文献核对与研究定位讨论](<Research_Notes/2026-10-23_文献核对与研究定位讨论.md>) | Codex单独分析；补查政治学／公共管理期刊及人类后果研究 |
| [全项目资料索引](PROJECT_INDEX.md) | 可在GitHub直接打开的逐文件相对链接 |

## 资料与研究状态

- Basic Idea保留原始项目资料；文献检索、下载归档和正文核查按各自目录组织。
- 80条是前期文献目录的记录数；后续专题包含补充研究。论文PDF取得、元数据核验、正文精读和研究结论核验是不同层次，以各记录中的状态为准。
- 发表版、预印本、作者稿和机构技术报告分别标记；待补全文和待核事项保留在相应清单。
- 原80条已有76篇论文PDF和2份机构报告HTML；F06、R02仍待补全文。Framing专题核查14项，Results专题核查16项，不等于80条均已精读。原库之外的发表定位补查单列在Research_Notes。
- Dawei Xiong的署名判断与Codex的文献核对、分析和建议分开保存。
- 阅读材料使用仓库相对链接；原始下载日志和来源JSON中的历史本机路径保留作溯源。
- Git记录项目资料、PDF、提取文本、脚本与核验结果；忽略凭据、本机设置、Python缓存和临时文件。
- 仓库保留原始资料与归档证据的字节内容，不自动转换换行符。

资料建立于2026-10-22起；本仓库于2026-10-23初始化。

## 归档维护

在仓库根目录执行 `python tools/prepare_repository.py`，可将研究文档中的本机链接转为相对链接、更新全项目索引，并核对本地链接、76篇原库PDF哈希和冻结目录。最新结果见[仓库检查记录](tools/repository_validation.json)。第三方复现说明按原文保留，链接指向其上游文件。

Results的两项数字复算使用 `python Literature_Review/2026-10-23/results_measurement/recalculate_tables.py`。它基于归档表格和公开标签，不调用模型，也不等于独立重做人类编码或论文实验。
