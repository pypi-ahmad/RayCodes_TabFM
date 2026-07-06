<div align="center">
  <a href="https://youtu.be/8QEAUtSoVgA">
    <img src="https://img.youtube.com/vi/8QEAUtSoVgA/0.jpg" alt="Google TabFM: Fast Tabular Predictions Running Locally!">
  </a>
  <h3><a href="https://youtu.be/8QEAUtSoVgA">Watch the full tutorial on YouTube</a></h3>
</div>

# TabFM + Ollama Analyzer

Zero-shot tabular predictions with Google TabFM (PyTorch backend), plus local Ollama summaries.

## What this app includes

- CSV Upload mode: one training CSV + one test CSV.
- Batch Upload mode: one training CSV + multiple test CSVs.
- Ollama model selector dropdown from local `/api/tags`.
- PDF export for insights.
- Plotly charts for prediction distribution and confidence.

## Tech stack

- Core ML: `TabFM` (PyTorch)
- Local LLM: `Ollama`
- Frontend: `Streamlit`
- Data: `pandas`, `numpy`
- Visualization: `plotly`
- PDF export: `reportlab`

## Setup

1. Install TabFM (official repo)

```bash
git clone https://github.com/google-research/tabfm.git
cd tabfm
uv pip install -e .[pytorch]
cd ..
```

2. Install this app dependencies

```bash
uv pip install -r requirements.txt
```

3. Pull at least one Ollama model

```bash
ollama pull qwen3:4b
```

4. Run app

```bash
streamlit run app.py --server.fileWatcherType none
```

## Usage

### CSV Upload

- Upload training CSV (must include target column).
- Upload test CSV (same feature columns as training CSV minus target).
- Select target column.
- Click `Run Prediction & Analyze`.

Outputs:
- TabFM predictions with confidence.
- Plotly charts.
- Ollama insight text.
- `outputs.md` snapshot.
- Downloadable PDF report.

### Batch Upload

- Upload one training CSV.
- Upload multiple test CSV files.
- Select target column.
- Click `Run Batch Prediction`.

Outputs:
- Per-file status table.
- Downloadable prediction CSV for each successful file.
- Aggregate prediction chart.
- Batch insight text.
- `outputs.md` snapshot.
- Downloadable batch PDF report.

## Why runs can take time

TabFM uses an ensemble-based in-context inference flow. The biggest avoidable slowdown in app logic is calling both `predict` and `predict_proba` in the same run. This app uses a single `predict_proba` pass and derives predicted labels from it, so inference is not duplicated.

## Quick TabFM sanity check

```bash
python3 -c "from tabfm import tabfm_v1_0_0_pytorch as b; b.load(); print('TabFM OK')"
```

## References

- Tutorial video: https://youtu.be/8QEAUtSoVgA
- Google Research blog: https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/
- TabFM repository: https://github.com/google-research/tabfm
- TabFM classifier internals: https://raw.githubusercontent.com/google-research/tabfm/main/tabfm/src/classifier_and_regressor.py
- Ollama API tags endpoint: https://docs.ollama.com/api/tags
