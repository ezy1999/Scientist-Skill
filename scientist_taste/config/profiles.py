"""
Scientist Taste Profiles Registry
===================================

Central registry of all scientist taste profiles. Each profile defines:
- Taste axes with weights
- Career periods
- Key evidence sources
- Evaluation style notes
"""

from __future__ import annotations
from pydantic import BaseModel, Field


class TasteAxis(BaseModel):
    name: str
    weight: float = Field(ge=0.0, le=1.0)
    description: str
    keywords: list[str] = Field(default_factory=list)


class ScientistProfile(BaseModel):
    """A complete taste profile for one scientist."""
    id: str
    name: str
    name_cn: str
    years: str
    field: str
    level: str  # "classical", "nobel", "pi"
    axes: list[TasteAxis]
    style_description: str
    style_description_cn: str
    would_love: list[str] = Field(default_factory=list)
    would_dislike: list[str] = Field(default_factory=list)
    key_evidence: list[str] = Field(default_factory=list)


# ══════════════════════════════════════════════════════════════════════════════
# CLASSICAL GIANTS
# ══════════════════════════════════════════════════════════════════════════════

EINSTEIN = ScientistProfile(
    id="einstein", name="Albert Einstein", name_cn="爱因斯坦",
    years="1879-1955", field="Physics", level="classical",
    axes=[
        TasteAxis(name="invariance", weight=0.95, description="Laws must be frame-independent", keywords=["covariance", "symmetry", "invariant"]),
        TasteAxis(name="unity", weight=0.90, description="Unify disparate phenomena", keywords=["unification", "single framework", "universal"]),
        TasteAxis(name="simplicity", weight=0.85, description="Minimize assumptions", keywords=["simple", "parsimony", "elegant"]),
        TasteAxis(name="physical_reality", weight=0.80, description="Objective reality exists", keywords=["realism", "determinism", "objective"]),
        TasteAxis(name="causal_continuity", weight=0.75, description="Local continuous causation", keywords=["locality", "continuous", "field"]),
        TasteAxis(name="mathematical_beauty", weight=0.70, description="Elegance guides truth", keywords=["beauty", "geometric", "elegant"]),
        TasteAxis(name="empirical_grounding", weight=0.65, description="Must be testable", keywords=["testable", "prediction", "experiment"]),
        TasteAxis(name="thought_experiment", weight=0.60, description="Gedankenexperiment", keywords=["thought experiment", "imagine"]),
    ],
    style_description="Top-down principle theorist. Seeks the deepest unifying framework.",
    style_description_cn="自上而下的原理理论家。追求最深层的统一框架。",
    would_love=["unified theories", "general principles", "geometric frameworks"],
    would_dislike=["ad hoc models", "observer-dependent reality", "too many parameters"],
    key_evidence=["Spencer Lecture (1933)", "EPR (1935)", "Holton's themata (1973)", "van Dongen (2010)"],
)

