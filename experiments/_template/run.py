"""Template run script: config.json in, primitives out. Copy and adapt.

Stages: ``pilot`` (a handful of samples to exercise the pipeline; its data
never enters the analysis), ``run`` (the preregistered N), ``analyze`` (the
preregistered analysis, run first and unmodified; anything else is labelled
exploratory).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
REPO = OUT.parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from primitives.config import ExperimentConfig  # noqa: E402


def stage_pilot(cfg: ExperimentConfig) -> None:
    pilot = cfg.replace(n_samples=min(cfg.n_samples, 5))
    print(f"pilot: {pilot.n_samples} samples from {pilot.dataset} (excluded from analysis)")


def stage_run(cfg: ExperimentConfig) -> None:
    if not (OUT / "PREREGISTRATION.md").exists():
        sys.exit("no PREREGISTRATION.md — run /preregister and commit it first")
    print(f"run: {cfg.n_samples} samples, seed {cfg.seed}")


def stage_analyze(cfg: ExperimentConfig) -> None:
    print("analyze: the statistic, interval and threshold from PREREGISTRATION.md §4")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["pilot", "run", "analyze"], required=True)
    args = ap.parse_args()
    cfg = ExperimentConfig.load(OUT / "config.json")
    cfg.save()  # stamp the config into cfg.out_dir on run start
    {"pilot": stage_pilot, "run": stage_run, "analyze": stage_analyze}[args.stage](cfg)


if __name__ == "__main__":
    main()
