---
name: ScientistResearchTaste.Skill
description: Multi-scientist research taste evaluation system. Apply the thinking patterns of Einstein, Feynman, Newton, Mendel, Galileo, 5 Nobel laureates, and 10 active PIs. Supports individual, group, and comparative evaluation modes.
---

# ScientistResearchTaste.Skill

A meta-level scientific taste evaluation system that houses **20+ scientist taste profiles** spanning classical giants, Nobel laureates, and contemporary PIs. Apply individual or collective scientific wisdom to evaluate any research question, theory, or decision.

## Core Principle: Taste Is Learnable and Transferable

Scientific taste — the implicit criteria by which scientists judge what is promising, elegant, or important — can be extracted from documented evidence and applied to any domain or era. This system does NOT role-play as scientists. It models their documented evaluation criteria and applies those criteria to your questions.

## When to Trigger

Activate when the user:
- Asks for scientific evaluation from a specific scientist's perspective
- Wants to evaluate a research direction using "great scientist" thinking
- Says "what would [scientist] think", "evaluate this like [X]"
- Asks for a "group meeting" or "panel discussion" evaluation
- Wants to compare how different scientific traditions would view a problem
- Needs hypothesis generation guided by specific research taste profiles
- Discusses research taste, scientific aesthetics, or methodology selection

## Available Modes

### Mode 1: Individual Scientist
Evaluate through one scientist's taste profile.
- Usage: "用爱因斯坦的品味评估..." or "What would Feynman think about..."
- Available profiles listed below.

### Mode 2: Era/Level Selection
Evaluate through a category of scientists.
- **古早大师 (Classical Giants):** Einstein, Feynman, Newton, Mendel, Galileo — deep first-principles thinking
- **诺奖级 (Nobel-level):** Doudna, Hinton, Karikó, Penrose, Yamanaka — cutting-edge methodology
- **通常PI (Regular PIs):** 10 representative active professors — practical, publication-oriented
- Usage: "用诺奖级科学家的标准评估..." or "如果是普通PI会怎么看..."

### Mode 3: Group Meeting (群体讨论)
Simulate a research group meeting where multiple taste profiles weigh in.
- Each scientist gives their perspective based on their taste axes
- Disagreements are highlighted
- A synthesis is provided at the end
- Usage: "召开一个品味评审会议来讨论我的项目"

### Mode 4: Comparative
Compare how different scientists/levels would evaluate the same idea.
- Usage: "比较爱因斯坦和费曼对这个方向的看法" or "古早大师vs诺奖级怎么看这个问题"

## Response Protocol

### Step 1: Conversational Response (ALWAYS FIRST)
Natural language analysis through the selected taste profile(s). Direct, insightful, addresses the user's actual question. For group mode: each scientist speaks in turn.

### Step 2: Structured Scoring
Per-scientist axis scores, then synthesis.

## Scientist Profiles

---

### CLASSICAL GIANTS (古早大师)

#### Albert Einstein (1879–1955) | Physics
**Core axes:** Invariance (0.95), Unity (0.90), Simplicity (0.85), Physical Reality (0.80), Mathematical Beauty (0.70)
**Style:** Top-down principle theorist. Seeks the deepest unifying framework. Trusts mathematical elegance. Demands observer-independence.
**Key evidence:** Spencer Lecture (1933), EPR (1935), Holton's themata (1973), van Dongen (2010).
**Would love:** Unified theories, general principles, geometric frameworks, thought experiments.
**Would dislike:** Ad hoc models, observer-dependent reality, action-at-distance, excessive parameters.

#### Richard Feynman (1918–1988) | Physics
**Core axes:** Physical Intuition (0.95), Computational Pragmatism (0.90), Empirical Ruthlessness (0.90), Playful Exploration (0.85), Anti-Formalism (0.80)
**Style:** Bottom-up calculator. "Shut up and compute." Physical pictures over formalism. Fierce honesty.
**Key evidence:** Cargo Cult Science (1974), Character of Physical Law (1965), Nobel Lecture (1965), Gleick (1992).
**Would love:** Calculable predictions, physical pictures, fun puzzles, cross-domain applications.
**Would dislike:** Pure formalism, philosophical hand-waving, cargo cult science, authority-based arguments.

#### Isaac Newton (1643–1727) | Physics/Mathematics
**Core axes:** Mathematical Rigor (0.95), Empirical Verification (0.90), Mechanistic Explanation (0.85), Universality (0.85), Systematic Completeness (0.80)
**Style:** Hypotheses non fingo — I frame no hypotheses beyond what can be deduced from phenomena. Demands mathematical proof.
**Key evidence:** Principia (1687), Opticks (1704), correspondence with Leibniz, Hooke.
**Would love:** Precise mathematical laws, universal mechanisms, complete systematic treatment, experimental verification.
**Would dislike:** Speculative hypotheses without math, qualitative hand-waving, incomplete theories.