FEYNMAN = ScientistProfile(
    id="feynman", name="Richard Feynman", name_cn="费曼",
    years="1918-1988", field="Physics", level="classical",
    axes=[
        TasteAxis(name="physical_intuition", weight=0.95, description="Physical pictures over formalism", keywords=["picture", "visualize", "intuition"]),
        TasteAxis(name="computational_pragmatism", weight=0.90, description="Can you calculate a number?", keywords=["calculate", "compute", "number"]),
        TasteAxis(name="empirical_ruthlessness", weight=0.90, description="Disagrees with experiment = wrong", keywords=["experiment", "test", "verify"]),
        TasteAxis(name="playful_exploration", weight=0.85, description="Curiosity-driven, no pressure", keywords=["play", "fun", "curiosity"]),
        TasteAxis(name="independent_thinking", weight=0.85, description="Challenge authority, first principles", keywords=["independent", "first principles", "challenge"]),
        TasteAxis(name="anti_formalism", weight=0.80, description="Distrust pure abstraction", keywords=["concrete", "grounded", "against axioms"]),
        TasteAxis(name="bottom_up_reasoning", weight=0.80, description="Examples first, then generalize", keywords=["bottom-up", "examples", "specific"]),
        TasteAxis(name="multiple_representations", weight=0.75, description="Many views = deep understanding", keywords=["multiple", "representations", "equivalent"]),
        TasteAxis(name="simplicity_of_explanation", weight=0.75, description="Freshman test", keywords=["explain simply", "teach", "clear"]),
        TasteAxis(name="cross_domain", weight=0.70, description="Transfer ideas between fields", keywords=["cross-domain", "interdisciplinary"]),
    ],
    style_description="Bottom-up calculator. Physical pictures. Fierce honesty. Cut through BS.",
    style_description_cn="自下而上的计算者。物理图像优先。极度诚实。直击要害。",
    would_love=["calculable predictions", "physical pictures", "fun puzzles", "cross-domain"],
    would_dislike=["pure formalism", "cargo cult science", "authority-based arguments"],
    key_evidence=["Cargo Cult Science (1974)", "Character of Physical Law (1965)", "Gleick (1992)"],
)

NEWTON = ScientistProfile(
    id="newton", name="Isaac Newton", name_cn="牛顿",
    years="1643-1727", field="Physics/Mathematics", level="classical",
    axes=[
        TasteAxis(name="mathematical_rigor", weight=0.95, description="Mathematical proof required", keywords=["proof", "rigorous", "mathematical"]),
        TasteAxis(name="empirical_verification", weight=0.90, description="Confirmed by observation", keywords=["observation", "verified", "data"]),
        TasteAxis(name="mechanistic_explanation", weight=0.85, description="Clear causal mechanism", keywords=["mechanism", "cause", "force"]),
        TasteAxis(name="universality", weight=0.85, description="Same law everywhere", keywords=["universal", "law", "everywhere"]),
        TasteAxis(name="systematic_completeness", weight=0.80, description="Complete treatment", keywords=["complete", "systematic", "thorough"]),
    ],
    style_description="Hypotheses non fingo. Mathematical proof from phenomena. Complete systematic treatment.",
    style_description_cn="我不虚构假说。从现象出发进行数学证明。追求系统的完备性。",
    would_love=["precise mathematical laws", "universal mechanisms", "experimental verification"],
    would_dislike=["speculative hypotheses without math", "incomplete theories"],
    key_evidence=["Principia (1687)", "Opticks (1704)"],
)

MENDEL = ScientistProfile(
    id="mendel", name="Gregor Mendel", name_cn="孟德尔",
    years="1822-1884", field="Biology/Genetics", level="classical",
    axes=[
        TasteAxis(name="quantitative_precision", weight=0.95, description="Count everything, find ratios", keywords=["count", "ratio", "quantitative"]),
        TasteAxis(name="controlled_experimentation", weight=0.90, description="Proper controls", keywords=["control", "systematic", "controlled"]),
        TasteAxis(name="pattern_recognition", weight=0.85, description="Find mathematical patterns in biology", keywords=["pattern", "regularity", "ratio"]),
        TasteAxis(name="patient_accumulation", weight=0.85, description="Large N, years of data", keywords=["large sample", "patient", "accumulate"]),
        TasteAxis(name="statistical_thinking", weight=0.80, description="Probabilistic reasoning", keywords=["probability", "statistics", "variation"]),
    ],
    style_description="Meticulous experimenter. Large samples. Finds mathematical ratios in biology.",
    style_description_cn="一丝不苟的实验者。大样本量。在生物学中发现数学比例。",
    would_love=["large-N experiments", "precise quantification", "clear controls", "reproducible ratios"],
    would_dislike=["small samples", "lack of controls", "qualitative only"],
    key_evidence=["Experiments on Plant Hybridization (1866)", "28,000+ plants analyzed"],
)

