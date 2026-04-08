"""
Multi-Scientist Taste Evaluator
================================

Evaluates candidates through one or more scientist taste profiles.
Supports individual, group, and comparative modes.
"""

from __future__ import annotations
from pydantic import BaseModel, Field
from scientist_taste.config.profiles import ScientistProfile, TasteAxis, get_profile, ALL_PROFILES


class AxisScore(BaseModel):
    axis_name: str
    score: float = Field(ge=-1.0, le=1.0)
    confidence: float = Field(ge=0.0, le=1.0)
    is_evidence_based: bool = True
    explanation: str = ""


class SingleEvaluation(BaseModel):
    """Evaluation of a candidate through one scientist's taste."""
    scientist_id: str
    scientist_name: str
    candidate: str
    axis_scores: list[AxisScore] = Field(default_factory=list)
    overall_score: float = 0.0
    overall_confidence: float = 0.0
    conversational_response: str = ""  # Natural language response
    caveats: list[str] = Field(default_factory=list)


class GroupEvaluation(BaseModel):
    """Evaluation of a candidate by a group of scientists."""
    candidate: str
    mode: str  # "individual", "group", "comparative"
    evaluations: list[SingleEvaluation] = Field(default_factory=list)
    synthesis: str = ""  # Overall synthesis


class TasteEvaluator:
    """Evaluates candidates using scientist taste profiles."""

    def __init__(self):
        self.profiles = ALL_PROFILES

    def evaluate_single(self, candidate: str, scientist_id: str) -> SingleEvaluation:
        """Evaluate through one scientist's profile using keyword matching."""
        profile = get_profile(scientist_id)
        if not profile:
            return SingleEvaluation(
                scientist_id=scientist_id, scientist_name="Unknown",
                candidate=candidate, caveats=[f"Profile '{scientist_id}' not found"],
            )
        candidate_lower = candidate.lower()
        axis_scores = []
        for axis in profile.axes:
            kw_hits = sum(1 for kw in axis.keywords if kw.lower() in candidate_lower)
            score = min(1.0, kw_hits * 0.3) if kw_hits > 0 else 0.0
            # Check "would_dislike" patterns
            for dislike in profile.would_dislike:
                if any(w in candidate_lower for w in dislike.lower().split()[:3]):
                    score = max(-1.0, score - 0.4)
            # Check "would_love" patterns
            for love in profile.would_love:
                if any(w in candidate_lower for w in love.lower().split()[:3]):
                    score = min(1.0, score + 0.3)
            axis_scores.append(AxisScore(
                axis_name=axis.name, score=max(-1.0, min(1.0, score)),
                confidence=min(1.0, 0.3 + kw_hits * 0.2),
                is_evidence_based=kw_hits > 0,
                explanation=f"{kw_hits} keyword matches",
            ))
        # Weighted aggregate
        total_w = sum(a.weight for a in profile.axes)
        overall = sum(s.score * a.weight for s, a in zip(axis_scores, profile.axes)) / total_w if total_w else 0
        conf = sum(s.confidence * a.weight for s, a in zip(axis_scores, profile.axes)) / total_w if total_w else 0
        return SingleEvaluation(
            scientist_id=profile.id, scientist_name=profile.name,
            candidate=candidate, axis_scores=axis_scores,
            overall_score=overall, overall_confidence=conf,
        )

    def evaluate_group(self, candidate: str, scientist_ids: list[str] | None = None, level: str | None = None) -> GroupEvaluation:
        """Evaluate through a group of scientists."""
        from scientist_taste.config.profiles import get_profiles_by_level
        if scientist_ids:
            ids = scientist_ids
        elif level:
            ids = [p.id for p in get_profiles_by_level(level)]
        else:
            ids = list(self.profiles.keys())

        evals = [self.evaluate_single(candidate, sid) for sid in ids]
        return GroupEvaluation(
            candidate=candidate, mode="group",
            evaluations=evals,
            synthesis=self._synthesize(evals),
        )

    def _synthesize(self, evals: list[SingleEvaluation]) -> str:
        """Create a synthesis of multiple evaluations."""
        if not evals:
            return "No evaluations."
        avg = sum(e.overall_score for e in evals) / len(evals)
        best = max(evals, key=lambda e: e.overall_score)
        worst = min(evals, key=lambda e: e.overall_score)
        return (
            f"Average score: {avg:+.2f}. "
            f"Most favorable: {best.scientist_name} ({best.overall_score:+.2f}). "
            f"Least favorable: {worst.scientist_name} ({worst.overall_score:+.2f})."
        )
