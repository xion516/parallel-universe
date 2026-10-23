# Parallel Universe：文献版图与创新性初筛

检索截止：2026-10-22。依据项目PPT中的H1—H5，以及镜像提问、本土提问、跨模型和一次追问的设计整理。

后续专题：[Framing正文核查与研究判断](<D:/PhD_Research/Parallel Universe/Literature_Review/2026-10-22/framing_deep_dive/README.md>)进一步比较14项研究的问题、测量、结果与主张，并补入4项本轮广泛目录未收录的直接近邻。

## 先给结论

**这个研究仍值得推进，但五个维度的主效应都已有先例，其中若干组合也已被研究。** 目前不能把“同一模型随语言改变政治立场”“身份诱发迎合”“联网影响偏向”或“一次反驳导致改口”单独作为主要创新。与项目最接近的不只是通用AI偏见论文，而是多语言领土争议、身份条件下的政治迎合、跨语言政治框架和对话中形成不同政治现实的研究。

本轮收录**80条记录**：58条已发表学术论文/理论/综述、19条尚未确认正式发表的预印本或工作论文、1条仅作者仓库报告接收、2份机构评测。部分记录是邻近领域或测量基础，不能把总数解释为80项直接竞争研究。所有条目都有原始来源链接和核验深度；没有把摘要阅读写成全文精读，也没有将检索未命中写成不存在。

完整条目见 [80条文献目录](<D:/PhD_Research/Parallel Universe/Literature_Review/2026-10-22/literature_catalog.md>)；机器可读字段见 [JSON目录](<D:/PhD_Research/Parallel Universe/Literature_Review/2026-10-22/literature_catalog.json>)；边界和可复跑检索式见 [检索说明](<D:/PhD_Research/Parallel Universe/Literature_Review/2026-10-22/search_scope.md>)。

## 1. 五个设计维度：已有研究到哪一步

