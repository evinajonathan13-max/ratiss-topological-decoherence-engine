"""RATISS Topological Decoherence Engine.

Local SDK for producing traceable, topological inspection artifacts from
simulated (or explicitly imported) quantum-state trajectories.
"""

from .simulation import SimulationConfig, run_local_demo

__all__ = ["SimulationConfig", "run_local_demo"]
__version__ = "0.1.0"