#### Gregor Mendel (1822–1884) | Biology/Genetics
**Core axes:** Quantitative Precision (0.95), Controlled Experimentation (0.90), Pattern Recognition (0.85), Patient Accumulation (0.85), Statistical Thinking (0.80)
**Style:** Meticulous experimenter. Large sample sizes. Counts everything. Finds mathematical ratios in biological data.
**Key evidence:** Experiments on Plant Hybridization (1866), 8 years of pea experiments, 28,000+ plants analyzed.
**Would love:** Large-N experiments, precise quantification, clear controls, reproducible ratios, statistical evidence.
**Would dislike:** Small samples, qualitative descriptions, lack of controls, ignoring variability.

#### Galileo Galilei (1564–1642) | Physics/Astronomy
**Core axes:** Experimental Demonstration (0.95), Quantitative Measurement (0.90), Challenge Authority (0.90), Mathematical Description (0.85), Observational Evidence (0.85)
**Style:** Father of experimental science. Measures everything. Challenges dogma with data. "Measure what is measurable, and make measurable what is not so."
**Key evidence:** Dialogue (1632), Discorsi (1638), telescope observations, inclined plane experiments.
**Would love:** Direct measurement, experimental proof, mathematical laws from data, challenging received wisdom.
**Would dislike:** Arguments from authority, untested dogma, purely theoretical speculation.

---

### NOBEL LAUREATES (诺奖级)

#### Jennifer Doudna (b.1964) | Chemistry/Biology, Nobel 2020
**Core axes:** Mechanistic Clarity (0.90), Translational Impact (0.85), Structural Insight (0.85), Collaborative Innovation (0.80), Ethical Awareness (0.80)
**Style:** Structure reveals function. Understands mechanism through 3D molecular architecture. Deeply concerned with societal implications.
**Would love:** Clear molecular mechanisms, structural biology approaches, tools with broad impact, responsible innovation.
**Would dislike:** Black-box methods without mechanistic understanding, ignoring ethical implications.

#### Geoffrey Hinton (b.1947) | Computer Science, Nobel Physics 2024
**Core axes:** Biological Inspiration (0.90), Representational Learning (0.90), Simplicity of Architecture (0.85), Persistent Contrarianism (0.85), Empirical Scaling (0.80)
**Style:** Neural networks as models of the brain. Simple architectures that learn complex representations. Willing to be wrong for decades until proven right.
**Would love:** Brain-inspired algorithms, learned representations, simple elegant architectures that scale, challenging conventional wisdom.
**Would dislike:** Hand-engineered features, overly complex architectures, ignoring biological plausibility.

#### Katalin Karikó (b.1955) | Biochemistry, Nobel Medicine 2023
**Core axes:** Experimental Persistence (0.95), Technical Precision (0.90), Problem-Focused Pragmatism (0.85), Underdog Resilience (0.85), Translational Vision (0.80)
**Style:** 40 years pursuing mRNA despite rejection and demotion. Extremely technically precise. Focused on making things actually work, not publishing flashy papers.
**Would love:** Persistent pursuit of difficult problems, precise experimental technique, practical medical applications, determination despite skepticism.
**Would dislike:** Trend-chasing, abandoning difficult problems, prioritizing publications over real results.

#### Roger Penrose (b.1931) | Mathematics/Physics, Nobel Physics 2020
**Core axes:** Mathematical Beauty (0.95), Geometric Visualization (0.90), Philosophical Depth (0.85), Unconventional Connections (0.85), Long-term Vision (0.80)
**Style:** Deep mathematical structures reveal physical truth. Penrose diagrams, twistor theory, Penrose tiling. Willing to pursue deeply unconventional ideas (quantum consciousness).
**Would love:** Beautiful mathematical structures, geometric insights, connections between distant fields, philosophical rigor.
**Would dislike:** Computationally brute-force approaches, lack of geometric insight, shallow empiricism.

#### Shinya Yamanaka (b.1962) | Medicine, Nobel Medicine 2012
**Core axes:** Clinical Motivation (0.90), Bold Reprogramming (0.90), Efficiency of Approach (0.85), Cross-disciplinary Transfer (0.80), Ethical Innovation (0.80)
**Style:** Pivoted from surgery to stem cells because he wanted bigger impact. Found the minimal set of factors (4 Yamanaka factors) for cell reprogramming. Efficiency-driven: what's the simplest intervention?
**Would love:** Minimal interventions with maximal effect, clinically motivated basic research, bold paradigm shifts, ethical awareness.
**Would dislike:** Overly complex interventions, basic research disconnected from clinical need, incremental approaches to transformative problems.

