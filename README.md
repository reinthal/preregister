# preregister

A [Claude Code](https://claude.com/claude-code) skill that makes the agent
**interrogate the researcher and freeze a preregistration before a new
experiment**, then hold the analysis and the report to what was written —
packaged inside a minimal example research repo that shows where it fits.

Flow: **preregister → hypothesis → test → analyze → report with conclusion**.

The agent asks in rounds (question and stakes, hypothesis, test design,
analysis plan, de-risking, pre-agreed conclusions), records the researcher's
answers verbatim, writes `experiments/<date>/PREREGISTRATION.md` from the
form in `experiments/_template/`, and refuses to start a non-pilot run until
it is committed. After the run it runs the preregistered analysis first,
appends changes under "Deviations" instead of editing frozen sections, and
reports prediction and outcome side by side using the pre-agreed conclusion
sentence.

## Repo layout (the illustration)

```
.claude/skills/preregister/SKILL.md      the skill
AGENTS.md  (CLAUDE.md -> AGENTS.md)      agent instructions wiring the skill into the workflow
experiments/_template/                   skeleton: PREREGISTRATION.md form, config.json, run.py, README
experiments/2026-10-12-example/          a filled-in preregistration (toy experiment) + matching config
research-log/log.md, template.md         the log the skill quotes predictions into
primitives/config.py                     ExperimentConfig: config.json in, cfg.save() on run start
pyproject.toml, uv.lock                  the uv project the scripts run under
```

Read `AGENTS.md`, then `experiments/_template/README.md`, then the example
folder. `research-log/log.md` shows how a preregistered experiment is logged:
*Expected Outcome* quotes the prediction, *Actual Outcome* is the
researcher's.

## Install the skill in your own repo

With the [`skills`](https://github.com/vercel-labs/skills) CLI:

```sh
npx skills add reinthal/preregister
```

Or copy by hand:

```sh
git clone https://github.com/reinthal/preregister
mkdir -p .claude/skills experiments/_template research-log
cp -r preregister/.claude/skills/preregister .claude/skills/
cp preregister/experiments/_template/PREREGISTRATION.md experiments/_template/
cp preregister/research-log/template.md research-log/
```

Then add the "Preregister before running" convention from `AGENTS.md` to your
own agent instructions, and `/preregister` in Claude Code (it also triggers
when you propose an experiment, ask to scaffold a run, or try to launch a
non-pilot run with no `PREREGISTRATION.md`).

## Try it here

```sh
uv sync
uv run python experiments/_template/run.py --stage pilot
uv run python experiments/2026-10-12-example/run.py --stage run
```

## Adapting

The skill assumes experiments live in `experiments/<date>/` with a
`config.json` holding every hyperparameter, and a research log with
Expected/Actual Outcome fields owned by the researcher. Edit the paths in
`SKILL.md` if your project differs. The pre-mortem list in section 5 is a
prompt, not a checklist: replace the examples with your own project's past
failures.

## Origin

Extracted from `reinthal/downstream-environment` (deception-probe research).