GALILEO = ScientistProfile(
    id="galileo", name="Galileo Galilei", name_cn="伽利略",
    years="1564-1642", field="Physics/Astronomy", level="classical",
    axes=[
        TasteAxis(name="experimental_demonstration", weight=0.95, description="Show it with an experiment", keywords=["demonstrate", "experiment", "show"]),
        TasteAxis(name="quantitative_measurement", weight=0.90, description="Measure everything", keywords=["measure", "quantify", "number"]),
        TasteAxis(name="challenge_authority", weight=0.90, description="Data over dogma", keywords=["challenge", "question", "against dogma"]),
        TasteAxis(name="mathematical_description", weight=0.85, description="Nature's book is written in math", keywords=["mathematical", "law", "formula"]),
        TasteAxis(name="observational_evidence", weight=0.85, description="Direct observation", keywords=["observe", "see", "evidence"]),
    ],
    style_description="Father of experimental science. Measures everything. Challenges dogma with data.",
    style_description_cn="实验科学之父。测量一切。用数据挑战教条。",
    would_love=["direct measurement", "experimental proof", "challenging received wisdom"],
    would_dislike=["arguments from authority", "untested dogma"],
    key_evidence=["Dialogue (1632)", "Discorsi (1638)", "telescope observations"],
)

# ══════════════════════════════════════════════════════════════════════════════
# NOBEL LAUREATES
# ══════════════════════════════════════════════════════════════════════════════

DOUDNA = ScientistProfile(
    id="doudna", name="Jennifer Doudna", name_cn="杜德纳",
    years="b.1964", field="Chemistry/Biology", level="nobel",
    axes=[
        TasteAxis(name="mechanistic_clarity", weight=0.90, description="Understand the mechanism", keywords=["mechanism", "structure", "how it works"]),
        TasteAxis(name="translational_impact", weight=0.85, description="Real-world applications", keywords=["application", "impact", "tool"]),
        TasteAxis(name="structural_insight", weight=0.85, description="3D structure reveals function", keywords=["structure", "3D", "crystal"]),
        TasteAxis(name="collaborative_innovation", weight=0.80, description="Team science", keywords=["collaboration", "team", "interdisciplinary"]),
        TasteAxis(name="ethical_awareness", weight=0.80, description="Consider societal implications", keywords=["ethics", "responsibility", "society"]),
    ],
    style_description="Structure reveals function. Clear mechanisms. Responsible innovation.",
    style_description_cn="结构揭示功能。清晰的机制。负责任的创新。",
    would_love=["clear molecular mechanisms", "broad-impact tools", "responsible innovation"],
    would_dislike=["black-box methods", "ignoring ethical implications"],
    key_evidence=["CRISPR-Cas9 discovery (2012)", "A Crack in Creation (2017)"],
)

HINTON = ScientistProfile(
    id="hinton", name="Geoffrey Hinton", name_cn="辛顿",
    years="b.1947", field="Computer Science/AI", level="nobel",
    axes=[
        TasteAxis(name="biological_inspiration", weight=0.90, description="Brain-inspired", keywords=["brain", "neural", "biological"]),
        TasteAxis(name="representational_learning", weight=0.90, description="Learn representations, don't engineer", keywords=["learn", "representation", "emergent"]),
        TasteAxis(name="architecture_simplicity", weight=0.85, description="Simple architectures that scale", keywords=["simple", "scale", "architecture"]),
        TasteAxis(name="persistent_contrarianism", weight=0.85, description="Pursue unfashionable ideas", keywords=["contrarian", "unfashionable", "persist"]),
        TasteAxis(name="empirical_scaling", weight=0.80, description="Does it work at scale?", keywords=["scale", "large", "empirical"]),
    ],
    style_description="Neural networks as brain models. Simple architectures that learn. Decades of contrarian persistence.",
    style_description_cn="神经网络作为大脑模型。学习型简单架构。数十年逆流坚持。",
    would_love=["brain-inspired algorithms", "learned representations", "simple scalable architectures"],
    would_dislike=["hand-engineered features", "overly complex architectures"],
    key_evidence=["Backpropagation (1986)", "Deep Belief Networks (2006)", "AlexNet influence (2012)"],
)

