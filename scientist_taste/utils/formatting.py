"""Formatting utilities for multi-scientist evaluations."""

from scientist_taste.core.evaluator import SingleEvaluation, GroupEvaluation


def format_single(ev: SingleEvaluation) -> str:
    lines = [
        f"--- {ev.scientist_name} ---",
        f"Overall: {ev.overall_score:+.2f} (conf: {ev.overall_confidence:.2f})",
    ]
    for s in sorted(ev.axis_scores, key=lambda x: x.score, reverse=True)[:5]:
        tag = "EVIDENCE" if s.is_evidence_based else "INFERRED"
        lines.append(f"  {s.axis_name:25s} {s.score:+.2f} [{tag}]")
    return "\n".join(lines)


def format_group(ge: GroupEvaluation) -> str:
    lines = [
        "=" * 60,
        f"SCIENTIST TASTE GROUP EVALUATION",
        f"Candidate: {ge.candidate[:80]}",
        "=" * 60, "",
    ]
    for ev in sorted(ge.evaluations, key=lambda e: e.overall_score, reverse=True):
        lines.append(format_single(ev))
        lines.append("")
    lines.append(f"Synthesis: {ge.synthesis}")
    return "\n".join(lines)


def format_comparison_table(ge: GroupEvaluation) -> str:
    lines = [f"| Scientist | Score | Top Axis |"]
    lines.append("|-----------|-------|----------|")
    for ev in sorted(ge.evaluations, key=lambda e: e.overall_score, reverse=True):
        top = max(ev.axis_scores, key=lambda s: s.score) if ev.axis_scores else None
        top_str = f"{top.axis_name} ({top.score:+.2f})" if top else "N/A"
        lines.append(f"| {ev.scientist_name} | {ev.overall_score:+.2f} | {top_str} |")
    return "\n".join(lines)
