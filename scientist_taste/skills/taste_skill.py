"""
Claude Code Skill wrapper for multi-scientist taste evaluation.
"""

from scientist_taste.core.evaluator import TasteEvaluator, SingleEvaluation, GroupEvaluation
from scientist_taste.config.profiles import ALL_PROFILES, get_profiles_by_level
from scientist_taste.utils.formatting import format_single, format_group, format_comparison_table


class ScientistTasteSkill:
    def __init__(self):
        self.evaluator = TasteEvaluator()

    def evaluate(self, candidate: str, scientist: str = "einstein") -> dict:
        ev = self.evaluator.evaluate_single(candidate, scientist)
        return {"scientist": ev.scientist_name, "score": ev.overall_score,
                "axes": [{"name": s.axis_name, "score": s.score} for s in ev.axis_scores]}

    def group_evaluate(self, candidate: str, level: str = "classical") -> str:
        ge = self.evaluator.evaluate_group(candidate, level=level)
        return format_group(ge)

    def compare(self, candidate: str, scientists: list[str] | None = None) -> str:
        ge = self.evaluator.evaluate_group(candidate, scientist_ids=scientists)
        return format_comparison_table(ge)

    def list_scientists(self) -> list[dict]:
        return [{"id": p.id, "name": p.name, "name_cn": p.name_cn, "field": p.field, "level": p.level}
                for p in ALL_PROFILES.values()]
