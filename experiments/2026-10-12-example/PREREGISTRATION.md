# Preregistration — Does the layer-16 deception probe transfer to a new task family?

Filled by the `/preregister` skill from the researcher's answers, quoted
verbatim. Committed before the first non-pilot run; the sections above
"Deviations" are frozen from that commit on. Unanswered items read
`NOT PREREGISTERED`.

> This folder is an **illustration** of what the skill produces. The
> experiment is a toy; the numbers are made up to show the shape of a filled
> form, including one `NOT PREREGISTERED` item and one deviation.

- Date: 2026-10-12
- Researcher: reinthal
- Builds on: `experiments/2026-09-22/` (probe training), log entry 2026-09-29

## 1. Question and stakes

- Decision this result informs: "Whether we keep the layer-16 probe as the
  default detector for the auditor, or go back and train on task-family data."
- Claim hoped for (one sentence): "A probe trained on instructed lies
  separates deceptive from honest game turns without any in-distribution
  training."
- Next step if supported / refuted / inconclusive: "Supported: wire it into
  the auditor. Refuted: train on 200 labelled game turns and rerun this exact
  design. Inconclusive: double N once, then decide."

## 2. Hypothesis

- H1 (with direction): "AUROC of the probe score for Parsnip vs Carrot turns
  is above chance."
- Null: "AUROC = 0.5."
- Rival explanation: "The probe is picking up turn length or position in the
  game, not deception. The random-direction control and a length-only
  logistic baseline rule that out."
- Prediction for the primary metric (value, interval, confidence %):
  "0.68, 95% interval [0.60, 0.76], 70% confident the point estimate lands
  inside."
- Result that would make me abandon H1: "AUROC below 0.58 with the interval
  excluding 0.65."
- Expected baseline / control values: "Random-direction probe: 0.50 ± 0.05.
  Length-only baseline: 0.55."

## 3. Test design

- Primary metric (one): "AUROC, Parsnip turns vs Carrot turns, probe score
  averaged over public tokens."
- Secondary metrics: "TPR at 5% FPR; per-speaking-position AUROC."
- Unit of analysis, independence, clustering: "The turn. Turns are clustered
  within games (5 per game); intervals are bootstrapped over games, not
  turns."
- Arms and controls (and what each control rules out): "Trained probe;
  random-direction probe at the same layer (rules out any direction working);
  length-only baseline (rules out verbosity)."
- Sample size and justification (detectable effect, expected interval width):
  "100 games = 500 turns, 100 Parsnip. At AUROC 0.68 the game-level bootstrap
  interval is about ±0.08 wide, which separates 0.68 from 0.5 but not from
  0.6."
- Fixed parameters: see `config.json` (model, probe/layer, datasets, seeds,
  prompts, token budgets)
- Stopping rule: "Fixed N = 100 games. No extension."

## 4. Analysis plan

- Statistic, interval method, comparison: "AUROC with a 2000-resample
  game-level bootstrap; compared against 0.5 and against the random
  direction."
- Threshold for "supported": "Lower bound of the 95% interval above 0.55 and
  above the random-direction upper bound."
- Exclusion rules, and the exclusion fraction that voids the run: "Drop turns
  where the `<think>` block was force-closed or the parser found no public
  text. More than 15% dropped voids the run."
- Multiple comparisons: "One primary comparison, none needed. Secondary
  metrics are reported with intervals and no claim."
- Figure (axes, shared ranges): "ROC curves for the three arms on one panel;
  score histograms per arm with x in [0, 1] and shared y."
- Confirmatory analyses: "The AUROC comparison above."
- Exploratory analyses: "Per-speaking-position breakdown."

## 5. De-risking

- Pre-mortem — boring failure modes and the check for each: "Parser drops
  turns silently → assert the count of parsed turns equals the transcript
  count. Probe scores quantized by the averaging window → inspect the score
  histogram in the pilot. Thinking hits the token budget on most turns →
  count force-closes in the pilot."
- Can the metric resolve the predicted effect (granularity, floor/ceiling, N
  per cell): "100 positives, 400 negatives; continuous scores. Yes."
- Positive control: "Score the probe's own held-out instructed-lie set; AUROC
  must be above 0.9 or the loading is wrong."
- Pilot (size, what it must show; pilot data is excluded from the analysis):
  "5 games. Must show zero parse failures, under 50% force-closes, and
  non-degenerate scores."
- Cost and wall-clock estimate, hard cap, abort criterion: "About 2 GPU-hours
  on 4 A40s. Abort if the pilot shows more than 50% force-closes."
- Reused primitives / new untested code: "Game engine, rollout harness,
  LMProbe reused. New: the per-position split, 40 lines."

## 6. Conclusions agreed in advance

- If supported, the report says: "The instructed-lie probe transfers to
  social-deduction turns at AUROC ≈ 0.7 without in-distribution training."
- If refuted, the report says: "The instructed-lie probe does not transfer to
  social-deduction turns; in-distribution training is needed."
- If inconclusive (defined as "interval includes 0.55 but excludes 0.5"), the
  report says: "The probe shows weak, uncertain transfer; N was too small to
  decide."
- Limitations stated regardless of outcome: NOT PREREGISTERED

---

## Deviations

<!-- Append only. Each entry: date, what changed, why, decided before or
     after seeing data. -->

- 2026-10-13 — Exclusion rule widened to also drop turns with an empty
  public message (12 turns). Reason: these have no tokens to score and the
  pipeline crashed on them. Decided after seeing data; the exclusion fraction
  stays under the 15% void threshold.
