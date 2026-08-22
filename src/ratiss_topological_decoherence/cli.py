"""Command line entry point for the local demonstration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .simulation import run_local_demo
from .studio_import import run_studio_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a local RATISS topological-decoherence timeline.")
    parser.add_argument("--output", default="artifacts/full_timeline.json", help="Destination JSON path.")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--studio-input", help="Quantum Circuit Studio v0.1 JSON document to compile and simulate internally.")
    source.add_argument("--statevector-input", help="External Qiskit-compatible statevector trajectory JSON to import locally.")
    source.add_argument("--counts-input", help="External Qiskit counts trajectory JSON to normalize as a declared classical association.")
    source.add_argument("--photon-input", help="External photonic mode-distribution trajectory JSON to normalize locally.")
    source.add_argument("--bio-input", help="External normalized bio correlation-matrix trajectory JSON to normalize locally.")
    args = parser.parse_args()
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if args.studio_input:
        document = run_studio_file(args.studio_input)
    elif args.statevector_input:
        from .external_statevector import run_qiskit_statevector_file
        document = run_qiskit_statevector_file(args.statevector_input)
    elif args.counts_input:
        from .correlation_import import run_qiskit_counts_file
        document = run_qiskit_counts_file(args.counts_input)
    elif args.photon_input:
        from .correlation_import import run_photonic_mode_file
        document = run_photonic_mode_file(args.photon_input)
    elif args.bio_input:
        from .correlation_import import run_bio_correlation_file
        document = run_bio_correlation_file(args.bio_input)
    else:
        document = run_local_demo()
    destination.write_text(json.dumps(document, indent=2), encoding="utf-8")
    print(f"Wrote {destination} ({len(document['steps'])} timeline steps).")


if __name__ == "__main__":
    main()
