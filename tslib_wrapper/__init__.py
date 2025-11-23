"""
Lightweight wrapper to run TSLib experiments programmatically without modifying
the original codebase. This keeps fork maintenance easy while enabling
library-style usage.
"""

from .api import build_parser, run_experiment, run_experiment_from_namespace

__all__ = ["build_parser", "run_experiment", "run_experiment_from_namespace"]
