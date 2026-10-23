# Parallel Universe：80条相关文献目录

检索截止：2026-10-22。与本目录配套的判断见 [研究维度与创新性初筛](README.md)，检索边界见 [检索说明](search_scope.md)。

共80条记录：58条已正式发表的学术论文/理论/综述，19条尚未确认正式发表的预印本或工作论文，1条仅由作者仓库确认接收，2份机构评测。数量包含直接竞争研究、邻近领域和测量/理论基础，不代表80项均完整覆盖本项目。

每条按“谁—在哪发表—研究什么—如何与本项目相接—核验深度”记录。P0为优先比对，P1为主要相关，P2为补充；优先级表示本项目阅读价值，不是论文质量排名。作者名单含 et al. 时为缩写。

## 语言与地缘政治（15条）

### L01 · This Land is Your, My Land: Evaluating Geopolitical Bias in Language Models through Territorial Disputes

- 作者：Bryan Li; Samar Haider; Chris Callison-Burch
- 年份与出处：2024；NAACL 2024，长文
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2024.naacl-long.213/)
- 研究内容：251个争议领土、49种语言，比较归属选择、一致性和地缘偏向，并操纵民族主义者及联合国维和人员角色。
- 与本项目的关系：最接近H1；语言与角色组合已有先例，但模型扮演身份与提问者身份须区分。
- 核验深度：正文方法段；阅读优先级：P0

### L02 · Multilingual Retrieval Augmented Generation for Culturally-Sensitive Tasks: A Benchmark for Cross-lingual Robustness

- 作者：Bryan Li; Fiona Luo; Samar Haider; Adwait Agashe; Siyu Li; Runqi Liu; Miranda Muqing Miao; Shriya Ramakrishnan; Yuan Yuan; Chris Callison-Burch
- 年份与出处：2025；Findings of ACL 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.findings-acl.219/)
- 研究内容：BordIRLines覆盖49种语言的领土争议与Wikipedia文档，比较无检索、提问语言检索、多语言检索等模式。多语言检索通常提升一致性。
- 与本项目的关系：直接覆盖语言×检索×冲突；H4需要区分检索语言组成。同谱系WikiNLP 2024版本合并记录。
- 核验深度：正文方法段；阅读优先级：P0
- 补充原始来源：[来源1](https://aclanthology.org/2024.wikinlp-1.3/)

### L03 · Political biases and inconsistencies in bilingual GPT models—the cases of the U.S. and China

- 作者：Di Zhou; Yinxian Zhang
- 年份与出处：2024；Scientific Reports
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://www.nature.com/articles/s41598-024-76395-w)
- 研究内容：以英文和简体中文询问相同的中美政治问题，发现跨语言知识、态度一致性与批评程度存在差异。
- 与本项目的关系：H1的直接先例，且来自社会学与跨文化信息传播问题。
- 核验深度：摘要及正文开头；阅读优先级：P0

### L04 · Navigating the Political Compass: Evaluating Multilingual LLMs across Languages and Nationalities

- 作者：Chadi Helwe; Oana Balalau; Davide Ceolin
- 年份与出处：2025；Findings of ACL 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.findings-acl.883/)
- 研究内容：15个模型，50个人口大国及其官方语言；分别测试语言、模型国籍角色以及二者组合。
- 与本项目的关系：语言×身份组合已有先例；其身份赋予模型，并不等同于用户说自己是哪国人。
- 核验深度：正文方法段；阅读优先级：P0

### L05 · Large language models reflect the ideology of their creators

- 作者：Maarten Buyl; Alexander Rogiers; Sander Noels; et al.
- 年份与出处：2026；npj Artificial Intelligence
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1038/s44387-025-00048-0)
- 研究内容：19个模型用联合国六种官方语言描述约3991名政治相关人物，比较评价与开发者地区差异。
- 与本项目的关系：跨语言×模型来源已被大规模研究；标题中的开发者解释不能直接当作训练机制的因果识别。
- 核验深度：摘要及正文结果/讨论；阅读优先级：P1

### L06 · Geopolitical Divisions Across Languages in Large Language Models

- 作者：Maxim Chupilkin
- 年份与出处：2026；arXiv:2609.20005
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2609.20005)
- 研究内容：同一组20条俄乌战争陈述，用112种语言询问GPT、Claude和Gemini，共67200条回答，比较亲俄/亲乌程度。
- 与本项目的关系：研究情境和主问题与项目高度重合；不能把俄乌跨语言审计视为新场景。
- 核验深度：元数据与摘要；阅读优先级：P0

### L07 · The Language You Ask In: Language-Conditioned Ideological Divergence in LLM Analysis of Contested Political Documents

- 作者：Oleg Smirnov
- 年份与出处：2026；arXiv:2601.12164，核验v6
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2601.12164)
- 研究内容：给两个模型相同的乌克兰公民社会文件，以语义匹配的俄语和乌克兰语提问，比较合法化、去合法化解读。
- 与本项目的关系：接近同一事实材料下不同叙事，超出了单纯选择题偏向；案例和材料范围较窄。
- 核验深度：元数据与摘要；阅读优先级：P0

### L08 · Bilingual Bias in Large Language Models: A Taiwan Sovereignty Benchmark Study

- 作者：Ju-Chun Ko
- 年份与出处：2026；arXiv:2602.06371
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2602.06371)
- 研究内容：17个模型，中英文台海问题，提出Language Bias Score及Quality-Adjusted Consistency。
- 与本项目的关系：双语政治一致性与质量分离的相关工作；需要进一步审查其答案标准的规范前提。
- 核验深度：元数据与摘要；阅读优先级：P1

### L09 · Multilingual Political Views of Large Language Models: Identification and Steering

- 作者：Daniil Gurgurov; Katharina Trinley; Ivan Vykopal; Josef van Genabith; Simon Ostermann; Roberto Zamparelli
- 年份与出处：2025；Findings of IJCNLP-AACL 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.findings-ijcnlp.17/)
- 研究内容：7个模型、14种语言、每条政治陈述11种等义改写，并研究激活干预的跨语言立场转向。
- 与本项目的关系：说明语言、模型家族、改写稳健性及立场控制已被组合研究。
- 核验深度：出版记录与摘要；阅读优先级：P1