KARIKO = ScientistProfile(
    id="kariko", name="Katalin Karikó", name_cn="卡里科",
    years="b.1955", field="Biochemistry", level="nobel",
    axes=[
        TasteAxis(name="experimental_persistence", weight=0.95, description="Never give up on a good idea", keywords=["persist", "determination", "years"]),
        TasteAxis(name="technical_precision", weight=0.90, description="Get the details right", keywords=["precise", "technical", "detail"]),
        TasteAxis(name="problem_focused", weight=0.85, description="Solve the actual problem", keywords=["problem", "practical", "solution"]),
        TasteAxis(name="underdog_resilience", weight=0.85, description="Continue despite rejection", keywords=["rejection", "resilience", "underdog"]),
        TasteAxis(name="translational_vision", weight=0.80, description="Lab to bedside", keywords=["translational", "clinical", "patient"]),
    ],
    style_description="40 years pursuing mRNA despite rejection. Precise technique. Make it actually work.",
    style_description_cn="40年坚持mRNA研究，尽管屡遭拒绝。精确技术。让它真正起作用。",
    would_love=["persistent difficult problems", "precise experiments", "practical medical applications"],
    would_dislike=["trend-chasing", "abandoning difficult problems", "flashy over substance"],
    key_evidence=["mRNA modification discovery (2005)", "40 years of mRNA research despite demotion"],
)

PENROSE = ScientistProfile(
    id="penrose", name="Roger Penrose", name_cn="彭罗斯",
    years="b.1931", field="Mathematics/Physics", level="nobel",
    axes=[
        TasteAxis(name="mathematical_beauty", weight=0.95, description="Beautiful math reveals truth", keywords=["beautiful", "elegant", "geometric"]),
        TasteAxis(name="geometric_visualization", weight=0.90, description="See it geometrically", keywords=["geometry", "diagram", "visual"]),
        TasteAxis(name="philosophical_depth", weight=0.85, description="Deep foundational questions", keywords=["philosophical", "foundational", "consciousness"]),
        TasteAxis(name="unconventional_connections", weight=0.85, description="Connect distant fields", keywords=["unconventional", "connection", "unexpected"]),
        TasteAxis(name="long_term_vision", weight=0.80, description="Pursue ideas for decades", keywords=["long-term", "decades", "patient"]),
    ],
    style_description="Deep mathematical structures reveal physical truth. Geometric insight. Deeply unconventional.",
    style_description_cn="深层数学结构揭示物理真理。几何洞察。深度非传统。",
    would_love=["beautiful mathematics", "geometric insights", "connections between distant fields"],
    would_dislike=["brute-force computation", "lack of geometric insight", "shallow empiricism"],
    key_evidence=["Penrose diagrams", "Twistor theory", "The Road to Reality (2004)"],
)

YAMANAKA = ScientistProfile(
    id="yamanaka", name="Shinya Yamanaka", name_cn="山中伸弥",
    years="b.1962", field="Medicine/Stem Cells", level="nobel",
    axes=[
        TasteAxis(name="clinical_motivation", weight=0.90, description="Motivated by patient need", keywords=["clinical", "patient", "disease"]),
        TasteAxis(name="bold_reprogramming", weight=0.90, description="Minimal intervention, maximal effect", keywords=["reprogram", "minimal", "transform"]),
        TasteAxis(name="efficiency", weight=0.85, description="Simplest intervention that works", keywords=["efficient", "minimal", "sufficient"]),
        TasteAxis(name="cross_disciplinary", weight=0.80, description="Surgery → stem cells → genomics", keywords=["cross-field", "pivot", "transfer"]),
        TasteAxis(name="ethical_innovation", weight=0.80, description="Ethical alternatives to embryonic stem cells", keywords=["ethics", "alternative", "responsible"]),
    ],
    style_description="Bold paradigm shift. Minimal factors for maximal effect. Clinical motivation.",
    style_description_cn="大胆的范式转换。最少因子实现最大效果。临床动机。",
    would_love=["minimal interventions with maximal effect", "clinically motivated research", "bold pivots"],
    would_dislike=["complex interventions", "research disconnected from clinical need"],
    key_evidence=["4 Yamanaka factors (2006)", "iPSC discovery", "pivot from surgery to stem cells"],
)

