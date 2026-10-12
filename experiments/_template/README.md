# Experiment template

Copy this folder to `experiments/<date>-<slug>/`, edit `config.json`, and write
the stages of `run.py`. The contract:

- **`PREREGISTRATION.md` comes first.** Run the `/preregister` skill; it fills
  the form from the researcher's answers. Commit it before the first
  non-pilot run; later changes go under its "Deviations" heading.
- **`config.json` is the single place hyperparameters live.** Scripts read
  `ExperimentConfig` (or a subclass adding experiment-specific fields) and
  build everything from it — no constants scattered across scripts.
  `cfg.save()` on run start stamps the config that actually ran.
- **Primitives come from the packages** (see AGENTS.md "Reuse, don't
  rebuild"), not from copies inside the experiment folder.
- Log every run in `research-log/log.md`; state design + deliberate
  limitations in the experiment README.

Run:

```
uv run python experiments/<date>/run.py --stage pilot    # 1-5 samples, excluded from analysis
uv run python experiments/<date>/run.py --stage run      # only after PREREGISTRATION.md is committed
uv run python experiments/<date>/run.py --stage analyze  # the preregistered analysis, unmodified
```