### L10 · Do Political Opinions Transfer Between Western Languages? An Analysis of Unaligned and Aligned Multilingual LLMs

- 作者：Franziska Weeber; Tanise Ceron; Sebastian Padó
- 年份与出处：2026；EACL 2026，长文
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2026.eacl-long.14/)
- 研究内容：5种西方语言的政治建议应用陈述；未对齐模型跨语言显著差异较少，英文DPO对齐近乎统一地改变各语言输出。
- 与本项目的关系：应纳入趋同证据，不能预设所有语言都必然对应本国立场；早期预印本为2025年。
- 核验深度：出版记录与摘要；阅读优先级：P0

### L11 · Unveiling Language-Driven Political Stances in Large Language Models on China and Cross-Strait Relations

- 作者：Yu-Ting Lin; Yao-Chung Fan
- 年份与出处：2024；ROCLING 2024
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2024.rocling-1.18/)
- 研究内容：8个模型，以繁体、简体中文和英文测试中国与两岸政治立场。
- 与本项目的关系：语言变体和模型来源的先例；文字体系不能简单等同于国籍。
- 核验深度：论文首页与摘要；阅读优先级：P1

### L12 · Cultural bias and cultural alignment of large language models

- 作者：Yan Tao; Olga Viberg; Ryan S. Baker; René F. Kizilcec
- 年份与出处：2024；PNAS Nexus
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1093/pnasnexus/pgae346)
- 研究内容：把5个模型回答与跨国价值观调查比较，并测试文化身份提示能否提高文化对齐。
- 与本项目的关系：语言与文化身份是不同构念；提供文化对齐框架及人类调查参照。
- 核验深度：元数据与摘要；阅读优先级：P1

### L13 · Towards Measuring the Representation of Subjective Global Opinions in Language Models

- 作者：Esin Durmus; Karina Nguyen; Thomas I. Liao; et al.
- 年份与出处：2024；COLM 2024
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://openreview.net/forum?id=zl16jLb91v)
- 研究内容：GlobalOpinionQA来自跨国调查，比较国家条件提示和题目翻译；翻译到某语言不一定最接近该语言人群的意见。
- 与本项目的关系：H1不能作为必然关系；同时提供国家视角与语言操纵的先例。
- 核验深度：原始摘要与大会接收记录；阅读优先级：P0
- 补充原始来源：[来源1](https://arxiv.org/abs/2306.16388)

### L14 · Language and the framing of historical narrative in large language models: the case of Asia minor (1922)

- 作者：Christos Papaioannou
- 年份与出处：2026；AI and Ethics 6, article 262
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://link.springer.com/article/10.1007/s43681-026-01138-8)
- 研究内容：以1922年小亚细亚历史叙事比较希腊语和英语的GPT-4o、Claude 3.5回答，分析术语、情绪及责任归属。
- 与本项目的关系：H1×H3的直接先例；并非希腊语与土耳其语双方语言的完整对照。
- 核验深度：出版社摘要与正文开头；阅读优先级：P0

### L15 · Do LLMs Transfer Political Framing across Languages? A Cross-Lingual Analysis of LLM-Generated Discourse

- 作者：Nooredeen Awwad; Ebtihal Ismail Enfes; Kolawole John Adebayo
- 年份与出处：2026；PoliticalNLP 2026工作坊，ELRA
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2026.politicalnlp-1.23/)
- 研究内容：在移民议题上对照英语与阿拉伯语，以GPT-4o和Jais-13B的800次生成结合词汇框架、统计和定性话语分析，识别跨语言框架漂移。
- 与本项目的关系：语言×框架×混合测量已有直接先例；移民议题并非双方国际冲突。
- 核验深度：出版记录与摘要；阅读优先级：P0

## 用户身份与隐含线索（8条）

### I01 · Political Bias Audits of LLMs Capture Sycophancy to the Inferred Auditor

- 作者：Petter Törnberg; Michelle Schimmel
- 年份与出处：2026；arXiv:2604.27633
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2604.27633)
- 研究内容：6个模型、3类政治量表、30990条回答，仅改变提问者明确身份，发现明显且不对称的党派迁移，并探测默认提问者推断。
- 与本项目的关系：H2的直接先例；无身份条件也可能含有模型推断的身份。
- 核验深度：元数据与摘要；阅读优先级：P0

### I02 · LLMs are ideological chameleons: personalized echo chambers in the Brazilian political context

- 作者：Anderson Luis Bento Soares; Bruno Antonio Veiga de Almeida; Leonardo Nascimento Ferreira; Anderson Rocha; Ruben Interian; Zanoni Dias
- 年份与出处：2026；Scientific Reports
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://www.nature.com/articles/s41598-026-52105-6)
- 研究内容：21个模型、47376条回答，巴西政治成对陈述，操纵用户不表态、左倾和右倾，比较相对立场迁移。
- 与本项目的关系：用户立场×问题成对×跨模型已发表；项目需要说明跨冲突和叙事分析的增量。
- 核验深度：摘要及正文开头；阅读优先级：P0

### I03 · GermanPartiesQA: Benchmarking Commercial Large Language Models and AI Companions for Political Alignment and Sycophancy

- 作者：Jan Batzner; Volker Stocker; Stefan Schmid; Gjergji Kasneci
- 年份与出处：2025；AAAI/ACM AIES 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://ojs.aaai.org/index.php/AIES/article/view/36552)
- 研究内容：418条德国选举立场陈述、6个商业模型，以政治人物角色比较立场控制；区分I am与You are。
- 与本项目的关系：作者强调角色可控性不应自动认定为迎合，对项目构念界定尤其重要。2024预印本与2025正式版合并。
- 核验深度：正式论文摘要与开头；阅读优先级：P0

### I04 · Interaction Context Often Increases Sycophancy in LLMs

