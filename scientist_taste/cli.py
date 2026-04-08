"""CLI for multi-scientist taste evaluation."""

import json
import click
from scientist_taste.core.evaluator import TasteEvaluator
from scientist_taste.utils.formatting import format_single, format_group


@click.group()
@click.version_option(version="0.1.0")
def main():
    """Multi-Scientist Research Taste Evaluation System."""
    pass


@main.command()
@click.argument("candidate")
@click.option("--scientist", "-s", default="einstein", help="Scientist profile ID")
def evaluate(candidate: str, scientist: str):
    """Evaluate through a single scientist's taste."""
    ev = TasteEvaluator().evaluate_single(candidate, scientist)
    click.echo(format_single(ev))


@main.command()
@click.argument("candidate")
@click.option("--level", "-l", default="classical", help="Level: classical, nobel, pi")
def group(candidate: str, level: str):
    """Evaluate through a group of scientists."""
    ge = TasteEvaluator().evaluate_group(candidate, level=level)
    click.echo(format_group(ge))


@main.command(name="list")
def list_scientists():
    """List all available scientist profiles."""
    from scientist_taste.config.profiles import ALL_PROFILES
    for p in ALL_PROFILES.values():
        click.echo(f"  {p.id:12s} {p.name_cn} ({p.name}) [{p.level}] - {p.field}")


if __name__ == "__main__":
    main()
