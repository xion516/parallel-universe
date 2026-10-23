# 检索说明与核验边界

- 检索截止：2026-10-22。
- 项目范围：语言（H1）、用户身份（H2）、本土政治框架（H3）、联网检索（H4）、一次用户反驳（H5）；另补跨模型、测量、人类结果和水资源冲突。
- 产物用途：为相关工作与创新性判断建立可继续精读的地图。不是按预先注册流程完成的系统综述；没有估计检索召回率，也没有以本轮未命中证明不存在。
- 项目原始PPT与逐字稿未改动。本目录是新增研究材料。

## 使用的来源层次

1. 发现：跨主题网络检索、SciSpace语义检索、直接近邻文章的相关工作线索。
2. 书目/状态校验：ACL Anthology、ICLR/ICML/NeurIPS/COLM官方论文页或论文集、出版社和期刊页面、arXiv版本页、作者原始论文与机构库。
3. 追加状态核验：出版社提交的Crossref DOI元数据，尤其是作者、在线/卷期年份和更新声明关系。
4. 机构报告：Anthropic、OpenAI原始评测说明，单独标注，不计为同行评议论文。

没有用二手报道代替论文标题与发表状态。作者仓库的接收声明弱于出版社正式目录，已对R02单独标注。

## 计数及合并原则

共80条：58条已发表学术论文/理论/综述，19条尚未确认正式发表的预印本或工作论文，1条作者仓库报告接收，2份机构技术报告。

- 80是记录数，不是直接竞争论文数，更不是已全文精读数量。
- 版本相同的预印本和正式论文尽量合并，优先正式版。
- BordIRLines的2024工作坊版与2025扩展版合并记录；原始BorderLines与BordIRLines因任务扩展分别保留。
- 2024在线/2025卷期、2025在线/2026卷期等情况在出处中注明；目录年份不是声称某研究此前不存在。
- 作者字段含et al.时是缩写展示。JSON是工作目录，不是声称可直接导入文献管理器的完整BibTeX。
- 政治量表、人口公平、移民、水外交等是邻近研究，已在每条“与本项目关系”中限制推论范围。

## 核验深度如何读

- “元数据与摘要/出版记录与摘要”：确认了原始条目及其摘要中的设计或结果，未据此推断全文未包含的条件。
- “摘要及正文开头”：已读到原始正文部分，仍不是全文精读。
- “正文方法段/方法与结果段/附录与局限”：对最接近研究的相应部分作了针对性核验，不代表逐页审查统计与复现代码。
- “正文检索片段”：原始论文文本可检索但访问受限；相应判断限于检索可见内容。
- “作者原始仓库”：确认作者声明与项目资料，不等于核实了出版社正式发表。

目录中的“关系”和候选贡献是本轮综合判断；“研究内容”尽量限定为原文报告的范围。

## 可复跑检索式

以下是按本轮主题整理的规范化检索式，便于后续扩展；不是声称逐字符完整保存了所有搜索调用。

### 语言与地缘政治

- multilingual large language models geopolitical bias territorial disputes
- same question different language political bias LLM Russian Ukrainian
- Hindi Urdu India Pakistan LLM political bias
- Arabic Hebrew Israel Palestine multilingual language model bias
- Amharic Arabic Ethiopia Egypt GERD Nile LLM narrative bias
- BorderLines territorial disputes language models
- language conditioned ideological divergence contested political documents
- multilingual political opinions transfer Western languages
- large language models ideology creators multilingual
- bilingual Taiwan sovereignty benchmark
- cross lingual political framing migration English Arabic
- language framing historical narrative Asia Minor 1922

### 用户身份、角色与来源

- user nationality political sycophancy language models
- inferred auditor political bias audits LLM
- identity persona multilingual political compass LLM
- implicit user identity interaction context sycophancy
- political personalization ideological chameleons Brazilian
- AI pandering diverging political realities conversation
- author nationality source framing bias large language models
- user demographics intersectional sycophancy
- dialect identity matched guise language model bias

### 框架与迎合追问

- native partisan framing political questions large language models
- source framing systematic bias LLM
- argument driven sycophancy user rebuttal
- are you sure flipflop experiment language models
- multi turn political sycophancy stance stability
- multilingual sycophancy language alignment failure
- ask don't tell reducing sycophancy framing
- compositional framing effect FramingQA
- political response stability under stress PReSS

### 搜索、检索与信息环境

- multilingual retrieval augmented generation geopolitical bias BordIRLines
- political bias retrieved documents generated responses RAG
- generative echo chamber LLM powered search diverse information seeking
- Answer Bubbles AI mediated search
- AI search news source citing patterns
- fair ranking retrieval augmented generation political bias
- query language preference cross lingual knowledge disparities
- search engine personalization Israel Palestine language
- political fact checking reasoning web search curated context

### 测量、理论与人类后果

- political compass spinning arrow language models evaluation
- narrative polarization actors victims responsibility common ground
- multilingual Wikipedia divergent historical narratives Rashomon
- media frames corpus cross country generalizability
- echo chambers epistemic bubbles Nguyen
- conversational AI political persuasion information density
- sycophantic AI prosocial intentions dependence
- AI democratic deliberation common ground Habermas machine
- artificial intelligence water diplomacy expert interviews

## 本轮尚未解决的具体问题

1. 未建立80篇全文的逐段差异矩阵。创新性结论应优先建立在README列出的最近邻精读上。
2. 对个别预印本未确认正式发表，不应把“本轮未确认”写成“肯定未发表”。
3. R02的SIGIR 2026接收来自作者仓库，仍需出版社目录或正式论文核实；未混入58条正式发表记录。
4. 尼罗河阿姆哈拉语—埃及阿拉伯语的完整对应审计本轮未检出；需继续用阿拉伯语/阿姆哈拉语检索和领域作者追踪，不能据此主张首次。
5. Poli-Bias的英语、单轮边界在正文已明示；其他仅摘要核验的文章没有提及某设计时，不按“未做”处理。
6. 原始模型、工具、搜索产品和版本会更新。论文结论对应其审计配置，不能直接当作2026-10-22所有产品的实时性能判断。
7. H05的编辑关注声明仅核实了原始出版社元数据和更新关系，未把声明解释为撤稿或不端结论，也未对后续争议作独立裁决。
8. 本轮发现不能证明某个完整的五因素设计此前无人做过，也不能用“组合更多条件”自动证明学术贡献。

## 追加核验事实

- M10：Crossref出版社元数据记录2026-08-10在线发表；作者为Jan Elfes、Marco Bastos、Luca Maria Aiello。
- G01：Crossref出版社元数据记录2026-03-25发表；DOI为10.1057/s41599-026-06577-6。
- H05：编辑声明DOI为10.1126/science.aej2383；出版社Crossref元数据的update-to指向10.1126/science.adq1814，类型expression_of_concern，日期2026-06-11。
- L02：正式ACL条目列10位作者；目录使用正式版作者名单，2024工作坊版作为补充来源而非重复独立记录。

原始链接集中保留在每条目录及JSON中；本说明不代替文章自身的方法、统计和规范立场审查。