---

### CONTEMPORARY PIs (当代代表性PI — 全部为真实人物)

#### Uri Alon (b.1969) | Systems Biology, Weizmann Institute
**Core axes:** Design Principle Seeking (0.90), Embrace Uncertainty (0.85), Feasibility-Interest Balance (0.85), Nurturing Pedagogy (0.80)
**Style:** Find engineering principles in biological networks. The "cloud" of confusion is creative, not to be avoided.
**Key evidence:** Network motifs discovery; "How to Choose a Good Scientific Problem" (Molecular Cell); TED talk on the "cloud."
**Would love:** Design principles in biology, well-chosen problems, creative labs.
**Would dislike:** Avoiding confusion, purely incremental work, toxic lab cultures.

#### Terence Tao (b.1975) | Mathematics, UCLA, Fields Medal 2006
**Core axes:** Multi-Perspectival (0.95), Boundary Probing (0.90), Simplification (0.85), Process Transparency (0.80)
**Style:** View every result from as many angles as possible. Select problems just beyond current tools. Rare breadth across 12+ subfields.
**Key evidence:** Green-Tao theorem; "What is Good Mathematics?" (AMS Bulletin); blog.
**Would love:** Multiple-view solutions, elegant abstractions, problems at the boundary of tractability.
**Would dislike:** Single-perspective approaches, opaque reasoning.

#### Chris Olah (b.~1990) | AI Interpretability, Anthropic
**Core axes:** Clarity as Output (0.95), Taste Over Technique (0.90), Visualization First (0.85), Non-Credentialist (0.80)
**Style:** "I want to understand things clearly and explain them well." Built major research career without a degree. Taste > technique.
**Key evidence:** colah.github.io/notes/taste; feature visualization; Circuits interpretability.
**Would love:** Clear explanations, visual understanding, good problem selection.
**Would dislike:** Opaque models, credential-based authority, performance-only optimization.

#### Manu Prakash (b.1980) | Frugal Science, Stanford
**Core axes:** Cost as Design Parameter (0.95), Access-First Design (0.90), Physics of Everyday (0.85), No-Compromise Frugality (0.85)
**Style:** $1 microscope (Foldscope), 20-cent centrifuge (Paperfuge). Affordability is a creative driver, not a compromise.
**Key evidence:** Foldscope; Paperfuge; HHMI investigator; IEEE Spectrum profile.
**Would love:** $1 solutions to $10000 problems, physics of mundane objects, billion-person scale.
**Would dislike:** Expensive-only solutions, ignoring resource-limited settings.

#### Sara Walker (b.~1980) | Origin of Life, Arizona State / Santa Fe Institute
**Core axes:** Theory First (0.95), Question Redefinition (0.90), Radical Interdisciplinarity (0.85), Outsider Perspective (0.85)
**Style:** Physicist entering biology asks: "Where's the theory?" Creates new theoretical vocabularies (Assembly Theory).
**Key evidence:** Assembly Theory (with Cronin); Santa Fe Institute; "Life as No One Knows It" (2024).
**Would love:** New theoretical frameworks, redefining questions, cross-field synthesis.
**Would dislike:** Pure wet-lab without theory, working within existing frameworks only.

#### John Jumper (b.1985) | AI for Structural Biology, DeepMind, Nobel Chemistry 2024
**Core axes:** Domain Knowledge Injection (0.95), Problem-Driven Engineering (0.90), Iterative Architecture (0.85), Computation as Biology (0.85)
**Style:** Build physics into the neural network. AlphaFold2's Evoformer was custom-designed for protein structure, not off-the-shelf.
**Key evidence:** AlphaFold2 (2021); Nobel Chemistry 2024; Evoformer architecture.
**Would love:** Domain-aware architectures, physics-constrained ML, biology-solving computation.
**Would dislike:** Off-the-shelf models for unique problems, ignoring domain structure.

#### Carolyn Bertozzi (b.1966) | Chemical Biology, Stanford, Nobel Chemistry 2022
**Core axes:** In-Vivo Constraint as Creativity (0.95), Tool Building for Biology (0.90), Selectivity Obsession (0.85), Iterative Improvement (0.80)
**Style:** Invented chemistry that works inside living organisms. Living-system compatibility is the design space, not a constraint.
**Key evidence:** Bioorthogonal chemistry; click chemistry Nobel 2022; glycan imaging in live organisms.
**Would love:** Bioorthogonal reactions, in-vivo compatible tools, systematic iterative improvement.
**Would dislike:** Flask-only chemistry, ignoring biological compatibility.

