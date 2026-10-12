# Research log

<!-- Entry format: research-log/template.md. Expected/Actual Outcome are the
     researcher's to write — Claude fills Context/Experiment/Parameters/Artifacts
     only. A preregistered experiment's Expected Outcome quotes the
     prediction from its PREREGISTRATION.md. -->

## 2026-10-12 — probe transfer to game turns (illustration)

### Context

Toy entry showing how a preregistered experiment is logged. The probe from
`experiments/2026-09-22/` was trained on instructed lies; the auditor needs
it to work on social-deduction turns it never saw.

### Experiment

Score 500 game turns (100 games) with the layer-16 probe, a random-direction
probe and a length-only baseline; compare AUROC for Parsnip vs Carrot turns.
Preregistered in `experiments/2026-10-12-example/PREREGISTRATION.md`.

### Expected Outcome

From the preregistration: "0.68, 95% interval [0.60, 0.76], 70% confident the
point estimate lands inside." Abandon H1 if "AUROC below 0.58 with the
interval excluding 0.65."

### Actual Outcome

<researcher to fill — prediction and outcome side by side, the preregistered
threshold applied, the pre-agreed conclusion sentence for the outcome that
occurred>

### Parameters/Configurations

`experiments/2026-10-12-example/config.json`. Run with
`uv run python experiments/2026-10-12-example/run.py --stage run`.

### Artifacts

- `experiments/2026-10-12-example/PREREGISTRATION.md`
- `experiments/2026-10-12-example/README.md`
