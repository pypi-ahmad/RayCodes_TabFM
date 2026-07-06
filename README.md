<div align="center">
  <a href="https://youtu.be/8QEAUtSoVgA">
    <img src="https://img.youtube.com/vi/8QEAUtSoVgA/0.jpg" alt="Google TabFM: Fast Tabular Predictions Running Locally!">
  </a>
  <h3>📺 <a href="https://youtu.be/8QEAUtSoVgA">Watch the full tutorial on YouTube</a></h3>
</div>

# 📊 TabFM + Ollama Analyzer

> **Zero-Shot Tabular Predictions & Local LLM Insights** 🧠⚡

A visually streamlined, end-to-end tool blending **TabFM** (Tabular Foundation Model) and **Ollama** (`qwen3:4b`). Input data, get predictions instantly, and receive AI-driven summaries—no dataset training required. This repository acts as an interface and wrapper for Google's TabFM, ensuring fast tabular predictions running 100% locally.

---

## 🛠️ Tech Stack
*   🧠 **Core ML:** `TabFM` (PyTorch)
*   🤖 **Local LLM:** `Ollama` (`qwen3:4b`)
*   🖥️ **Frontend:** `Streamlit`
*   💾 **Data:** `pandas` & `numpy`
*   📈 **Charts:** `plotly`
*   🖨️ **PDF Export:** `reportlab`

## 📂 Files
*   📄 **`README.md`**: Project overview and setup.
*   🐍 **`app.py`**: Streamlit UI, TabFM engine, and Ollama integration.
*   📦 **`requirements.txt`**: Python dependencies.
*   📝 **`outputs.md`**: Auto-generated markdown log of latest predictions and insights.

---

## 🚀 Setup & Execution

Copy-paste these commands directly into terminal (PowerShell/Bash):

**1. Install Core Dependencies**
```bash
git clone https://github.com/google-research/tabfm.git
cd tabfm
pip install -e .[pytorch]
cd ..
pip install -r requirements.txt
ollama pull qwen3:4b
```

**2. Run Application**
```bash
streamlit run app.py
```

If Streamlit watcher causes reload issues in your environment:
```bash
streamlit run app.py --server.fileWatcherType none
```

**3. Quick Test (Headless)**
```bash
python3 -c "from tabfm import tabfm_v1_0_0_pytorch as b; b.load(); print('TabFM loaded successfully')"
```

---

## ✅ Implemented Upgrades
1. 📁 **Batch Upload:** CSV support for bulk processing.
2. 🎛️ **Model Selector:** UI dropdown for discovered local Ollama models.
3. 🖨️ **PDF Export:** Download AI insights instantly.
4. 📈 **Dynamic Charts:** Plotly visual metrics for predictions and confidence.

## 📁 Usage Modes

### CSV Upload
- Upload 1 training CSV (includes target column) and 1 test CSV.
- Select target column and run prediction.
- Get predictions, confidence, charts, Ollama insight, and PDF export.

### Batch Upload
- Upload 1 training CSV and multiple test CSV files.
- Fit once and predict each test file.
- Download per-file predictions and batch PDF summary.

---

## 🎯 5 Core Use Cases
1. 🏦 **Risk Assessment:** Instantly predict credit risk based on mixed tabular data.
2. 🏡 **Real Estate Valuation:** Zero-shot regression on property features for pricing.
3. 📉 **Customer Churn:** Identify subscription cancellations from usage data.
4. 🏥 **Medical Triage:** Classify patient risk levels from health records.
5. 📦 **Inventory Forecasting:** Predict stock needs using historical inputs.

## 🔗 References
- Tutorial video: https://youtu.be/8QEAUtSoVgA
- Google Research blog: https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/
- TabFM repository: https://github.com/google-research/tabfm
- TabFM classifier internals: https://raw.githubusercontent.com/google-research/tabfm/main/tabfm/src/classifier_and_regressor.py
- Ollama API tags endpoint: https://docs.ollama.com/api/tags

---

**SEO Keywords:** Google TabFM, Tabular Foundation Model, Local LLM, Ollama, Qwen3, Streamlit AI interface, zero-shot tabular predictions, offline AI inference, Python tabular analysis, data science automation.
