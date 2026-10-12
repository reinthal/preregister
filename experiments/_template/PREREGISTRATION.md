# Preregistration — <experiment title>

Filled by the `/preregister` skill from the researcher's answers, quoted
verbatim. Committed before the first non-pilot run; the sections above
"Deviations" are frozen from that commit on. Unanswered items read
`NOT PREREGISTERED`.

- Date:
- Researcher:
- Builds on: <experiments/<date>/, log entries>

## 1. Question and stakes

- Decision this result informs:
- Claim hoped for (one sentence):
- Next step if supported / refuted / inconclusive:

## 2. Hypothesis

- H1 (with direction):
- Null:
- Rival explanation:
- Prediction for the primary metric (value, interval, confidence %):
- Result that would make me abandon H1:
- Expected baseline / control values:

## 3. Test design

- Primary metric (one):
- Secondary metrics:
- Unit of analysis, independence, clustering:
- Arms and controls (and what each control rules out):
- Sample size and justification (detectable effect, expected interval width):
- Fixed parameters: see `config.json` (model, probe/layer, datasets, seeds,
  prompts, token budgets)
- Stopping rule:

## 4. Analysis plan

- Statistic, interval method, comparison:
- Threshold for "supported":
- Exclusion rules, and the exclusion fraction that voids the run:
- Multiple comparisons:
- Figure (axes, shared ranges):
- Confirmatory analyses:
- Exploratory analyses:

## 5. De-risking

- Pre-mortem — boring failure modes and the check for each:
- Can the metric resolve the predicted effect (granularity, floor/ceiling, N per cell):
- Positive control:
- Pilot (size, what it must show; pilot data is excluded from the analysis):
- Cost and wall-clock estimate, hard cap, abort criterion:
- Reused primitives / new untested code:

## 6. Conclusions agreed in advance

- If supported, the report says:
- If refuted, the report says:
- If inconclusive (defined as ...), the report says:
- Limitations stated regardless of outcome:

---

## Deviations

<!-- Append only. Each entry: date, what changed, why, decided before or
     after seeing data. -->
