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

ALL_PROFILES: dict[str, ScientistProfile] = {
    p.id: p for p in [
        EINSTEIN, FEYNMAN, NEWTON, MENDEL, GALILEO,
        DOUDNA, HINTON, KARIKO, PENROSE, YAMANAKA,
    ]
}

CLASSICAL = [EINSTEIN, FEYNMAN, NEWTON, MENDEL, GALILEO]
NOBEL = [DOUDNA, HINTON, KARIKO, PENROSE, YAMANAKA]

def get_profile(scientist_id: str) -> ScientistProfile | None:
    return ALL_PROFILES.get(scientist_id.lower())

def get_profiles_by_level(level: str) -> list[ScientistProfile]:
    return [p for p in ALL_PROFILES.values() if p.level == level]
