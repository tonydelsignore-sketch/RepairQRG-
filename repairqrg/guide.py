"""Core classes for interacting with the repair quick reference guide."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence

from .data import (
    RepairCategory,
    RepairProcedure,
    build_sample_catalog,
    flatten_procedures,
)


@dataclass
class QuickReferenceGuide:
    """Provide convenient lookup helpers for repair procedures."""

    catalog: Dict[str, RepairCategory]

    @classmethod
    def from_sample_catalog(cls) -> "QuickReferenceGuide":
        """Create a quick reference guide populated with sample data."""

        return cls(build_sample_catalog())

    def list_categories(self) -> Sequence[str]:
        """Return all known category keys sorted alphabetically."""

        return sorted(self.catalog.keys())

    def get_category(self, key: str) -> Optional[RepairCategory]:
        """Return a category by its identifier."""

        return self.catalog.get(key.lower())

    def list_procedures(self, key: str) -> Sequence[RepairProcedure]:
        """Return all repair procedures stored under a category."""

        category = self.get_category(key)
        return list(category.procedures) if category else []

    def find_procedures(self, phrase: str) -> Sequence[RepairProcedure]:
        """Return procedures whose name or summary contains the phrase."""

        if not phrase:
            return []

        phrase_lower = phrase.lower()
        results: List[RepairProcedure] = []
        for procedure in flatten_procedures(self.catalog):
            if phrase_lower in procedure.name.lower() or phrase_lower in procedure.summary.lower():
                results.append(procedure)
        return results

    def describe_procedure(self, procedure: RepairProcedure) -> str:
        """Create a formatted summary of the provided procedure."""

        lines: List[str] = []
        lines.append(f"{procedure.name} ({procedure.difficulty})")
        lines.append(procedure.summary)
        lines.append(f"Estimated time: {procedure.estimated_time}")
        if procedure.tools:
            lines.append("Tools: " + ", ".join(procedure.tools))
        if procedure.supplies:
            lines.append("Supplies: " + ", ".join(procedure.supplies))
        lines.append("")
        for idx, step in enumerate(procedure.steps, start=1):
            lines.append(f"{idx}. {step.instruction}")
            for tip in step.tips:
                lines.append(f"   - Tip: {tip}")
        if procedure.notes:
            lines.append("")
            lines.append("Notes:")
            for note in procedure.notes:
                lines.append(f" - {note}")
        return "\n".join(lines)

    def describe_category(self, key: str) -> Optional[str]:
        """Return a formatted description for a category key."""

        category = self.get_category(key)
        if not category:
            return None
        lines: List[str] = [f"{category.name}", category.overview, ""]
        for procedure in category.procedures:
            lines.append(f"- {procedure.name}: {procedure.summary}")
        return "\n".join(lines)