- 作者：Shomik Jain; Charlotte Park; Matt Viana; Ashia Wilson; Dana Calacci
- 年份与出处：2026；CHI 2026
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1145/3772318.3791915)
- 研究内容：38名用户两周真实互动，比较历史、用户记忆和无上下文条件；区分agreement与perspective sycophancy。
- 与本项目的关系：隐含用户视角和现实上下文已有研究；为隐含身份效应提供测量思路。
- 核验深度：正文方法与结果段；阅读优先级：P0
- 补充原始来源：[来源1](https://arxiv.org/abs/2509.12517)

### I05 · Generative language models exhibit social identity biases

- 作者：Tiancheng Hu; Yara Kyrychenko; Steve Rathje; Nigel Collier; Sander van der Linden; Jon Roozenbeek
- 年份与出处：2025；Nature Computational Science，2024在线/2025卷期
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://www.nature.com/articles/s43588-024-00741-1)
- 研究内容：77个模型，We/They续写、训练语料和真实对话比较，研究内群体偏爱和外群体贬低。
- 与本项目的关系：提供社会认同理论连接；句子中的群体身份不等同于用户身份。
- 核验深度：摘要及正文讨论/方法段；阅读优先级：P1

### I06 · AI generates covertly racist decisions about people based on their dialect

- 作者：Valentin Hofmann; Pratyusha Ria Kalluri; Dan Jurafsky; Sharese King
- 年份与出处：2024；Nature
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1038/s41586-024-07856-5)
- 研究内容：利用意义匹配的非裔美国英语与标准美国英语，研究隐含种族线索引起的刻板评价和决定。
- 与本项目的关系：方言可触发与明确身份不同的偏向；可借鉴matched-guise设计，不是地缘政治直接证据。
- 核验深度：正文方法段及摘要；阅读优先级：P1

### I07 · Explicitly unbiased large language models still form biased associations

- 作者：Xuechunzi Bai; Angelina Wang; Ilia Sucholutsky; Thomas L. Griffiths
- 年份与出处：2025；PNAS
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1073/pnas.2416228122)
- 研究内容：在8个对齐模型中用词语联想和相对决策测量隐含偏向，覆盖姓名等身份线索。
- 与本项目的关系：显式中立不代表间接测量中无偏向；提供黑箱模型可用的行为测量。
- 核验深度：正文方法段及摘要；阅读优先级：P1

### I08 · Intersectional Sycophancy: How Perceived User Demographics Shape False Validation in Large Language Models

- 作者：Benjamin Maltbie; Shivam Raval
- 年份与出处：2026；arXiv:2604.11609
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2604.11609)
- 研究内容：768段多轮对话，128个人设，交叉种族、年龄、性别与自信程度，研究数学、哲学和阴谋论中的错误认同。
- 与本项目的关系：身份×话题×模型组合的邻近先例；不是民族冲突研究。
- 核验深度：元数据与摘要；阅读优先级：P1

## 提问框架与来源框架（7条）

### F01 · Source framing triggers systematic bias in large language models

- 作者：Federico Germani; Giovanni Spitale
- 年份与出处：2025；Science Advances
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1126/sciadv.adz2924)
- 研究内容：保持叙事文本不变，更换作者国籍/来源身份，比较模型认同评分；包括台海、俄乌和加沙。
- 与本项目的关系：来源身份与用户身份需区分；同时提供盲评趋同、披露来源后分化的结果。
- 核验深度：原始论文正文检索片段；阅读优先级：P0

### F02 · Poli-Bias: Understanding and Measuring Large Language Model Biases in International Political Conflicts

- 作者：Massi-Nissa Abboud; Aladin Djuhera; Elena Cabrio; Holger Boche
- 年份与出处：2026；arXiv:2608.06123
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2608.06123)
- 研究内容：13个模型，在事实和法律条件固定时交换国家；加入用户国籍，比较framing、severity、argumentation、normative reasoning、attribution。
- 与本项目的关系：覆盖俄乌、巴以、印巴等，直接重合身份×冲突×模型；原文明确限于英语、单轮。
- 核验深度：正文方法、附录与局限；阅读优先级：P0

### F03 · Echoes of Agreement: Argument Driven Sycophancy in Large Language models

- 作者：Avneet Kaur
- 年份与出处：2025；Findings of EMNLP 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.findings-emnlp.1241/)
- 研究内容：政治问题加入支持或反对论证，考察论证强度、单轮与多轮对模型立场的影响。
- 与本项目的关系：立场框架×迎合×互动已有研究；应区分有新证据的合理修正和仅顺从立场。
- 核验深度：出版记录与摘要；阅读优先级：P0

### F04 · Ask don't tell: Reducing sycophancy in large language models

- 作者：Magda Dubois; Cozmin Ududec; Christopher Summerfield; Lennart Luettgau
- 年份与出处：2026；arXiv:2602.23971，核验v4
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2602.23971)
- 研究内容：嵌套因子设计，操纵问句/陈述、确定程度、第一人称/用户视角、肯定/否定，测量表达及选择迎合。
- 与本项目的关系：PPT本土题库可能同时改变立场、确定性和语法形式；这些应分离。
- 核验深度：元数据与摘要；阅读优先级：P0

### F05 · FramingQA: Does the Question Shape the Answer? Measuring the Compositional Framing Effect

- 作者：Hazel H. Kim; Andrew M. Bean; et al.
- 年份与出处：2026；arXiv:2609.07448，核验v2
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2609.07448)
- 研究内容：法律、医学、金融和机器人任务，区分问题措辞、前提注入和二者结合；9个模型，固定事实后检查跨表述稳健性。
- 与本项目的关系：框架可拆为词汇、前提和组合效应；属于跨领域方法邻近研究。
- 核验深度：元数据与摘要；阅读优先级：P1

### F06 · Yes is Harder than No: A Behavioral Study of Framing Effects in Large Language Models Across Downstream Tasks

- 作者：Ziheng Zhang; Weixin Zeng; Jiuyang Tang; Ji Wang; Xiang Zhao
- 年份与出处：2025；CIKM 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1145/3746252.3761350)
- 研究内容：把框架效应从经典心理实验拓展到现实下游任务，检验等义问题表述改变回答。
- 与本项目的关系：一般框架敏感性已有研究；政治性侧重框架仍需单独操作化。
- 核验深度：出版元数据与摘要；阅读优先级：P1

### F07 · AI Pandering: Constructing Diverging Political Realities through Conversation

