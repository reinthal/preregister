"""ExperimentConfig: the one place an experiment's hyperparameters live.

Every `experiments/<date>/` carries a `config.json` that reproduces the run.
Scripts load it, never hardcode values, and call `save()` on run start so the
folder records exactly what ran. Subclass to add experiment-specific fields.
"""
from __future__ import annotations

import dataclasses
import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ExperimentConfig:
    model_id: str
    layer: int
    probe_path: str
    dataset: str
    n_samples: int
    seed: int
    temperature: float
    max_new_tokens: int
    out_dir: str
    extra: dict = field(default_factory=dict)

    @classmethod
    def load(cls, path: str | Path) -> "ExperimentConfig":
        raw = json.loads(Path(path).read_text())
        known = {f.name for f in dataclasses.fields(cls)}
        unknown = set(raw) - known
        if unknown:
            raise KeyError(f"{path}: unknown config keys {sorted(unknown)}")
        return cls(**raw)

    def save(self, out_dir: str | Path | None = None) -> Path:
        out = Path(out_dir or self.out_dir)
        out.mkdir(parents=True, exist_ok=True)
        path = out / "config.json"
        path.write_text(json.dumps(dataclasses.asdict(self), indent=2) + "\n")
        return path

    def replace(self, **changes) -> "ExperimentConfig":
        return dataclasses.replace(self, **changes)
