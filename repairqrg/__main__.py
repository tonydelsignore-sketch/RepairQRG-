"""Entry point for ``python -m repairqrg``."""

from .cli import main


if __name__ == "__main__":  # pragma: no cover - delegated to CLI
    raise SystemExit(main())