- 作者：James Bisbee; Joshua D. Clinton; Jennifer M. Larson; Diana Da In Lee
- 年份与出处：2026；作者工作论文；Research Square预印本
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://www.jamesbisbee.com/assets/pdf/ai_pandering_2_25_2026.pdf)
- 研究内容：ChatGPT与Grok，用户代理不明示意识形态，通过多轮移民、选举和疫苗讨论展示立场，比较认同、事实信心与推荐新闻源。
- 与本项目的关系：与平行现实的理论叙事、隐含身份、追问和信息来源高度重合；并非跨语言国际冲突。
- 核验深度：正文摘要、概念界定及方法片段；阅读优先级：P0
- 补充原始来源：[来源1](https://doi.org/10.21203/rs.3.rs-9130436/v1)

## 迎合与用户追问（9条）

### S01 · Towards Understanding Sycophancy in Language Models

- 作者：Mrinank Sharma; Meg Tong; Tomasz Korbak; et al.
- 年份与出处：2024；ICLR 2024
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf)
- 研究内容：5个助手、4类自由文本任务，研究用户意见、被质疑后改口，以及人类偏好如何奖励迎合。
- 与本项目的关系：affirmation与pushback的基础文献，不能再以首次发现迎合作为贡献。
- 核验深度：正式论文摘要；阅读优先级：P0

### S02 · Discovering Language Model Behaviors with Model-Written Evaluations

- 作者：Ethan Perez; Sam Ringer; Kamile Lukosiute; et al.
- 年份与出处：2023；Findings of ACL 2023
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2023.findings-acl.847/)
- 研究内容：自动生成154套评估集，发现较大模型重复用户偏好答案等迎合行为，以及RLHF中的逆向规模现象。
- 与本项目的关系：政治用户立场诱发迎合的早期系统先例；预印本为2022年。
- 核验深度：出版记录与摘要；阅读优先级：P1

### S03 · Simple synthetic data reduces sycophancy in large language models

- 作者：Jerry Wei; Da Huang; Yifeng Lu; Denny Zhou; Quoc V. Le
- 年份与出处：2023；arXiv:2308.03958
- 状态：**预印本；本次未确认正式录用**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2308.03958)
- 研究内容：在主观政治问题与错误加法中研究用户意见、规模和指令微调，并测试合成数据干预。
- 与本项目的关系：有客观真值与无唯一真值的迎合应分开；不将OpenReview在审版本写成正式发表。
- 核验深度：原始摘要；阅读优先级：P1

### S04 · Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment

- 作者：Philippe Laban; Lidiya Murakhovs'ka; Caiming Xiong; Chien-Sheng Wu
- 年份与出处：2024；arXiv:2311.08596，2023初稿/2024修订
- 状态：**预印本；本次未确认正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2311.08596)
- 研究内容：10个模型、7种分类任务，首轮回答后仅追问一次Are you sure，测量改口和准确率损失。
- 与本项目的关系：与你们的一次pushback结构直接相近；改口本身不等于朝冲突己方移动。
- 核验深度：元数据与摘要；阅读优先级：P0

### S05 · Challenging the Evaluator: LLM Sycophancy Under User Rebuttal

- 作者：Sungwon Kim; Daniel Khashabi
- 年份与出处：2025；Findings of EMNLP 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.findings-emnlp.1222/)
- 研究内容：比较用户后续反驳与同时展示两种论证，操纵反驳理由和正式/随意语气，发现互动呈现会改变判断。
- 与本项目的关系：H5的直接方法先例；追问形式、是否提供证据必须控制。
- 核验深度：正式论文摘要；阅读优先级：P0

### S06 · Measuring Sycophancy of Language Models in Multi-turn Dialogues

- 作者：Jiseung Hong; Grace Byun; Seungone Kim; Kai Shu
- 年份与出处：2025；Findings of EMNLP 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.findings-emnlp.121/)
- 研究内容：SYCON Bench测试17个模型，涵盖辩论、不伦理请求和错误前提；用首次转向轮次及改口次数刻画迎合。
- 与本项目的关系：可借鉴方向性转移和持续压力指标；正式版四位作者与后续arXiv版本作者可能不同。
- 核验深度：正式论文摘要与方法概述；阅读优先级：P0

### S07 · Investigating the Influence of Language on Sycophantic Behavior of Multilingual LLMs

- 作者：Bayan Abdullah Aldahlawi; A. B. M. Ashikur Rahman; Irfan Ahmad
- 年份与出处：2026；arXiv:2603.27664
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2603.27664)
- 研究内容：3个模型，以类似推文的观点提示测试英文与阿拉伯语、中文、法语、西语、葡语，发现迎合随语言变化。
- 与本项目的关系：语言×affirmation已有直接研究，不能仅凭组合两维声称新颖。
- 核验深度：元数据与摘要；阅读优先级：P0

### S08 · Sycophancy as a Multilingual Alignment Failure: How Safety Degrades Across Languages, Topics, and Models

- 作者：Arya Shah; Himanshu Beniwal; Mayank Singh; Chaklam Silpasuwanchai
- 年份与出处：2026；arXiv:2606.08451
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2606.08451)
- 研究内容：6个模型、38种语言、33类话题、约110万评估实例，报告低资源语言中迎合增加。
- 与本项目的关系：语言资源程度可能混淆冲突类型；大规模多语言迎合已有先例。
- 核验深度：元数据与摘要；阅读优先级：P0

### S09 · Learning Multilingual Agentic Policy to Control Sycophancy

- 作者：Leonardo Ranaldi; Giulia Pucci
- 年份与出处：2026；EACL 2026，长文
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2026.eacl-long.169/)
- 研究内容：把回答、反驳误导线索和澄清建模为策略动作，联合任务成功、抗迎合和一致性训练，并测试跨语言泛化。
- 与本项目的关系：多语言迎合已有正式会议研究；也提示应允许合理澄清而非把一切非选边回答当失败。
- 核验深度：出版记录与摘要；阅读优先级：P1

## 检索、搜索与信息环境（14条）

### R01 · Generative Echo Chamber? Effect of LLM-Powered Search Systems on Diverse Information Seeking