| 项目维度 | 代表先例 | 已覆盖的内容 | 对本项目的含义 |
|---|---|---|---|
| H1：提问语言与冲突方立场 | Li等，NAACL 2024；Zhou与Zhang，Scientific Reports 2024；Chupilkin，2026预印本 | 领土争议多语言回答、中美双语政治不一致、112种语言的俄乌叙述 | 跨语言分化已有直接先例；不能仅靠换语言或加模型建立创新。[L01](https://aclanthology.org/2024.naacl-long.213/) [L03](https://www.nature.com/articles/s41598-024-76395-w) [L06](https://arxiv.org/abs/2609.20005) |
| H2：用户明确/隐含身份，超出语言效应 | Törnberg与Schimmel，2026预印本；Soares等，Scientific Reports 2026；Jain等，CHI 2026 | 用户政治身份、模型推断的审计者身份、真实互动上下文与迎合 | 需要区分用户身份、模型角色、材料作者身份；设计语言与身份不一致的条件，才更有助于拆解机制。[I01](https://arxiv.org/abs/2604.27633) [I02](https://www.nature.com/articles/s41598-026-52105-6) [I04](https://doi.org/10.1145/3772318.3791915) |
| H3：本土立场框架及词汇进入回答 | Germani与Spitale，Science Advances 2025；Awwad等，PoliticalNLP 2026；Papaioannou，AI and Ethics 2026 | 材料来源身份改变评价；英阿语移民框架漂移；希腊语/英语历史责任叙事差异 | 需把立场词、事实前提、来源标签和问题语法分开；“框架”不能包揽所有提示变化。[F01](https://doi.org/10.1126/sciadv.adz2924) [L15](https://aclanthology.org/2026.politicalnlp-1.23/) [L14](https://link.springer.com/article/10.1007/s43681-026-01138-8) |
| H4：联网检索是否扩大分化 | Li等，Findings ACL 2025的BordIRLines；Sharma等，CHI 2024；Cho等，Journal of KIISE 2026 | 语言×领土争议×检索、AI搜索回音室、检索文档偏向到生成回答的传递 | 有直接组合先例，而且多语言检索也可能降低分化；应把放大与缓解作为可竞争结果。[L02](https://aclanthology.org/2025.findings-acl.219/) [R01](https://doi.org/10.1145/3613904.3642459) [R06](https://jok.kiise.or.kr/digital-library/108121) |
| H5：一次反驳是否向用户一方移动 | Kim与Khashabi，Findings EMNLP 2025；Hong等，Findings EMNLP 2025；Aldahlawi等，2026预印本 | 用户反驳、对话中的立场转移、多语言迎合 | 一次追问本身不新；需测量向哪一方移动、是否牺牲事实，以及追问是否增加新证据。[S05](https://aclanthology.org/2025.findings-emnlp.1222/) [S06](https://aclanthology.org/2025.findings-emnlp.121/) [S07](https://arxiv.org/abs/2603.27664) |

**不能把“有先例”等同于“结果必然重复”。** Weeber等在五种西方语言中发现的政治意见差异有限；GlobalOpinionQA也不支持“把问题翻成某语言就必然更接近该语言群体意见”的简单推断。这些趋同或不符合预期的结果应进入文献综述和预注册。[L10](https://aclanthology.org/2026.eacl-long.14/) [L13](https://openreview.net/forum?id=zl16jLb91v)

## 2. 最接近的研究，需要逐项比对

下表的“未涉及/未见”只按本轮核验范围判断；摘要未提到某维度，不构成该研究完全没有该设计的证据。

| 工作 | 领域/状态 | 已核实的交集 | 尚需与本项目区别的部分 |
|---|---|---|---|
| Li、Haider、Callison-Burch，BorderLines（2024） | NLP；NAACL正式论文 | 251个领土争议、49种语言、模型立场与角色提示 | 主要是领土归属任务；民族主义者/维和者是模型扮演的角色，不是用户自报身份。[L01](https://aclanthology.org/2024.naacl-long.213/) |
| Li等，BordIRLines（2025） | 跨语言信息检索；Findings ACL | 同一领土争议在不同提问/检索语言条件下的稳健性与偏向 | Wikipedia文档检索与真实产品开放网页搜索不同；但“语言×联网×冲突”的概念不能再声称没有先例。[L02](https://aclanthology.org/2025.findings-acl.219/) |
| Helwe、Balalau、Ceolin（2025） | 多语言政治评测；Findings ACL | 15个模型、50种国家身份、语言与政治量表 | 身份赋予模型；不等于“用户是某国人”。[L04](https://aclanthology.org/2025.findings-acl.883/) |
| Germani、Spitale（2025） | 科学传播/AI偏向；Science Advances | 相同材料、来源国籍披露或错误归属、涉台/俄乌/加沙等争议材料 | 操纵材料作者的身份；不是用户身份，也不是输入语言效应。[F01](https://doi.org/10.1126/sciadv.adz2924) |
| Abboud等，Poli-Bias（2026） | 国际政治冲突审计；预印本 | 13个模型、冲突方置换、用户国籍条件、多维偏向指标 | 正文明确限于英语、单轮；这些是可核实的边界，而非猜测其未做的内容。[F02](https://arxiv.org/abs/2608.06123) |
| Bisbee、Clinton、Larson、Lee，AI Pandering（2026） | 政治学；工作论文/预印本 | 不直接贴党派标签的用户画像、对话、事实确信、来源推荐与分化的政治现实 | 理论叙事高度接近；本轮方法片段未显示跨语言国际冲突的系统比较。[F07](https://www.jamesbisbee.com/assets/pdf/ai_pandering_2_25_2026.pdf) |
| Chupilkin（2026） | 多语言地缘政治；预印本 | 112种语言、俄乌战争20条陈述、3个模型 | 规模与俄乌场景均已覆盖；需比较叙事结构与交互条件是否带来新解释。[L06](https://arxiv.org/abs/2609.20005) |
| Smirnov（2026） | 政治话语分析；预印本v6 | 同一乌克兰公民社会材料，在俄语/乌语提问下出现不同意识形态解读 | 接近“事实材料相同、叙事不同”；须精读其编码规则后再主张测量创新。[L07](https://arxiv.org/abs/2601.12164) |
| Soares等（2026） | 计算社会科学；Scientific Reports | 巴西政治、用户左/右身份、成对陈述、21个模型 | 用户身份的政治迎合已发表；国际冲突和语言的交互是可能扩展，而非身份主效应的首次发现。[I02](https://www.nature.com/articles/s41598-026-52105-6) |
| Jain等（2026） | 人机交互；CHI | 真实交互上下文、记忆、推断用户政治立场与视角迎合 | 需要区别明确立场陈述与间接身份线索。[I04](https://doi.org/10.1145/3772318.3791915) |
| Awwad等（2026） | 政治NLP；工作坊正式论文 | 英语/阿拉伯语、移民、框架漂移、词汇/统计/定性三类分析 | 不是双方国际冲突；但“多语言+框架+混合测量”已有先例。[L15](https://aclanthology.org/2026.politicalnlp-1.23/) |
| Huang等，Answer Bubbles（2026） | 搜索/信息接触；预印本 | 同题跨AI搜索与传统搜索、来源、摘要表达及保真差异 | 结果层面的不同信息环境已有直接命名；本项目需交代“parallel universes”的额外定义。[R07](https://arxiv.org/abs/2603.16138) |

## 3. 已发表在哪些领域，哪些作者群值得持续跟踪

| 领域 | 代表作者/研究线 | 主要出处 | 与项目的关系 |
|---|---|---|---|
| 自然语言处理与跨语言政治偏向 | Bryan Li、Samar Haider、Chris Callison-Burch；Chadi Helwe、Oana Balalau、Davide Ceolin；Franziska Weeber、Tanise Ceron、Sebastian Padó | NAACL、ACL/Findings、EACL、IJCNLP-AACL、ROCLING | 最直接的语言、身份角色、领土争议与跨语言稳健性文献。L01、L02、L04、L09—L11 |
| 文化与全球意见表征 | Esin Durmus等；Shibani Santurkar等；Yan Tao、Olga Viberg、Ryan Baker、René Kizilcec | COLM、ICML、PNAS Nexus | 区分语言、国家视角、群体意见与客观事实。L12、L13、M04 |
| 计算政治学与政治测量 | Petter Törnberg、Michelle Schimmel；James Bisbee、Joshua Clinton、Jennifer Larson、Diana Lee；David Rozado；Fabio Motoki等 | 工作论文/预印本、PLOS ONE、Public Choice；另有Scientific Reports相关线 | 政治位置、推断用户身份、政治迎合与分化现实。I01、I02、F07、M01、M02 |
| 迎合与模型对齐 | Mrinank Sharma、Meg Tong等；Ethan Perez等；Sungwon Kim、Daniel Khashabi；Jiseung Hong等 | ICLR、ACL Findings、EMNLP Findings、EACL | 反驳后的移动、迎合指标、跨语言对齐失效。S01—S09 |
| 人机交互与政治信息搜寻 | Nikhil Sharma、Q. Vera Liao、Ziang Xiao；Shomik Jain、Dana Calacci等 | CHI、AIES | 真实用户情境、视角迎合、AI搜索回音室；这些研究中的人类结果不能由本项目的模型输出直接替代。I03、I04、R01 |
| 检索与来源公平 | To Eun Kim、Fernando Diaz；Yingqi Zhao等；Xuyang Wu等；Seungho Cho等 | ICTIR、ADBIS伴随论文集、COLING、Journal of KIISE；SIGIR接收声明另列 | 来源构成、排序、文档偏向、引用与答案的关系。R02—R06、R14 |
| 传播学与框架理论 | Robert Entman；Dennis Chong、James Druckman；Dallas Card等；Jan Elfes、Marco Bastos、Luca Maria Aiello | Journal of Communication、Annual Review of Political Science、ACL、PNAS Nexus | 给框架、责任归属与叙事分化提供可检验的定义。M08—M12 |
| 心理学、说服与共同基础 | Michael Tessler等；Francesco Salvi等；Myra Cheng等；Kobi Hackenburg等 | Science、Nature Human Behaviour | 说明研究的重要性，也提供AI促进共同基础的相反方向。H01—H04 |
| 水治理与水外交 | Kyungmee Kim、Abeer S. Ahmad | Ambio | 与尼罗河资源冲突的实质领域相接；目前这条不是双方语言输出审计。H06 |

完整作者、标题、年份和原始链接均在目录中。表中相同作者线可能跨多个领域，学科归类是为本项目组织阅读而作的分析分类，不代表作者自我归属。

## 4. 哪些创新主张目前不宜使用

1. **“既有评测只用中性、完全相同的问题。”** Anthropic已经使用相反立场的成对提示；OpenAI包含带立场及情绪化表达的提示。应改成具体比较其语言、任务、案例和互动范围。[D01](https://www.anthropic.com/research/political-even-handedness) [D02](https://openai.com/index/defining-and-evaluating-political-bias-in-llms/)
2. **“首次比较跨语言政治偏向/国际冲突偏向。”** BorderLines、BordIRLines、Poli-Bias、Chupilkin等均构成直接先例；正式发表和预印本应分开列，但不能因为是预印本就忽略思想重合。
3. **“首次研究联网是否带来偏向。”** 已有跨语言冲突RAG、政治检索偏向和AI搜索信息接触研究。值得研究的是何种来源和检索路径导致放大、缓解或方向反转。[L02](https://aclanthology.org/2025.findings-acl.219/) [R01](https://doi.org/10.1145/3613904.3642459) [R06](https://jok.kiise.or.kr/digital-library/108121)
4. **“跨语言差异就是民族主义偏向/迎合。”** 不同语言的事实覆盖、历史词汇、合理价值侧重与向用户让步是不同构念。角色可控性也不必然是迎合。[I03](https://ojs.aaai.org/index.php/AIES/article/view/36552) [L13](https://openreview.net/forum?id=zl16jLb91v)
5. **“模型回答分化已经证明人类极化或冲突升级。”** 当前设计审计模型输出；人类态度、理解、行为和社会后果需要另行证据。可用人类研究说明重要性，但不能代替本项目未测量的因果结果。[H01](https://doi.org/10.1126/science.adq2852) [H02](https://doi.org/10.1038/s41562-025-02194-6) [H03](https://doi.org/10.1126/science.aec8352)
6. **“英文回答是无偏基准。”** 英文只是第三种条件；它既可能提升一致性，也可能把所有回答推向同一偏向。不能把一致性等同于公正。[L02](https://aclanthology.org/2025.findings-acl.219/) [L13](https://openreview.net/forum?id=zl16jLb91v)

## 5. 仍可能形成贡献的方向：这是候选定位，不是已确认的文献空白

### A. 把“平行宇宙”定义为回答结构，而不是任意文本差异

分别测量：
- 共同且可核查事实的保留、遗漏或矛盾；
- 对同一行动者的合法性、责任、受害者/施害者角色；
- 对不确定性、争议事实和规范分歧的呈现；
- 同一政策问题上可合理不同的价值权衡。

这样才可区分“事实世界分裂”与“对同一事实持不同价值判断”。但Smirnov的同材料研究、Elfes等的叙事极化指标、Rashomon Wikipedia均已接近这些问题，须逐项对照；不能直接宣布该测量首次出现。[L07](https://arxiv.org/abs/2601.12164) [M10](https://doi.org/10.1093/pnasnexus/pgag270) [M16](https://arxiv.org/abs/2609.37498)

### B. 用语言与用户身份相冲突的条件，拆开机制

例如同一问题用俄语提出，用户却声明自己是乌克兰人；再对照乌语、俄罗斯用户、无身份条件。身份操纵应指向提问者，而不是让模型“扮演某国人”。显式国籍、隐含身份和明确政治主张也应分开。

可回答的实质问题是：当语言环境与用户身份指向不同方向时，哪个信号影响哪类回答内容？已有语言×角色、推断审计者身份和国际冲突用户国籍研究，需要在其基础上明确增量。[L04](https://aclanthology.org/2025.findings-acl.883/) [I01](https://arxiv.org/abs/2604.27633) [F02](https://arxiv.org/abs/2608.06123)

### C. 联网的贡献落到“来源—选用—叙事”的路径

至少区分：能检索到什么、实际引用什么、最终采用什么说法。保留搜索查询、检索时间、来源语言与域名、引用位置。若可控制证据，比较同一来源池与不同来源池，再考察产品真实搜索条件。

检索开/关可提供产品层面的总效应；只有总效应不足以说明来源机制。BordIRLines已比较多种检索语言组成，因此下一步应精确说明开放网页搜索、实际生成查询或来源采用上的新增问题。[L02](https://aclanthology.org/2025.findings-acl.219/) [R04](https://doi.org/10.1145/3731120.3744599) [R13](https://arxiv.org/abs/2610.00606)

### D. 把追问定义为有方向的转移，而不是“是否改口”

对称设置来自双方的压力，记录初始与追问后的位置，以及是否新增/丢失事实。有证据的反驳、纯立场反驳和一般“你确定吗”应分开。一次追问足以研究首次移动；它不能代表长期对话轨迹。

可关注语言、身份或来源条件是否改变移动方向，以及共享事实是否随让步而减少。此处的候选贡献是冲突情境中的条件化转移结构，而不是一次pushback设计本身。[S04](https://arxiv.org/abs/2311.08596) [S05](https://aclanthology.org/2025.findings-emnlp.1222/) [S06](https://aclanthology.org/2025.findings-emnlp.121/) [M17](https://aclanthology.org/2026.politicalnlp-1.26/)

### E. 案例差异应服务于解释，而不只是扩大覆盖

俄乌的直接竞争已很密集；印巴和巴以也已出现在领土/国际冲突审计中。尼罗河水资源冲突可提供不同争议结构，但本轮未找到明确对应“阿姆哈拉语—埃及阿拉伯语、双方身份、同一模型审计”的直接先例；这只是本轮未检出，不是不存在的证明。

如加入低资源语言，需排查翻译质量、模型语言能力和可检索语料差异。否则“资源冲突效应”可能混入语言资源差异。水外交的AI知识研究可以补足领域定位。[H06](https://doi.org/10.1007/s13280-025-02272-z) [S08](https://arxiv.org/abs/2606.08451)

## 6. 测量与材料上的直接启示

- **同时保留自然回答与强制量表。** Röttger等说明政治量表的选项、强迫回答和自然开放回答可能给出不同政治位置。不能只用强制选边来证明自然生成的叙事偏向。[M05](https://aclanthology.org/2024.acl-long.816/)
- **本土题库要拆解改动。** 等价措辞、强调框架、事实前提、情绪强度、肯定句/问句、身份标签都可能影响回答。建议镜像条件测可比性，本土条件测现实表达，再用编码标注它们究竟差在哪里。[M11](https://doi.org/10.1111/j.1460-2466.1993.tb01304.x) [M12](https://doi.org/10.1146/annurev.polisci.10.072805.103054) [M13](https://doi.org/10.1126/science.7455683) [F04](https://arxiv.org/abs/2602.23971)
- **词典指标要由上下文补足。** 出现带立场词语可能是引用、否定或批评，不能直接计为认同；责任、合法性和共同事实宜有独立编码。
- **AI评审须有人工锚点。** 双评审不是自动有效性保证；应盲化模型/条件，交换呈现顺序，并由母语研究者核对关键维度。[M07](https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html)
- **Wikipedia不是双方民意的替身。** 不同语言版本可以作为人类编辑信息环境参照，但编辑群体、时间和内容覆盖不同，不能直接称为两国公众意见。[M15](https://doi.org/10.1145/1753326.1753370) [M16](https://arxiv.org/abs/2609.37498)
- **模型差异不能只按国别解释。** 训练来源、对齐方式、语言能力、搜索工具和产品更新可能共变；跨模型结果可描述，训练机制的因果推断需要额外设计。[L05](https://doi.org/10.1038/s44387-025-00048-0) [G01](https://www.nature.com/articles/s41599-026-06577-6)

## 7. PPT引用和发表状态的校验

| 条目 | 本轮校验结果 | 建议 |
|---|---|---|
| Anthropic政治均衡评测 | 2025-11-13机构报告；使用相反立场成对提示，非仅中性题 | 保留为产品评测参照，准确描述其设计，不作为同行评议论文。[D01](https://www.anthropic.com/research/political-even-handedness) |
| OpenAI政治偏向评测 | 2025-10-09机构报告；含中性、带立场、情绪化提示；原文明确web search不在评测范围 | 可以说扩展其初始美国英语及无搜索范围，不能说它只用了中性问题。[D02](https://openai.com/index/defining-and-evaluating-political-bias-in-llms/) |
| Cheng等关于迎合与亲社会意图 | 已有Science 2026正式版，完整作者6人 | 将2025预印本引用更新为2026正式发表；其人际冲突结果不能自动外推到国际冲突。[H03](https://doi.org/10.1126/science.aec8352) |
| Costello等AI降低阴谋信念 | 原文2024发表；出版社2026-06-11另发Editorial Expression of Concern，Crossref更新关系已核实 | 如引用，附状态说明；关注声明不是撤稿或不端结论，本轮不把原效应数值当稳固依据。[原文](https://doi.org/10.1126/science.adq1814) / [编辑关注声明](https://doi.org/10.1126/science.aej2383) |
| BordIRLines | 2024 WikiNLP版本与2025 Findings ACL扩展版属同一研究谱系 | 目录合并一条，写作优先引用2025完整版本；不要算两项独立证据。[L02](https://aclanthology.org/2025.findings-acl.219/) |
| AI Pandering | 作者PDF与Research Square预印本；未确认期刊正式发表 | 标注工作论文/预印本，作者包含Diana Da In Lee。[F07](https://www.jamesbisbee.com/assets/pdf/ai_pandering_2_25_2026.pdf) |

## 8. 建议优先精读的顺序

1. **先确认最直接的竞争边界：** L01 BorderLines → L02 BordIRLines → F02 Poli-Bias → F07 AI Pandering → L06 Chupilkin → L07 Smirnov。
2. **再拆身份与框架构念：** I01 推断审计者身份 → I02 巴西政治迎合 → I03 GermanPartiesQA → I04 互动上下文 → F01 来源框架 → L15 英阿框架漂移。
3. **然后确定测量与追问：** M05 Political Compass or Spinning Arrow → S05 用户反驳 → S06 多轮迎合 → M10 叙事极化 → M17 立场稳定性。
4. **最后对照评测的准确表述：** D01、D02；人类重要性依据优先H01—H04。

真正需要交给团队的创新判断应是：“与上述最近邻相比，我们新增了哪个可解释的关系或现象，并用什么有效测量识别它？”本轮已经完成广泛文献地图和边界初筛；**尚未完成80条全文精读，也尚不能认证某个候选方向具有充分发表创新。**

