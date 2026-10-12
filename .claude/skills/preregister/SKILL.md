---
name: preregister
description: Interrogate the researcher and freeze a preregistration before a new experiment, then hold the analysis and report to it. Use when the researcher proposes a new experiment, asks to plan or scaffold a run, says "preregister", or before creating experiments/<date>/ or launching any non-pilot run that has no PREREGISTRATION.md.
---

# Preregister an experiment

Flow: **preregister → hypothesis → test → analyze → report with conclusion**.
Your job in the first half is to interrogate the researcher until every
choice that could later be bent toward the result is written down, and to
find the boring reasons the run could fail before it costs GPU-hours or API
budget. In the second half you hold the analysis and the report to what was
written.

The output is `experiments/<date>/PREREGISTRATION.md` (form:
`experiments/_template/PREREGISTRATION.md`), committed before the first
non-pilot run.

## Rules

- **Interrogate, don't author.** Predictions, thresholds, exclusion rules and
  conclusion sentences are the researcher's. Record them verbatim. You may
  lay out options and say what each would cost; you never fill an answer in
  yourself. This is the same rule as the research log's Expected/Actual
  Outcome.
- **Prepare first.** Read `research-log/log.md` and the README, config and
  results of the experiments this one builds on, so questions carry the
  actual numbers ("suspicion AUROC was 0.735 on 94 trajectories — what do
  you expect here, and why would it move?"). Do not ask what the repo
  already answers.
- **Ask in rounds.** One stage at a time, 2-4 questions per round, using
  AskUserQuestion when the answer is a choice and plain questions when it is
  a number or a sentence. Later questions depend on earlier answers; do not
  dump the whole list.
- **Push back on vague answers.** "It should be better" is not a prediction.
  Ask for a direction, a number, an interval and a confidence. Ask once more;
  if the researcher still declines, record it as below.
- **Nothing is silently skipped.** An item the researcher does not answer is
  written as `NOT PREREGISTERED`. Whatever is decided about it later is
  exploratory.
- **Say when the design cannot answer the question.** If the planned N, the
  score granularity or the controls cannot distinguish the hypothesis from
  its rival, say so plainly before the run rather than after.
- **Gate.** No non-pilot run until the form is written and the researcher has
  committed it (or asked you to). The commit is the timestamp. Pilots are
  allowed before that, and their data never enters the analysis.

## Line of questioning

Skip a question only when the repo or an earlier answer already settles it.

### 1. Question and stakes

- What decision changes depending on the result? If none, why run it?
- What is the one-sentence claim you hope to make afterwards?
- What do you do next under each outcome?

### 2. Hypothesis

- State H1 with its direction, and the null.
- What is the most plausible rival explanation for the result you expect?
- Give a numeric prediction for the primary metric, an interval, and your
  confidence in percent.
- What result would make you abandon the hypothesis? If no result would,
  this is not a test — say so.
- What do you expect each baseline and control to show?

### 3. Test design

- Primary metric: exactly one. Everything else is secondary or exploratory.
- Unit of analysis, and what is independent (game, task, trajectory, epoch,
  seed). What is clustered within what?
- Arms and controls (benign control, random-direction probe, coef 0, honest
  mode), and what each control rules out.
- Sample size and the reason for it: what effect size can this N detect, and
  how wide will the interval be?
- Model, probe and layer, datasets, seeds, prompts, token budgets — fixed now
  and written to `config.json`.
- Stopping rule: a fixed N, or the exact condition for stopping or extending.

### 4. Analysis plan

- The exact statistic, the interval method, the comparison, and the threshold
  for calling the hypothesis supported.
- Exclusion rules, decided now: faulty tasks, parse failures, force-closed
  `<think>` blocks, truncated trajectories, provider errors. What fraction of
  exclusions voids the run?
- How many arms and metrics are compared, and is there a correction?
- Which figure will be drawn? Fix the axes now; panels meant to be compared
  share ranges.
- Which analyses are confirmatory and which exploratory?

### 5. De-risking

- Pre-mortem: suppose the run failed for a boring reason. What was it?
  Prompt with the project's own history of failures — a parser fallback, a
  message or context limit capping the score, quantized scores, a shared GPU
  being occupied, OOM at long contexts, thinking hitting the token budget,
  provider errors, the cost cap.
- Can the metric resolve the predicted effect at all? Check score granularity
  against the FPR budget, floor and ceiling effects, and N per cell.
- Positive control: does the pipeline detect an effect known to be there?
- What pilot (1-5 samples) exercises the pipeline end to end, and what must
  it show before scaling?
- Cost and wall-clock estimate, the hard cap, and the abort criterion
  mid-run.
- Which existing primitives are reused (AGENTS.md "Reuse, don't rebuild", if the project has one),
  and which code is new and untested?

### 6. Report and conclusion, agreed in advance

- The conclusion sentence for each outcome — supported, refuted,
  inconclusive — written now.
- What counts as inconclusive, and what happens then?
- Which limitations will be stated whatever the outcome?

## Writing the form

Copy `experiments/_template/PREREGISTRATION.md` into the experiment folder
and fill it from the answers, quoting the researcher. Show it to them, apply
their corrections, and stop there: the run starts after it is committed.
Quote the prediction into the research-log entry's *Expected Outcome*.

## After the run

- **Analyze.** Run the preregistered analysis first and unmodified. Anything
  else goes under an "Exploratory" heading in the results, labelled as such.
- **Deviations.** Never edit the frozen sections. Append to "Deviations":
  what changed, why, and whether it was decided before or after seeing data.
- **Report.** In the log entry's Results, put prediction and outcome side by
  side, apply the pre-agreed threshold, and use the pre-agreed conclusion
  sentence for the outcome that occurred. If the result is inconclusive by
  the preregistered rule, report it as inconclusive. *Actual Outcome* is the
  researcher's: ask them for it, do not write it.