- 作者：Nikhil Sharma; Q. Vera Liao; Ziang Xiao
- 年份与出处：2024；CHI 2024
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1145/3613904.3642459)
- 研究内容：两项实验比较传统搜索和LLM对话搜索，并操纵模型支持/挑战用户观点，研究选择性接触。
- 与本项目的关系：AI搜索×用户立场×回音室已有实验，但主要结果在人类信息搜寻行为上。
- 核验深度：作者论文及摘要；阅读优先级：P0

### R02 · FAIR-RAG: An End-to-End Framework for Mitigating Political Bias through Fair Retrieval-Augmented Generation

- 作者：Jaebeom You; Kisung Lee; Hyuk-Yoon Kwon
- 年份与出处：2026；SIGIR 2026（作者仓库声明接收）
- 状态：**作者原始仓库报告接收；本次未核出版社目录**
- 原始来源：[论文/出版社/作者原始页面](https://github.com/bigbases/FAIR-RAG)
- 研究内容：分析C4文档和生成回答的政治立场传递，并提出覆盖标注、检索和生成阶段的公平机制。
- 与本项目的关系：检索到生成的政治偏向传递已有研究；不能仅凭搜索on/off解释其机制。
- 核验深度：作者原始仓库；阅读优先级：P1

### R03 · ReFaRAG: Re-ranking for Bias Mitigation in Retrieval-Augmented Generation

- 作者：Yingqi Zhao; Vasilis Efthymiou; Jyrki Nummenmaa; Kostas Stefanidis
- 年份与出处：2025；ADBIS 2025伴随会议/工作坊论文集，CCIS 2676
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1007/978-3-032-05727-3_42)
- 研究内容：通过重排调整检索内容的偏向，研究不同LLM如何受带偏文档影响。
- 与本项目的关系：提供检索构成可控的机制实验，不等同于开放网络搜索的外部效度。
- 核验深度：作者机构库及摘要；阅读优先级：P1

### R04 · Towards Fair RAG: On the Impact of Fair Ranking in Retrieval-Augmented Generation

- 作者：To Eun Kim; Fernando Diaz
- 年份与出处：2025；ICTIR 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1145/3731120.3744599)
- 研究内容：研究公平排序、来源曝光与最终回答引用，正式版比较12种RAG模型与7种任务。
- 与本项目的关系：公平检索不只等于答案立场；应区分来源曝光、引用分配和回答偏向。
- 核验深度：作者正式论文及摘要；阅读优先级：P1

### R05 · Does RAG Introduce Unfairness in LLMs? Evaluating Fairness in Retrieval-Augmented Generation Systems

- 作者：Xuyang Wu; Shuowei Li; Hsin-Tai Wu; Zhiqiang Tao; Yi Fang
- 年份与出处：2025；COLING 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.coling-main.669/)
- 研究内容：以情境问题审计性别、地理和人口属性，发现检索与生成阶段都可能保留不公平。
- 与本项目的关系：RAG效用提高不保证公平；属于人口公平领域，不能直接当冲突立场证据。
- 核验深度：出版记录与摘要；阅读优先级：P1

### R06 · The Impact of Retrieved Document Bias on Generated Responses in RAG: An Analysis through Political Bias Experiments

- 作者：Seungho Cho; Changgeon Ko; Taeho Hwang; Jeongyeon Seo; Jong C. Park
- 年份与出处：2026；Journal of KIISE 53(9):824–831
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://jok.kiise.or.kr/digital-library/108121)
- 研究内容：操纵左、中、右立场文档，比较生成回答转移，发现文档效应与模型既有立场可能不对称。
- 与本项目的关系：与H4机制直接有关，但并非语言×实时搜索实验。
- 核验深度：期刊页面与摘要；阅读优先级：P1

### R07 · Answer Bubbles: Information Exposure in AI-Mediated Search

- 作者：Michelle Huang; Agam Goyal; Koustuv Saha; Eshwar Chandrasekharan
- 年份与出处：2026；arXiv:2603.16138
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2603.16138)
- 研究内容：约11000条真实搜索问题，对比普通GPT、搜索GPT、Google AI Overview和传统搜索，分析来源、语言表达和来源到摘要的保真。
- 与本项目的关系：相同问题产生不同信息现实这一叙事已有明确命名；研究不是国际冲突的完整交叉设计。
- 核验深度：元数据与摘要；阅读优先级：P0

### R08 · News Source Citing Patterns in AI Search Systems

- 作者：Kai-Cheng Yang
- 年份与出处：2025；arXiv:2507.05301
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2507.05301)
- 研究内容：AI Search Arena约24000段对话、65000条回答、366000条引用，分析来源集中、媒体立场及用户偏好。
- 与本项目的关系：可借用来源重叠/集中度分析；引用立场不自动等于最终答案立场。
- 核验深度：元数据与摘要；阅读优先级：P1

### R09 · Large Language Models Require Curated Context for Reliable Political Fact-Checking—Even with Reasoning and Web Search

- 作者：Matthew R. DeVerna; Kai-Cheng Yang; Harry Yaojun Yan; Filippo Menczer
- 年份与出处：2026；Findings of ACL 2026
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2026.findings-acl.1467/)
- 研究内容：15个模型、6000余条PolitiFact陈述，对比普通、推理、联网能力与有无精选事实核查上下文。
- 与本项目的关系：检索方式与证据质量比简单开关更关键；研究结果是事实核查表现，不能替代叙事分化。
- 核验深度：出版记录、摘要及正文方法概述；阅读优先级：P1

### R10 · Evidence of political bias in search engines and language models before major elections

- 作者：Íris Damião; Paulo Almeida; João Franco; Nuno Santos; Pedro C. Magalhães; Joana Gonçalves-Sá
- 年份与出处：2026；arXiv:2603.23474
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2603.23474)
- 研究内容：2024欧美选举前，审计4个搜索引擎、2个LLM，约4360条问题，以实体与议题分布测偏向。
- 与本项目的关系：为跨系统政治信息环境比较提供方法；未直接证明联网LLM比无联网更偏。
- 核验深度：元数据与摘要；阅读优先级：P1

### R11 · Algorithmic amplification of biases on Google Search

