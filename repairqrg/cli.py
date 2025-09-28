"""Command line interface for the Repair Quick Reference Guide."""

from __future__ import annotations

import argparse
from typing import Sequence

from .guide import QuickReferenceGuide


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Browse procedures in the Repair Quick Reference Guide.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("categories", help="List all available categories")

    category_parser = subparsers.add_parser(
        "category", help="Show details for a category",
    )
    category_parser.add_argument("key", help="Category identifier (e.g. appliances)")

    search_parser = subparsers.add_parser(
        "search", help="Search for procedures by keyword",
    )
    search_parser.add_argument("phrase", help="Keyword or phrase to search for")

    detail_parser = subparsers.add_parser(
        "procedure", help="Show procedure details",
    )
    detail_parser.add_argument("phrase", help="Name or partial name of the procedure")

    return parser


def render_categories(guide: QuickReferenceGuide) -> str:
    items = guide.list_categories()
    return "\n".join(items) if items else "No categories found."


def render_category(guide: QuickReferenceGuide, key: str) -> str:
    description = guide.describe_category(key)
    return description or f"No category found for '{key}'."


def render_search_results(guide: QuickReferenceGuide, phrase: str) -> str:
    results = guide.find_procedures(phrase)
    if not results:
        return f"No procedures found containing '{phrase}'."

    lines = []
    for procedure in results:
        lines.append(f"{procedure.name} [{procedure.difficulty}]")
        lines.append(f"  {procedure.summary}")
    return "\n".join(lines)


def render_procedure_detail(guide: QuickReferenceGuide, phrase: str) -> str:
    results = guide.find_procedures(phrase)
    if not results:
        return f"No procedures found containing '{phrase}'."
    if len(results) == 1:
        return guide.describe_procedure(results[0])

    # If multiple matches, show a summary list to help narrow down the query.
    lines = [
        "Multiple procedures matched. Please refine your search:",
        "",
    ]
    for procedure in results:
        lines.append(f"- {procedure.name}: {procedure.summary}")
    return "\n".join(lines)


def dispatch(args: argparse.Namespace) -> str:
    guide = QuickReferenceGuide.from_sample_catalog()
    if args.command == "categories":
        return render_categories(guide)
    if args.command == "category":
        return render_category(guide, args.key)
    if args.command == "search":
        return render_search_results(guide, args.phrase)
    if args.command == "procedure":
        return render_procedure_detail(guide, args.phrase)
    raise ValueError(f"Unknown command: {args.command}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    output = dispatch(args)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