# ══════════════════════════════════════════════════════════════════════════════
# ALL PROFILES REGISTRY
# ══════════════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════════════
# REPRESENTATIVE PIs (based on documented research philosophies)
# ══════════════════════════════════════════════════════════════════════════════

URI_ALON = ScientistProfile(
    id="uri_alon", name="Uri Alon", name_cn="乌里·阿隆",
    years="b.1969", field="Systems Biology", level="pi",
    axes=[
        TasteAxis(name="design_principle_seeking", weight=0.90, description="Find engineering-like principles in biology", keywords=["motif", "principle", "design", "circuit"]),
        TasteAxis(name="embrace_uncertainty", weight=0.85, description="The 'cloud' of confusion is generative", keywords=["cloud", "uncertainty", "confusion", "creative"]),
        TasteAxis(name="feasibility_interest_balance", weight=0.85, description="Evaluate problems on how-hard vs how-interesting", keywords=["feasible", "interesting", "choose problem"]),
        TasteAxis(name="nurturing_pedagogy", weight=0.80, description="Emotional well-being as research methodology", keywords=["nurture", "mentor", "emotional", "lab culture"]),
    ],
    style_description="Find engineering principles in biological networks. Embrace the 'cloud' of uncertainty.",
    style_description_cn="在生物网络中寻找工程原理。拥抱不确定性的'迷雾'。",
    would_love=["design principles in biology", "well-chosen problems", "creative uncertainty"],
    would_dislike=["avoiding confusion", "purely incremental work"],
    key_evidence=["Network motifs", "How to Choose a Good Problem (Mol Cell)", "TED talk on the 'cloud'"],
)

TERENCE_TAO = ScientistProfile(
    id="terence_tao", name="Terence Tao", name_cn="陶哲轩",
    years="b.1975", field="Mathematics", level="pi",
    axes=[
        TasteAxis(name="multi_perspectival", weight=0.95, description="View every result from as many angles as possible", keywords=["multiple perspectives", "angles", "heuristic", "rigorous"]),
        TasteAxis(name="boundary_probing", weight=0.90, description="Select problems just beyond current tools", keywords=["boundary", "just beyond", "stretch"]),
        TasteAxis(name="simplification", weight=0.85, description="Find the right objects to reduce complexity", keywords=["simplify", "reduce", "right abstraction"]),
        TasteAxis(name="process_transparency", weight=0.80, description="Document how you actually approach problems", keywords=["process", "transparent", "approach"]),
    ],
    style_description="Multi-perspectival mathematician. Problems just beyond reach. Transparent process.",
    style_description_cn="多角度数学家。选择刚好超出能力范围的问题。过程透明。",
    would_love=["multi-view solutions", "elegant abstractions", "broad collaboration"],
    would_dislike=["single-perspective approaches", "opaque reasoning"],
    key_evidence=["Green-Tao theorem", "Fields Medal 2006", "'What is Good Mathematics?' (AMS Bull)"],
)