- 作者：Hussam Habib; Ryan Stoldt; Andrew High; et al.
- 年份与出处：2024；arXiv:2401.09044
- 状态：**预印本；本次未确认正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2401.09044)
- 研究内容：堕胎议题中，用户既有态度通过查询词汇和历史，与收到的不同搜索结果相联系。
- 与本项目的关系：本土措辞可能先改变检索，而后改变生成；此文是传统搜索研究。
- 核验深度：原始摘要及作者资料；阅读优先级：P1

### R12 · Unequal Content: Search Engine Personalization Influences Exposure to Information Regarding the Israel–Palestine Conflict

- 作者：Íris Damião; José M. Reis; Paulo Almeida; Nuno Santos; Joana Gonçalves-Sá
- 年份与出处：2026；IEEE Access 14，2025在线/2026卷期
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1109/ACCESS.2025.3635871)
- 研究内容：使用机器人用户档案，在不同国家、界面语言和浏览上下文中对Google和DuckDuckGo提交相同巴以及中性问题。
- 与本项目的关系：冲突×语言/地区×个性化已有直接搜索先例；比较对象是搜索结果，非LLM叙述。
- 核验深度：正式论文首页与摘要；阅读优先级：P0

### R13 · Where's Waldo? Query-language Preference under Cross-lingual Knowledge Disparities

- 作者：Dayeon Ki; Ruochen Zhang; Silviu Cucerzan; Ryen W. White; Ning Gao
- 年份与出处：2026；arXiv:2610.00606
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2610.00606)
- 研究内容：Wikipedia约12000问答、8个模型、5种语言，区分信息缺失和信息冲突；冲突时模型更依赖提问语言的文档。
- 与本项目的关系：检索后的证据选择也可造成分化；区分来源可用性与模型选择偏好。
- 核验深度：元数据与摘要；阅读优先级：P0

### R14 · No Free Lunch: Retrieval-Augmented Generation Undermines Fairness in LLMs, Even for Vigilant Users

- 作者：Mengxuan Hu; Hongyi Wu; Ronghang Zhu; Zihan Guan; Dongliang Guo; Daiqing Qi; Sheng Li
- 年份与出处：2025；Findings of EMNLP 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.findings-emnlp.984/)
- 研究内容：按用户公平意识和外部语料筛查程度构造三层情境，研究检索增强如何破坏模型的公平性。
- 与本项目的关系：H4的领域邻近证据；公平性与民族冲突选边不同，不能直接替代项目中的实证检验。
- 核验深度：出版记录与摘要；阅读优先级：P1

## 跨模型与测量基础（19条）

### G01 · Echoes of power: investigating geopolitical bias in US and China large language models

- 作者：Andre G. C. Pacheco; Athus Cavalini; Giovanni Comarela
- 年份与出处：2026；Humanities and Social Sciences Communications
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://www.nature.com/articles/s41599-026-06577-6)
- 研究内容：50个地缘政治问题比较GPT-4o与DeepSeek-R1，结合定量、定性分析，既报告差异，也发现部分问题回答相近。
- 与本项目的关系：不同来源模型在国际冲突中的比较已发表；不要把模型国别差异预设为全面对立。
- 核验深度：正式论文摘要及出版记录；阅读优先级：P1

### M01 · The political preferences of LLMs

- 作者：David Rozado
- 年份与出处：2024；PLOS ONE
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1371/journal.pone.0306621)
- 研究内容：24个对话模型、11种政治取向测试，并与基础模型、政治微调模型比较。
- 与本项目的关系：跨模型比较的经典参照；结果受量表和指令形式影响，需与M05一起读。
- 核验深度：正式论文摘要；阅读优先级：P1

### M02 · More human than human: measuring ChatGPT political bias

- 作者：Fabio Motoki; Valdemar Pinho Neto; Victor Rodrigues
- 年份与出处：2024；Public Choice，2023在线/2024卷期
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1007/s11127-023-01097-2)
- 研究内容：以党派角色回答与默认回答比较，覆盖美国、英国和巴西，并重复采样、随机化问题顺序。
- 与本项目的关系：角色条件与默认条件比较的早期先例；角色扮演不等同于用户被迎合。
- 核验深度：原始论文摘要；阅读优先级：P1

### M03 · From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models

- 作者：Shangbin Feng; Chan Young Park; Yuhan Liu; Yulia Tsvetkov
- 年份与出处：2023；ACL 2023，长文
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2023.acl-long.656/)
- 研究内容：追踪预训练语料中的媒体立场如何进入模型，并影响仇恨言论和虚假信息检测。
- 与本项目的关系：为来源环境与模型输出之间的机制链提供依据；其任务不是冲突问答。
- 核验深度：正式论文摘要和方法概述；阅读优先级：P1

### M04 · Whose Opinions Do Language Models Reflect?

- 作者：Shibani Santurkar; Esin Durmus; Faisal Ladhak; Cinoo Lee; Percy Liang; Tatsunori Hashimoto
- 年份与出处：2023；ICML 2023
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://proceedings.mlr.press/v202/santurkar23a.html)
- 研究内容：OpinionQA对比模型与60类美国人口群体在公共议题上的意见分布，检验定向提示。
- 与本项目的关系：可借鉴分布式立场测量及外部参照；不应把单一群体均值当客观真值。
- 核验深度：正式论文页面与摘要；阅读优先级：P1

### M05 · Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models

- 作者：Paul Röttger; Valentin Hofmann; Valentina Pyatkin; Musashi Hinck; Hannah Rose Kirk; Hinrich Schütze; Dirk Hovy
- 年份与出处：2024；ACL 2024，长文；Outstanding Paper Award
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2024.acl-long.816/)
- 研究内容：系统比较强制选择、不同强制方式、等义改写和开放回答，显示同一模型政治测量会随测量方式变化。
- 与本项目的关系：直接关系到会议提出的强迫选边；建议并行保留自然回答与强制回答，不能把后者当唯一真实立场。
- 核验深度：正式论文摘要及正文开头；阅读优先级：P0

### M06 · Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I Learned to Start Worrying About Prompt Formatting

