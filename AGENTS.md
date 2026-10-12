# Agent instructions for this repo

Example research repo showing how the `/preregister` skill
(`.claude/skills/preregister/`) fits an experiment workflow. Read
`research-log/log.md` for what has been run and why.

**No defensive programming without explicit instruction.** No fallback code
paths, lenient parsing, or silent error recovery "just in case" — fail loudly
on unexpected input. If a fallback seems genuinely needed, propose it and let
the researcher decide.

## Reuse, don't rebuild

- `primitives/config.py::ExperimentConfig` — the ONE place an experiment's
  hyperparameters live. Each `experiments/<date>/` carries a `config.json`
  that reproduces the run (`cfg.save()` on run start); subclass it to add
  fields. Put further shared primitives (model wrappers, generation
  backends, environments) in packages here and import them from experiments;
  never copy code into an experiment folder.

## Conventions

- New experiments go in `experiments/<date>-<slug>/` with a README stating
  design and deliberate limitations; log every run in `research-log/log.md`
  (Claude fills Context/Experiment/Parameters/Artifacts; Expected/Actual
  Outcome are the researcher's). Skeleton: `experiments/_template/`.
- **Preregister before running**: a new experiment starts with the
  `/preregister` skill (`.claude/skills/preregister/`), which interrogates the
  researcher and writes `experiments/<date>/PREREGISTRATION.md` (hypothesis,
  prediction, primary metric, analysis plan, exclusions, de-risking,
  pre-agreed conclusions). It is committed before the first non-pilot run and
  its frozen sections are never edited afterwards — changes are appended
  under "Deviations". The answers are the researcher's, recorded verbatim.
  Pilot runs (1-5 samples) may precede the commit; their data never enters
  the analysis.
- Every experiment folder carries a `config.json` (an `ExperimentConfig`,
  possibly subclassed) holding ALL of the run's hyperparameters — scripts
  read it, never hardcode.
- After the run: the preregistered analysis runs first and unmodified;
  anything else is reported under an "Exploratory" heading. The log entry's
  Results put prediction and outcome side by side and use the pre-agreed
  conclusion sentence.
- **Figures: panels meant to be compared share identical axis ranges.**
- `CLAUDE.md` is a symlink to this file.