CHRIS_OLAH = ScientistProfile(
    id="chris_olah", name="Chris Olah", name_cn="克里斯·奥拉",
    years="b.1990s", field="AI Interpretability", level="pi",
    axes=[
        TasteAxis(name="clarity_as_output", weight=0.95, description="Understand clearly and explain well", keywords=["clarity", "understand", "explain", "visualize"]),
        TasteAxis(name="taste_over_technique", weight=0.90, description="Problem selection > execution skill", keywords=["taste", "problem selection", "what to work on"]),
        TasteAxis(name="visualization_first", weight=0.85, description="Visual/geometric intuition as primary tool", keywords=["visual", "geometric", "diagram", "picture"]),
        TasteAxis(name="non_credentialist", weight=0.80, description="Ideas matter more than pedigree", keywords=["ideas", "non-credentialist", "substance"]),
    ],
    style_description="Clarity is the research output. Taste > technique. Visualization-first understanding.",
    style_description_cn="清晰度就是研究成果。品味 > 技巧。可视化优先的理解方式。",
    would_love=["clear explanations", "visual understanding", "good problem selection"],
    would_dislike=["opaque models", "credential-based authority", "performance-only optimization"],
    key_evidence=["colah.github.io/notes/taste", "Feature visualization research", "Circuits interpretability"],
)

MANU_PRAKASH = ScientistProfile(
    id="manu_prakash", name="Manu Prakash", name_cn="马努·普拉卡什",
    years="b.1980", field="Frugal Science/Bioengineering", level="pi",
    axes=[
        TasteAxis(name="cost_as_design_parameter", weight=0.95, description="Affordability is a creative driver", keywords=["cost", "affordable", "frugal", "cheap"]),
        TasteAxis(name="access_first", weight=0.90, description="What if 1 billion people can use this?", keywords=["access", "global", "billion", "resource-limited"]),
        TasteAxis(name="physics_of_everyday", weight=0.85, description="Deep physics in mundane phenomena", keywords=["everyday", "mundane", "paper", "folding"]),
        TasteAxis(name="no_compromise_frugality", weight=0.85, description="Frugal does not mean inferior", keywords=["optimal", "no compromise", "performance"]),
    ],
    style_description="Frugal science: cost as a creative driver. Optimal performance at radical cost reduction.",
    style_description_cn="节俭科学：成本作为创造性驱动力。以激进的成本削减实现最优性能。",
    would_love=["$1 solutions to $10000 problems", "physics of everyday objects", "global access"],
    would_dislike=["expensive-only solutions", "ignoring resource-limited settings"],
    key_evidence=["Foldscope ($1 microscope)", "Paperfuge (20-cent centrifuge)", "HHMI investigator"],
)

SARA_WALKER = ScientistProfile(
    id="sara_walker", name="Sara Walker", name_cn="萨拉·沃克",
    years="b.1980s", field="Origin of Life/Theoretical Physics", level="pi",
    axes=[
        TasteAxis(name="theory_first", weight=0.95, description="Biology needs new physics, not just more chemistry", keywords=["theory", "physics for biology", "framework"]),
        TasteAxis(name="question_redefinition", weight=0.90, description="Reframe the question as the contribution", keywords=["redefine", "reframe", "new question"]),
        TasteAxis(name="radical_interdisciplinarity", weight=0.85, description="Merge physics, chemistry, philosophy, CS", keywords=["interdisciplinary", "merge", "bridge"]),
        TasteAxis(name="outsider_perspective", weight=0.85, description="Physicist entering biology brings new tools", keywords=["outsider", "new perspective", "different tools"]),
    ],
    style_description="Where's the theory? Physicist building new theoretical frameworks for life's origins.",
    style_description_cn="理论在哪里？物理学家为生命起源构建新的理论框架。",
    would_love=["new theoretical frameworks", "redefining questions", "cross-field synthesis"],
    would_dislike=["pure wet-lab without theory", "working within existing frameworks only"],
    key_evidence=["Assembly theory (with Cronin)", "Santa Fe Institute", "Life as No One Knows It (2024)"],
)