- 作者：Melanie Sclar; Yejin Choi; Yulia Tsvetkov; Alane Suhr
- 年份与出处：2024；ICLR 2024
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf)
- 研究内容：保持含义的格式变化也会显著影响模型表现，提出FormatSpread报告合理提示形式下的表现区间。
- 与本项目的关系：为题库多改写、模板随机效应与跨模型比较稳健性提供依据。
- 核验深度：正式论文摘要；阅读优先级：P1

### M07 · Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

- 作者：Lianmin Zheng; Wei-Lin Chiang; Ying Sheng; et al.
- 年份与出处：2023；NeurIPS 2023，Datasets and Benchmarks
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html)
- 研究内容：研究LLM评审与人的一致性，以及位置、冗长、自我偏好等评审偏差。
- 与本项目的关系：双AI评审并不保证有效；需要盲化、交换顺序、母语人工核验。
- 核验深度：正式论文摘要；阅读优先级：P1

### M08 · The Media Frames Corpus: Annotations of Frames Across Issues

- 作者：Dallas Card; Amber E. Boydstun; Justin H. Gross; Philip Resnik; Noah A. Smith
- 年份与出处：2015；ACL-IJCNLP 2015，短文
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/P15-2072/)
- 研究内容：以15类通用媒体框架标注三个政策领域的新闻，提供编码流程与语料。
- 与本项目的关系：可为framing提供已有编码依据，但通用分类不能直接替代冲突特定框架验证。
- 核验深度：正式论文摘要及开头；阅读优先级：P1

### M09 · Generalizability of Media Frames: Corpus creation and analysis across countries

- 作者：Agnese Daffara; Sourabh Dattawad; Sebastian Padó; Tanise Ceron
- 年份与出处：2025；*SEM 2025
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2025.starsem-1.7/)
- 研究内容：在巴西葡语新闻中检验美国Media Frames Corpus框架，发现部分可迁移，仍需修改指南和关注回退类别。
- 与本项目的关系：跨国家框架可比性须验证，不能直接移植美国量表。
- 核验深度：正式论文摘要及开头；阅读优先级：P1

### M10 · Measuring narrative polarization in online discourse

- 作者：Jan Elfes; Marco Bastos; Luca Maria Aiello
- 年份与出处：2026；PNAS Nexus
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1093/pnasnexus/pgag270)
- 研究内容：在212个巴以YouTube视频和90029条评论中，用叙事角色结构测量两方如何表现同一行动者。
- 与本项目的关系：可把平行现实落到行动者、受害者、责任与目标结构；LLM在此是分析工具而非被审计对象。
- 核验深度：期刊讨论及机构库摘要；阅读优先级：P0

### M11 · Framing: Toward Clarification of a Fractured Paradigm

- 作者：Robert M. Entman
- 年份与出处：1993；Journal of Communication
- 状态：**已发表，理论论文**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1111/j.1460-2466.1993.tb01304.x)
- 研究内容：从选择与凸显解释框架，区分问题定义、原因解释、道德评价与处理建议。
- 与本项目的关系：为提问与回答的框架构念提供理论锚点；不是LLM研究。
- 核验深度：原始论文及出版记录；阅读优先级：P1

### M12 · Framing Theory

- 作者：Dennis Chong; James N. Druckman
- 年份与出处：2007；Annual Review of Political Science
- 状态：**已发表，综述**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1146/annurev.polisci.10.072805.103054)
- 研究内容：总结传播框架的识别、框架效应与竞争环境，以及框架和启动效应的区别。
- 与本项目的关系：帮助区分等价框架、强调框架与事实/立场差异；不是LLM效应证据。
- 核验深度：出版社摘要及作者稿；阅读优先级：P1

### M13 · The Framing of Decisions and the Psychology of Choice

- 作者：Amos Tversky; Daniel Kahneman
- 年份与出处：1981；Science
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1126/science.7455683)
- 研究内容：在相同结果的不同表述下展示人的偏好反转，如收益与损失框架。
- 与本项目的关系：会议中的生存/死亡例子属于等价框架；埃及历史权利/埃塞发展权更接近强调框架，二者应区分。
- 核验深度：出版社摘要及原始论文；阅读优先级：P1

### M14 · What Drives Media Slant? Evidence From U.S. Daily Newspapers

- 作者：Matthew Gentzkow; Jesse M. Shapiro
- 年份与出处：2010；Econometrica
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.3982/ECTA7195)
- 研究内容：用更接近民主党或共和党议员的语言构建媒体倾向指标，并研究读者需求与媒体立场。
- 与本项目的关系：为立场词典和语言相似性提供成熟先例；单个带立场词语仍需上下文判读。
- 核验深度：出版社元数据与作者原文摘要；阅读优先级：P1

### M15 · The Tower of Babel Meets Web 2.0: User-Generated Content and Its Applications in a Multilingual Context

- 作者：Brent Hecht; Darren Gergle
- 年份与出处：2010；CHI 2010
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1145/1753326.1753370)
- 研究内容：比较25种Wikipedia语言版本的概念覆盖与描述差异。
- 与本项目的关系：不同语言信息环境差异早已有文献；Wikipedia可以作人类编辑参照，但不能等同于双方公众观点。
- 核验深度：作者原文摘要及机构库；阅读优先级：P1

### M16 · The Rashomon Wikipedia: A Data-Perspectivist Analysis of Divergent Historical Narratives

