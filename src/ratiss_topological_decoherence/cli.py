"""Command line entry point for the local demonstration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .simulation import run_local_demo


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a local RATISS topological-decoherence timeline.")
    parser.add_argument("--output", default="artifacts/full_timeline.json", help="Destination JSON path.")
    args = parser.parse_args()
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    document = run_local_demo()
    destination.write_text(json.dumps(document, indent=2), encoding="utf-8")
    print(f"Wrote {destination} ({len(document['steps'])} timeline steps).")


if __name__ == "__main__":
    main()