JOHN_JUMPER = ScientistProfile(
    id="john_jumper", name="John Jumper", name_cn="约翰·坚普",
    years="b.1985", field="AI for Structural Biology", level="pi",
    axes=[
        TasteAxis(name="domain_knowledge_injection", weight=0.95, description="Build physics into the architecture", keywords=["domain knowledge", "physics-aware", "constraint"]),
        TasteAxis(name="problem_driven_engineering", weight=0.90, description="Novel architecture for novel problem", keywords=["problem-driven", "novel architecture", "custom"]),
        TasteAxis(name="iterative_architecture", weight=0.85, description="Feedback loops > one-directional pipelines", keywords=["iterative", "feedback", "refinement"]),
        TasteAxis(name="computation_as_biology", weight=0.85, description="Computation genuinely solves biology", keywords=["computational biology", "solve", "prediction"]),
    ],
    style_description="Build physics into the neural network. Novel problems need novel architectures.",
    style_description_cn="将物理学嵌入神经网络。新问题需要新架构。",
    would_love=["domain-aware ML architectures", "physics-constrained models", "biology-solving computation"],
    would_dislike=["off-the-shelf models for unique problems", "ignoring domain structure"],
    key_evidence=["AlphaFold2 (2021)", "Nobel Chemistry 2024", "Evoformer architecture"],
)

CAROLYN_BERTOZZI = ScientistProfile(
    id="carolyn_bertozzi", name="Carolyn Bertozzi", name_cn="卡罗琳·贝尔托齐",
    years="b.1966", field="Chemical Biology", level="pi",
    axes=[
        TasteAxis(name="in_vivo_constraint_creativity", weight=0.95, description="Living systems constraint as design space", keywords=["in vivo", "living system", "biocompatible", "bioorthogonal"]),
        TasteAxis(name="tool_building_for_biology", weight=0.90, description="Chemistry tools for biological questions", keywords=["tool", "chemistry for biology", "probe"]),
        TasteAxis(name="selectivity_obsession", weight=0.85, description="Zero side-reactivity with natural molecules", keywords=["selective", "specific", "orthogonal", "no side reaction"]),
        TasteAxis(name="iterative_improvement", weight=0.80, description="Systematically remove each practical limitation", keywords=["improve", "iterate", "remove limitation"]),
    ],
    style_description="Invented chemistry that works inside living organisms. Constraint as creative space.",
    style_description_cn="发明了在活体内工作的化学。约束即创造空间。",
    would_love=["bioorthogonal reactions", "in-vivo compatible tools", "systematic improvement"],
    would_dislike=["flask-only chemistry", "ignoring biological compatibility"],
    key_evidence=["Bioorthogonal chemistry", "Click chemistry (Nobel 2022)", "Glycan imaging in live organisms"],
)

REDIET_ABEBE = ScientistProfile(
    id="rediet_abebe", name="Rediet Abebe", name_cn="雷迪特·阿贝贝",
    years="b.1991", field="CS/Algorithmic Fairness", level="pi",
    axes=[
        TasteAxis(name="equity_as_objective", weight=0.95, description="Fairness is the optimization target", keywords=["equity", "fairness", "justice", "inequality"]),
        TasteAxis(name="deeply_interdisciplinary", weight=0.90, description="Computational work informed by social science", keywords=["interdisciplinary", "social", "community"]),
        TasteAxis(name="harm_aware", weight=0.85, description="Model negative consequences of algorithms", keywords=["harm", "consequence", "negative impact"]),
        TasteAxis(name="community_building", weight=0.85, description="Creating research communities as scholarship", keywords=["community", "conference", "organize"]),
    ],
    style_description="Algorithms where fairness is the objective function. Community-building as research.",
    style_description_cn="以公平为目标函数的算法。社区建设即研究。",
    would_love=["equity-focused algorithms", "community-engaged research", "interdisciplinary grounding"],
    would_dislike=["ignoring social impact", "abstract bounds without real-world grounding"],
    key_evidence=["MD4SG (Mechanism Design for Social Good)", "ACM EAAMO conference", "Quanta Magazine profile"],
)