#### Rediet Abebe (b.1991) | Algorithmic Fairness, UC Berkeley
**Core axes:** Equity as Objective (0.95), Deep Interdisciplinarity (0.90), Harm Awareness (0.85), Community Building (0.85)
**Style:** Algorithms where fairness is the optimization target. Created the MD4SG community and EAAMO conference as scholarly contributions.
**Key evidence:** MD4SG; ACM EAAMO conference; Quanta Magazine profile.
**Would love:** Equity-focused algorithms, community-engaged research, interdisciplinary grounding.
**Would dislike:** Ignoring social impact, abstract bounds without real-world grounding.

#### Subhash Khot (b.1978) | Computational Complexity, NYU, Nevanlinna Prize 2014
**Core axes:** Conjecture as Contribution (0.95), Boundary Mapping (0.90), Long-Horizon Conviction (0.85), Cross-Area Bridge (0.80)
**Style:** The right question is more valuable than solving the wrong one. Won a major prize for a conjecture, not a proof.
**Key evidence:** Unique Games Conjecture (2002); Nevanlinna Prize 2014; MacArthur Fellow.
**Would love:** Right questions over quick answers, hardness-approximation connections.
**Would dislike:** Avoiding hard open questions, narrow technical contributions.

#### Daniela Witten (b.1985) | Statistical ML, U. of Washington, COPSS Award 2020
**Core axes:** Scientist-Question-Driven (0.90), Structure Exploitation (0.90), Inferential Rigor (0.85), Broad Communication (0.80)
**Style:** Methods motivated by what scientists actually need. Brings formal inference to exploratory methods. ISLR textbook as first-class output.
**Key evidence:** ISLR textbook (co-author); selective inference framework; COPSS Presidents' Award 2020.
**Would love:** Scientist-motivated methods, structure-exploiting algorithms, accessible teaching.
**Would dislike:** Methods without scientific motivation, brute-force approaches.

---

## Group Meeting Mode Example

**User:** "我想用图神经网络预测新材料的性质，召开一个品味评审会来讨论"

**Response:**

**Einstein 视角：**
这个方向的核心问题是——图神经网络是在发现材料性质的统一规律，还是只在做曲线拟合？如果能从模型中提取出某种简洁的物理原理，比如"所有材料性质都可以从某种不变量推导出来"，那就有深层价值。否则，它只是一个高级的查找表。

**Feynman 视角：**
先算一个具体的数字。选一种已知的材料，看你的模型能不能准确预测它的带隙或硬度。然后再选一种你模型没见过的材料，做出预测并去实验室验证。如果验证通过了，你就有了真正的东西。如果只是在测试集上表现好——那可能是cargo cult。

**Newton 视角：**
你需要数学上的严格性。图神经网络的预测精度具体是多少？误差棒有多大？和已有的第一性原理计算相比，优势是什么？请用数字说话，不要用"表现很好"这种定性描述。

**Doudna 视角：**
这个预测能实际指导实验吗？如果你预测某种组合会有特殊性质，实验组能不能立即去合成和验证？工具的价值在于它能不能真的帮人做出新材料。

**Karikó 视角：**
这个方向别人看好吗？如果很多人在做，要小心变成跟风。如果别人不看好但你有扎实的初步结果——坚持下去。最好的工作往往来自别人不愿意做的方向。

**综合评审：**
| 科学家 | 总分 | 核心关切 |
|--------|------|---------|
| Einstein | +0.35 | 能否揭示统一原理？ |
| Feynman | +0.45 | 能否算出可验证的数字？ |
| Newton | +0.40 | 数学精度如何？ |
| Doudna | +0.50 | 能否直接指导实验？ |
| Karikó | +0.55 | 有没有坚实的初步结果？ |

**共识：** 方向有潜力，但需要：(1) 具体的数值预测+实验验证；(2) 探索模型是否揭示了某种物理规律；(3) 不要只追求benchmark分数。

---

## Comparative Mode Example

**User:** "古早大师 vs 诺奖级科学家，怎么看transformer架构？"

| 维度 | 古早大师视角 | 诺奖级视角 |
|------|------------|-----------|
| 核心关切 | 是否揭示了某种不变原理？(Einstein) 能否用物理图像理解？(Feynman) | 是否受大脑启发？(Hinton) 能否用于解决真实问题？(Doudna) |
| 优点 | 注意力机制有数学优雅性(Einstein+), 可以计算具体结果(Feynman+) | 学到的表示很强大(Hinton+), 已证明大规模实用价值(Karikó+) |
| 缺点 | 参数太多不够简约(Einstein-), 不理解因果机制(Newton-) | 缺乏可解释性(Penrose-), 能耗太大效率存疑(Yamanaka-) |

---

## For Python API (Optional)

```bash
git clone https://github.com/ezy1999/Scientist-Skill.git
cd Scientist-Skill && pip install -e .
```
