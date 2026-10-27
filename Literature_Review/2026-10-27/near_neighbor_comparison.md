# 现有文献库中的近邻研究

本表先按研究维度定位近邻。对于“是否明确研究因素之间的作用关系，并解释为什么”这一更严格标准，请优先阅读[Whether／Why正文核查](whether_why_neighbor_audit.md)。二者不能混同。

日期：2026-10-27。整理：Codex。以下8项均已在原80条目录中；本表不新增文献记录。研究对象仍是模型输出。

## 对照

| 原库ID／论文 | 接近我们设计的部分 | 需要区分的边界 | 原库记录 |
|---|---|---|---|
| F02 · [Poli-Bias](https://arxiv.org/abs/2608.06123v3) | 国际冲突；固定事实与法律条件；国家互换；用户国籍；多维评价 | 与模型偏差审计最直接重合。采用本轮v3；原库v1的模型数和人工验证不能混用。 | [记录](<../../Literature_Library/03_提问框架与来源框架/F02_2026_Poli-Bias Understanding and Measuring Large Language Model Biases in International Political Conflicts.md>) |
| L07 · [The Language You Ask In](https://arxiv.org/abs/2601.12164) | 同一政治材料，俄语／乌语提示产生不同合法性解释 | 与共享事实上的叙事分化直接重合；以单个文件的比较分析为主。 | [记录](<../../Literature_Library/01_语言与地缘政治/L07_2026_The Language You Ask In Language-Conditioned Ideological Divergence in LLM Analysis of Contested Political Documents.md>) |
| L02 · [BordIRLines](https://aclanthology.org/2025.findings-acl.219/) | 语言×检索×领土争议；多语言文档改善一致性 | 检索放大或缓解偏差已有直接组合研究；Wikipedia RAG与开放网页搜索有区别。 | [记录](<../../Literature_Library/01_语言与地缘政治/L02_2025_Multilingual Retrieval Augmented Generation for Culturally-Sensitive Tasks A Benchmark for Cross-lingual Robustness.md>) |
| F07 · [AI Pandering](https://www.jamesbisbee.com/assets/pdf/ai_pandering_2_25_2026.pdf) | 隐含用户立场、多轮对话、新闻来源推荐及事实确信分化 | 与平行现实的总体叙事尤其接近；使用LLM代理，不是人类态度实验；未做跨语言国际冲突。 | [记录](<../../Literature_Library/03_提问框架与来源框架/F07_2026_AI Pandering Constructing Diverging Political Realities through Conversation.md>) |
| I01 · [Political Bias Audits of LLMs Capture Sycophancy to the Inferred Auditor](https://arxiv.org/abs/2604.27633) | 明确身份操纵与模型对默认提问者的身份推断 | 与身份线索的解释机制相近；不提示身份也不能直接当成没有身份影响。 | [记录](<../../Literature_Library/02_用户身份与隐含线索/I01_2026_Political Bias Audits of LLMs Capture Sycophancy to the Inferred Auditor.md>) |
| L04 · [Navigating the Political Compass](https://aclanthology.org/2025.findings-acl.883/) | 语言与国家身份角色的组合 | 是语言×身份近邻，但身份赋予模型，不是用户自报国籍。 | [记录](<../../Literature_Library/01_语言与地缘政治/L04_2025_Navigating the Political Compass Evaluating Multilingual LLMs across Languages and Nationalities.md>) |
| S07 · [Investigating the Influence of Language on Sycophantic Behavior](https://arxiv.org/abs/2603.27664) | 不同语言下对用户观点的迎合程度 | 语言×迎合已有先例；不是国际冲突中的完整语言×用户国籍交叉设计。 | [记录](<../../Literature_Library/04_迎合与用户追问/S07_2026_Investigating the Influence of Language on Sycophantic Behavior of Multilingual LLMs.md>) |
| S05 · [Challenging the Evaluator](https://aclanthology.org/2025.findings-emnlp.1222/) | 追问与同时呈现论证；反驳理由及语气改变模型判断 | 追问是否导致改口、互动呈现如何影响判断已有方法近邻。 | [记录](<../../Literature_Library/04_迎合与用户追问/S05_2025_Challenging the Evaluator LLM Sycophancy Under User Rebuttal.md>) |

## 对候选创新点的判断

“语言与用户身份指向不同时，哪种线索主导回答”有值得比较的近邻：L04已有语言与国家角色组合，I01直接操纵提问者身份，F02检验国际冲突中的用户国籍，S07考察语言与迎合。它们不是完全相同的处理，但已经足以约束宽泛的首次主张。是否存在完全相同的语言×用户身份×立场框架交叉设计，尚不能由当前目录直接确定。

优先比较F02、F07、L07和L02，分别对应反事实差别对待、对话中的政治现实分化、共享材料的解释分化，以及跨语言检索。若把线索竞争作为主问题，再细查L04、I01和S07的条件设置。

## 核查层级与版本

本表结合原库记录、已有专题正文核查及本轮原始论文页面复核。L04、I01、S07本轮复核了正式摘要或作者预印本摘要；没有因此声称本轮重新精读其全部实验条件。F07的作者工作论文摘要亦已复核。F02以本轮保存的v3为准；其他论文的具体方法和边界沿用各自记录及已有核查，不把“相邻”写成“已经做完完全相同的设计”。

[返回核心短评](core_review.md)