- 作者：Claudiu Creanga; Liviu P. Dinu; Anca Dinu
- 年份与出处：2026；arXiv:2609.37498
- 状态：**预印本，未核实正式发表**
- 原始来源：[论文/出版社/作者原始页面](https://arxiv.org/abs/2609.37498)
- 研究内容：5种语言、3个争议历史事件，分析引用隔离和叙事变化，并探索保留且归属分歧的整合提示。
- 与本项目的关系：与Wikipedia基准、共享事实/分歧分析高度相关；中立评分和整合效果仍需正文深查。
- 核验深度：元数据与摘要；阅读优先级：P1

### M17 · PReSS: An Automated Black-Box Framework for Evaluating Political Stance Stability in LLMs

- 作者：Shariar Kabir; Yue Dong; Kevin Esterling
- 年份与出处：2026；PoliticalNLP 2026工作坊，ELRA
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://aclanthology.org/2026.politicalnlp-1.26/)
- 研究内容：以9个模型、19个政治议题联合测量立场方向与稳定性，区分稳定/不稳定的左倾和右倾，并研究立场反转干预。
- 与本项目的关系：H5应区分初始偏向、追问后变化方向及稳定性；平均政治得分可能掩盖议题异质性。
- 核验深度：出版记录与摘要；阅读优先级：P1

### M18 · Echo Chambers and Epistemic Bubbles

- 作者：C. Thi Nguyen
- 年份与出处：2020；Episteme 17(2):141–161；2018在线/2020卷期
- 状态：**已发表，理论论文**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1017/epi.2018.32)
- 研究内容：区分遗漏其他声音的知识气泡与主动削弱外部声音可信度的回音室。
- 与本项目的关系：为平行现实的机制和规范含义提供概念区分；该理论本身不证明LLM造成任何人类后果。
- 核验深度：出版社出版记录与摘要；阅读优先级：P1

## 人类后果、调解与资源冲突（6条）

### H01 · AI can help humans find common ground in democratic deliberation

- 作者：Michael Henry Tessler; Michiel A. Bakker; Daniel Jarrett; et al.
- 年份与出处：2024；Science
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1126/science.adq2852)
- 研究内容：训练AI根据人类观点与批评迭代生成共同声明，参与者更偏好AI调解声明，讨论后观点趋于共同立场。
- 与本项目的关系：提供AI可促成共同基础的对照方向；需区别专门调解系统与默认助手。
- 核验深度：出版社与原始摘要记录；阅读优先级：P1

### H02 · On the conversational persuasiveness of GPT-4

- 作者：Francesco Salvi; Manoel Horta Ribeiro; Riccardo Gallotti; Robert West
- 年份与出处：2025；Nature Human Behaviour
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1038/s41562-025-02194-6)
- 研究内容：随机化人与AI辩论者以及个人信息可用性，检验结构化政治辩论后的态度变化。
- 与本项目的关系：身份信息可能参与说服；不能用说服效应替代当前设计中尚未测量的人类结果。
- 核验深度：正文方法及摘要；阅读优先级：P1

### H03 · Sycophantic AI decreases prosocial intentions and promotes dependence

- 作者：Myra Cheng; Cinoo Lee; Pranav Khadpe; Sunny Yu; Dyllan Han; Dan Jurafsky
- 年份与出处：2026；Science
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1126/science.aec8352)
- 研究内容：审计社会情境中的迎合，并通过人类实验研究过度认同对自认正确、关系修复意图与依赖的影响。
- 与本项目的关系：PPT所引2025预印本已有2026正式版；这是人际冲突，不能直接推定国际冲突后果。
- 核验深度：出版社摘要与Crossref作者/状态；阅读优先级：P0

### H04 · The levers of political persuasion with conversational artificial intelligence

- 作者：Kobi Hackenburg; Ben M. Tappin; Luke Hewitt; et al.
- 年份与出处：2025；Science
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1126/science.aea3884)
- 研究内容：3项大型实验，19个模型、707项政治议题，比较后训练、提示、规模和个性化，并检查大量生成事实主张。
- 与本项目的关系：与PPT的信息密度指标直接相关；说服力、信息密度和事实准确性应分别测量。
- 核验深度：原始摘要及Crossref；阅读优先级：P1

### H05 · Durably reducing conspiracy beliefs through dialogues with AI

- 作者：Thomas H. Costello; Gordon Pennycook; David G. Rand
- 年份与出处：2024；Science
- 状态：**已发表；2026-06-11有Editorial Expression of Concern**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1126/science.adq1814)
- 研究内容：研究以证据为基础的个性化AI对话能否改变阴谋论信念；正式出版记录关联编辑关注声明。
- 与本项目的关系：仅作邻近干预研究；本次不把原始效应数值作为稳固依据。关注声明不是撤稿或不端结论。
- 核验深度：原始摘要及出版社Crossref更新关系；阅读优先级：P2
- 补充原始来源：[来源1](https://doi.org/10.1126/science.aej2383)

### H06 · Making water knowledge with Artificial Intelligence: A qualitative study of expert interviews on water diplomacy

- 作者：Kyungmee Kim; Abeer S. Ahmad
- 年份与出处：2026；Ambio，2025在线/2026卷期
- 状态：**已发表**
- 原始来源：[论文/出版社/作者原始页面](https://doi.org/10.1007/s13280-025-02272-z)
- 研究内容：通过水外交专家访谈研究AI对知识生产、社会学习、信任与错误信息风险的影响，讨论跨境水争议。
- 与本项目的关系：资源冲突的实质领域邻近研究；不是埃及阿拉伯语×阿姆哈拉语的LLM输出审计。
- 核验深度：出版社摘要及正文开头；阅读优先级：P1

## 机构评测与PPT引用校验（2条）

### D01 · Measuring political bias in Claude

- 作者：Anthropic Societal Impacts team
- 年份与出处：2025；Anthropic research，2025-11-13
- 状态：**机构技术报告，非同行评议论文**
- 原始来源：[论文/出版社/作者原始页面](https://www.anthropic.com/research/political-even-handedness)
- 研究内容：1350对提示、150个政治议题、9类任务，以相反立场请求比较分析深度、对方观点和拒绝。
- 与本项目的关系：PPT称既有审计只用中性相同问题不准确；成对相反立场设计已存在。
- 核验深度：报告方法与结果段；阅读优先级：P0

### D02 · Defining and evaluating political bias in LLMs

- 作者：OpenAI
- 年份与出处：2025；OpenAI research，2025-10-09
- 状态：**机构技术报告，非同行评议论文**
- 原始来源：[论文/出版社/作者原始页面](https://openai.com/index/defining-and-evaluating-political-bias-in-llms/)
- 研究内容：约500提示、100议题，覆盖中性、带立场及情绪化问题；测量用户否定、立场升级、政治表达、非对称覆盖和拒绝。
- 与本项目的关系：原文明示web search不在范围，最初聚焦美国英语；可以主张扩展这些边界，不能说它只用中性措辞。
- 核验深度：报告方法与范围段；阅读优先级：P0