SUBHASH_KHOT = ScientistProfile(
    id="subhash_khot", name="Subhash Khot", name_cn="苏巴什·科特",
    years="b.1978", field="Computational Complexity", level="pi",
    axes=[
        TasteAxis(name="conjecture_as_contribution", weight=0.95, description="Posing the right question > solving existing ones", keywords=["conjecture", "question", "framing"]),
        TasteAxis(name="boundary_mapping", weight=0.90, description="Delineate tractable vs intractable precisely", keywords=["boundary", "tractable", "hardness"]),
        TasteAxis(name="long_horizon_conviction", weight=0.85, description="Pursue ideas for years despite divided opinion", keywords=["conviction", "long-term", "persist"]),
        TasteAxis(name="cross_area_bridge", weight=0.80, description="Connect complexity with analysis and geometry", keywords=["bridge", "connect", "analysis", "geometry"]),
    ],
    style_description="The right question is more valuable than solving the wrong one. Conjecture as contribution.",
    style_description_cn="提出正确的问题比解决错误的问题更有价值。猜想即贡献。",
    would_love=["right questions over quick answers", "hardness-approximation connections"],
    would_dislike=["avoiding hard open questions", "narrow technical contributions"],
    key_evidence=["Unique Games Conjecture (2002)", "Nevanlinna Prize 2014", "MacArthur Fellow"],
)

DANIELA_WITTEN = ScientistProfile(
    id="daniela_witten", name="Daniela Witten", name_cn="丹妮拉·威滕",
    years="b.1985", field="Statistical ML/Biostatistics", level="pi",
    axes=[
        TasteAxis(name="scientist_question_driven", weight=0.90, description="Methods from what scientists need to ask", keywords=["scientist-driven", "collaboration", "real question"]),
        TasteAxis(name="structure_exploitation", weight=0.90, description="Leverage data structure, not brute force", keywords=["structure", "exploit", "leverage"]),
        TasteAxis(name="inferential_rigor", weight=0.85, description="Formal inference for exploratory methods", keywords=["inference", "rigorous", "selective", "valid"]),
        TasteAxis(name="broad_communication", weight=0.80, description="Textbooks as first-class research", keywords=["textbook", "communicate", "accessible"]),
    ],
    style_description="Methods driven by what scientists actually need. Formal inference meets exploration.",
    style_description_cn="方法由科学家的实际需求驱动。形式推断与探索的结合。",
    would_love=["scientist-motivated methods", "structure-exploiting algorithms", "accessible teaching"],
    would_dislike=["methods without scientific motivation", "brute-force approaches"],
    key_evidence=["ISLR textbook (co-author)", "Selective inference framework", "COPSS Presidents' Award 2020"],
)

# ══════════════════════════════════════════════════════════════════════════════
# ALL PROFILES REGISTRY
# ══════════════════════════════════════════════════════════════════════════════

ALL_PROFILES: dict[str, ScientistProfile] = {
    p.id: p for p in [
        # Classical Giants
        EINSTEIN, FEYNMAN, NEWTON, MENDEL, GALILEO,
        # Nobel Laureates
        DOUDNA, HINTON, KARIKO, PENROSE, YAMANAKA,
        # Representative PIs (with documented research philosophies)
        URI_ALON, TERENCE_TAO, CHRIS_OLAH, MANU_PRAKASH, SARA_WALKER,
        JOHN_JUMPER, CAROLYN_BERTOZZI, REDIET_ABEBE, SUBHASH_KHOT, DANIELA_WITTEN,
    ]
}

CLASSICAL = [EINSTEIN, FEYNMAN, NEWTON, MENDEL, GALILEO]
NOBEL = [DOUDNA, HINTON, KARIKO, PENROSE, YAMANAKA]
PI = [URI_ALON, TERENCE_TAO, CHRIS_OLAH, MANU_PRAKASH, SARA_WALKER,
      JOHN_JUMPER, CAROLYN_BERTOZZI, REDIET_ABEBE, SUBHASH_KHOT, DANIELA_WITTEN]

def get_profile(scientist_id: str) -> ScientistProfile | None:
    return ALL_PROFILES.get(scientist_id.lower())

def get_profiles_by_level(level: str) -> list[ScientistProfile]:
    return [p for p in ALL_PROFILES.values() if p.level == level]
