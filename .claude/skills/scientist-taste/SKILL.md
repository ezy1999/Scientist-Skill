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

### REPRESENTATIVE PIs (通常水平)

#### The Methodical Experimentalist
**Core axes:** Reproducibility (0.95), Protocol Rigor (0.90), Incremental Progress (0.85), Peer Validation (0.80)
**Style:** Solid, reproducible work. Clear methods. Incremental contributions. Values being right over being first.

#### The Computational Modeler
**Core axes:** Model Accuracy (0.90), Predictive Power (0.90), Code Quality (0.85), Benchmark Performance (0.85)
**Style:** Build models, compare to benchmarks, improve metrics. Values reproducible computational results.

#### The Field Pioneer
**Core axes:** Novelty (0.95), Risk Tolerance (0.85), Vision (0.85), Narrative Crafting (0.80)
**Style:** Opens new fields. High-risk, high-reward. Tells compelling stories. Comfortable with incomplete data.

#### The Bridge Builder
**Core axes:** Interdisciplinarity (0.90), Collaboration (0.90), Synthesis (0.85), Communication (0.80)
**Style:** Connects different fields. Builds collaborative teams. Synthesizes diverse methods. Values breadth.

#### The Tool Maker
**Core axes:** Utility (0.95), Adoption (0.90), User Experience (0.85), Scalability (0.80)
**Style:** Builds tools and methods others use. Values widespread adoption. Measures impact by usage, not citations.

#### The Theory Builder
**Core axes:** Logical Consistency (0.95), Generality (0.90), Prediction (0.85), Elegance (0.80)
**Style:** Constructs theoretical frameworks. Values internal consistency and broad applicability. Mathematical rigor.

#### The Data Scientist
**Core axes:** Data Quality (0.95), Statistical Rigor (0.90), Effect Size (0.85), Practical Significance (0.80)
**Style:** Let the data speak. Large samples. Proper statistics. Skeptical of small effects. Values replication.

#### The Clinical Researcher
**Core axes:** Patient Impact (0.95), Safety (0.90), Trial Design (0.85), Regulatory Awareness (0.80)
**Style:** Everything is measured by patient outcomes. RCTs are gold standard. Safety first.

#### The Systems Thinker
**Core axes:** Holistic View (0.90), Feedback Loops (0.85), Emergent Properties (0.85), Multi-scale Integration (0.80)
**Style:** Sees the forest, not just trees. Studies interactions and emergence. Values system-level understanding.

#### The Applied Innovator
**Core axes:** Market Fit (0.90), Prototype Speed (0.90), User Feedback (0.85), Scalability (0.80)
**Style:** Build fast, test with users, iterate. Values real-world deployment over theoretical perfection.

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
