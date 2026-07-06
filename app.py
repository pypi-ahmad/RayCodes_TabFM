import io
import textwrap
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tabfm import TabFMClassifier
from tabfm import tabfm_v1_0_0_pytorch as tabfm_v1_0_0

# Model Configuration
OLLAMA_DEFAULT_MODEL = "qwen3:4b"
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_GENERATE_URL = f"{OLLAMA_BASE_URL}/api/generate"
OLLAMA_TAGS_URL = f"{OLLAMA_BASE_URL}/api/tags"

OUTPUTS_MD_PATH = Path("outputs.md")
MAX_BATCH_FILES = 25
MAX_PREVIEW_ROWS = 200


st.set_page_config(page_title="TabFM Zero-Shot Analyzer", layout="wide", page_icon="📊")

st.title("📊 TabFM Zero-Shot Analyzer")
st.markdown(
    "Instantly predict tabular outcomes using **TabFM** (zero-shot) and generate "
    "insights using a local **Ollama** LLM without reasoning overhead."
)


@st.cache_resource
def load_tabfm():
    return tabfm_v1_0_0.load()


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def _read_uploaded_csv(uploaded_file) -> pd.DataFrame:
    return pd.read_csv(uploaded_file)


def _prepare_datasets(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    target_column: str,
) -> tuple[pd.DataFrame, np.ndarray, pd.DataFrame]:
    if train_df.empty or test_df.empty:
        raise ValueError("Train and test CSVs must contain at least one row each.")

    if target_column not in train_df.columns:
        raise ValueError(f"Target column '{target_column}' not found in training CSV.")

    y_train = train_df[target_column]
    if y_train.isna().all():
        raise ValueError("Target column is empty or all-NaN.")

    x_train = train_df.drop(columns=[target_column])
    if x_train.empty:
        raise ValueError("No feature columns remain after removing the target column.")

    if target_column in test_df.columns:
        test_df = test_df.drop(columns=[target_column])

    if set(x_train.columns) != set(test_df.columns):
        missing_in_test = sorted(set(x_train.columns) - set(test_df.columns))
        extra_in_test = sorted(set(test_df.columns) - set(x_train.columns))
        raise ValueError(
            "Feature mismatch between train and test CSVs. "
            f"Missing in test: {missing_in_test or 'None'}. "
            f"Extra in test: {extra_in_test or 'None'}."
        )

    x_test = test_df.loc[:, x_train.columns]
    return x_train, y_train.to_numpy(), x_test


def _fetch_ollama_models(tags_url: str) -> tuple[list[str], str | None]:
    try:
        response = requests.get(tags_url, timeout=5)
        if response.status_code != 200:
            return [OLLAMA_DEFAULT_MODEL], f"HTTP {response.status_code} while listing models"

        payload = response.json()
        model_names = sorted(
            {
                str(item.get("name", "")).strip()
                for item in payload.get("models", [])
                if str(item.get("name", "")).strip()
            }
        )
        if not model_names:
            return [OLLAMA_DEFAULT_MODEL], "No models returned by Ollama /api/tags"

        return model_names, None
    except Exception as e:
        return [OLLAMA_DEFAULT_MODEL], str(e)


def _call_ollama(prompt: str, model_name: str) -> tuple[bool, str | None, str | None, float]:
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.0},
    }

    start_time = time.time()
    try:
        response = requests.post(OLLAMA_GENERATE_URL, json=payload, timeout=60)
        latency = time.time() - start_time
        if response.status_code != 200:
            return False, None, f"HTTP {response.status_code}: {response.text[:240]}", latency

        text = str(response.json().get("response", "")).strip()
        if not text:
            return False, None, "Empty response payload", latency

        return True, text, None, latency
    except Exception as e:
        latency = time.time() - start_time
        return False, None, str(e), latency


def _predict_with_confidence(
    clf: TabFMClassifier,
    x_test: pd.DataFrame,
    target_column: str,
) -> pd.DataFrame:
    # One pass only: get probabilities once, then derive labels + confidence.
    probabilities = np.asarray(clf.predict_proba(x_test))
    if probabilities.ndim != 2:
        raise ValueError(f"Unexpected probability shape: {probabilities.shape}")

    pred_indices = np.argmax(probabilities, axis=1)
    predictions = np.asarray(clf.classes_)[pred_indices]

    results_df = x_test.copy()
    results_df[f"Predicted_{target_column}"] = predictions
    results_df["Confidence"] = np.max(probabilities, axis=1)
    return results_df


def _render_prediction_charts(results_df: pd.DataFrame, pred_col: str) -> None:
    counts_df = (
        results_df[pred_col]
        .value_counts()
        .rename_axis("label")
        .reset_index(name="count")
    )

    col1, col2 = st.columns(2)
    with col1:
        st.caption("Predicted class distribution")
        fig_counts = px.bar(counts_df, x="label", y="count")
        st.plotly_chart(fig_counts, use_container_width=True)

    with col2:
        st.caption("Confidence distribution")
        fig_conf = px.histogram(results_df, x="Confidence", nbins=20)
        st.plotly_chart(fig_conf, use_container_width=True)


def _build_pdf_bytes(title: str, sections: list[tuple[str, str]]) -> bytes:
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    _, height = letter
    y_pos = height - 40

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y_pos, title)
    y_pos -= 22

    for heading, body in sections:
        if y_pos < 70:
            pdf.showPage()
            y_pos = height - 40

        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(40, y_pos, heading)
        y_pos -= 16

        pdf.setFont("Helvetica", 9)
        lines = body.splitlines() if body else [""]
        for raw_line in lines:
            wrapped = textwrap.wrap(raw_line, width=105) or [""]
            for line in wrapped:
                if y_pos < 50:
                    pdf.showPage()
                    y_pos = height - 40
                    pdf.setFont("Helvetica", 9)
                pdf.drawString(40, y_pos, line)
                y_pos -= 12

        y_pos -= 6

    pdf.save()
    buffer.seek(0)
    return buffer.getvalue()


def _write_outputs_md(content: str) -> None:
    OUTPUTS_MD_PATH.write_text(content, encoding="utf-8")


# Load TabFM Model
try:
    with st.spinner("Loading TabFM (PyTorch Backend)..."):
        model = load_tabfm()
except Exception as e:
    hint = ""
    if isinstance(e, NameError) and "safetensors" in str(e):
        hint = " (Hint: install `safetensors`.)"
    st.error(f"Failed to load TabFM. Did you install it properly? Error: {e}{hint}")
    st.stop()

# Ollama model selector
ollama_models, ollama_error = _fetch_ollama_models(OLLAMA_TAGS_URL)
default_index = 0
if OLLAMA_DEFAULT_MODEL in ollama_models:
    default_index = ollama_models.index(OLLAMA_DEFAULT_MODEL)

selected_ollama_model = st.selectbox(
    "Ollama model",
    options=ollama_models,
    index=default_index,
    help="Models discovered from local Ollama (`/api/tags`).",
)
if ollama_error:
    st.caption(f"Model discovery fallback used: {ollama_error}")

# Mode selector
mode = st.radio("Mode", options=["CSV Upload", "Batch Upload"], horizontal=True)

if mode == "CSV Upload":
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Input Data (Training Context)")
        train_file = st.file_uploader("Upload Training CSV", type=["csv"], key="single_train")
    with col2:
        st.subheader("2. Target Data (To Predict)")
        test_file = st.file_uploader("Upload Test CSV", type=["csv"], key="single_test")

    if train_file is None or test_file is None:
        st.info("Upload both training and test CSV files to continue.")
        st.stop()

    try:
        train_df = _read_uploaded_csv(train_file)
        test_df = _read_uploaded_csv(test_file)
    except Exception as e:
        st.error(f"Failed to read CSV files: {e}")
        st.stop()

    target_column = st.selectbox("Select target column from training CSV", train_df.columns)

    st.caption("Training preview (first 50 rows)")
    st.dataframe(train_df.head(50), use_container_width=True)
    st.caption("Test preview (first 50 rows)")
    st.dataframe(test_df.head(50), use_container_width=True)

    if st.button("Run Prediction & Analyze", type="primary"):
        try:
            x_train, y_train, x_test = _prepare_datasets(
                train_df=train_df,
                test_df=test_df,
                target_column=str(target_column),
            )
        except Exception as e:
            st.error(f"Dataset validation failed: {e}")
            st.stop()

        with st.spinner("Running TabFM zero-shot classification..."):
            try:
                clf = TabFMClassifier(model=model)
                clf.fit(x_train, y_train)
                results_df = _predict_with_confidence(clf, x_test, str(target_column))
            except Exception as e:
                st.error(f"TabFM prediction failed: {e}")
                st.stop()

        pred_col = f"Predicted_{target_column}"
        st.subheader("3. TabFM Predictions")
        st.dataframe(results_df.head(500), use_container_width=True)
        _render_prediction_charts(results_df, pred_col)

        st.subheader("4. AI Insights (Ollama)")
        prompt = (
            "Analyze these prediction results:\n"
            f"{results_df.head(MAX_PREVIEW_ROWS).to_string(index=False)}\n"
            "Give a short, crisp 2-sentence summary."
        )

        with st.spinner(f"Generating insights using {selected_ollama_model}..."):
            ok, insight_text, error, latency = _call_ollama(prompt, selected_ollama_model)

        if ok and insight_text:
            st.success(insight_text)
            st.caption(f"Insight generated by {selected_ollama_model} in {latency:.2f}s")
            insight_status = "ok"
        else:
            st.error(f"Error calling Ollama: {error}. Please ensure Ollama is running.")
            insight_text = "Insight unavailable."
            insight_status = f"error: {error}"

        output_content = (
            "## 1. Input Data (Training Context)\n"
            f"```text\n{train_df.head(MAX_PREVIEW_ROWS).to_string()}\n```\n\n"
            "## 2. Target Data (To Predict)\n"
            f"```text\n{test_df.head(MAX_PREVIEW_ROWS).to_string()}\n```\n\n"
            "## 3. TabFM Predictions\n"
            f"```text\n{results_df.head(500).to_string()}\n```\n\n"
            "## 4. AI Insights (Ollama)\n"
            f"Model: {selected_ollama_model}\n\n"
            f"Status: {insight_status}\n\n"
            f"{insight_text}\n"
        )
        _write_outputs_md(output_content)
        st.caption("Saved: outputs.md")

        pdf_sections = [
            ("Model", f"TabFM backend: PyTorch\\nOllama model: {selected_ollama_model}"),
            ("Training Shape", f"Rows: {len(train_df)}\\nColumns: {len(train_df.columns)}"),
            ("Test Shape", f"Rows: {len(test_df)}\\nColumns: {len(test_df.columns)}"),
            ("Prediction Preview", results_df.head(MAX_PREVIEW_ROWS).to_string(index=False)),
            ("AI Insight", insight_text),
        ]
        pdf_bytes = _build_pdf_bytes("TabFM Zero-Shot Analyzer Report", pdf_sections)
        st.download_button(
            "Download Insights PDF",
            data=pdf_bytes,
            file_name=f"tabfm_insights_{_utc_timestamp()}.pdf",
            mime="application/pdf",
        )

else:
    st.subheader("1. Input Data (Training Context)")
    train_file = st.file_uploader("Upload Training CSV", type=["csv"], key="batch_train")

    st.subheader("2. Batch Test Files (To Predict)")
    test_files = st.file_uploader(
        "Upload Test CSV Files",
        type=["csv"],
        accept_multiple_files=True,
        key="batch_tests",
    )

    if train_file is None or not test_files:
        st.info("Upload one training CSV and at least one test CSV file to continue.")
        st.stop()

    if len(test_files) > MAX_BATCH_FILES:
        st.error(f"Batch Upload supports at most {MAX_BATCH_FILES} test CSV files per run.")
        st.stop()

    try:
        train_df = _read_uploaded_csv(train_file)
    except Exception as e:
        st.error(f"Failed to read training CSV: {e}")
        st.stop()

    target_column = st.selectbox("Select target column from training CSV", train_df.columns)

    st.caption("Training preview (first 50 rows)")
    st.dataframe(train_df.head(50), use_container_width=True)

    if st.button("Run Batch Prediction", type="primary"):
        try:
            y_train = train_df[str(target_column)].to_numpy()
            x_train = train_df.drop(columns=[str(target_column)])
        except Exception as e:
            st.error(f"Failed to prepare training dataset: {e}")
            st.stop()

        with st.spinner("Running TabFM on batch files..."):
            try:
                clf = TabFMClassifier(model=model)
                clf.fit(x_train, y_train)
            except Exception as e:
                st.error(f"TabFM fit failed: {e}")
                st.stop()

        pred_col = f"Predicted_{target_column}"
        aggregate_counts: dict[str, int] = {}
        status_rows: list[dict] = []
        successful_outputs: list[dict] = []

        for idx, uploaded in enumerate(test_files):
            try:
                test_df = _read_uploaded_csv(uploaded)
                _, _, x_test = _prepare_datasets(
                    train_df=train_df,
                    test_df=test_df,
                    target_column=str(target_column),
                )

                result_df = _predict_with_confidence(clf, x_test, str(target_column))
                counts = result_df[pred_col].value_counts().to_dict()
                for label, count in counts.items():
                    aggregate_counts[str(label)] = aggregate_counts.get(str(label), 0) + int(count)

                csv_bytes = result_df.to_csv(index=False).encode("utf-8")
                successful_outputs.append(
                    {
                        "name": uploaded.name,
                        "rows": int(len(result_df)),
                        "results": result_df,
                        "csv": csv_bytes,
                        "index": idx,
                    }
                )
                status_rows.append(
                    {
                        "file": uploaded.name,
                        "status": "success",
                        "rows": int(len(result_df)),
                        "error": "",
                    }
                )
            except Exception as e:
                status_rows.append(
                    {
                        "file": uploaded.name,
                        "status": "failed",
                        "rows": 0,
                        "error": str(e),
                    }
                )

        st.subheader("3. Batch Prediction Status")
        status_df = pd.DataFrame(status_rows)
        st.dataframe(status_df, use_container_width=True)

        if successful_outputs:
            for item in successful_outputs:
                with st.expander(f"Results: {item['name']}"):
                    st.dataframe(item["results"].head(200), use_container_width=True)
                    st.download_button(
                        label=f"Download predictions CSV - {item['name']}",
                        data=item["csv"],
                        file_name=f"predictions_{Path(item['name']).stem}.csv",
                        mime="text/csv",
                        key=f"download_csv_{item['index']}",
                    )

            counts_df = pd.DataFrame(
                [{"label": k, "count": v} for k, v in aggregate_counts.items()]
            )
            if not counts_df.empty:
                st.caption("Aggregate predicted class distribution")
                fig_aggregate = px.bar(counts_df, x="label", y="count")
                st.plotly_chart(fig_aggregate, use_container_width=True)

        st.subheader("4. AI Insights (Ollama)")
        insight_prompt = (
            "Analyze this batch prediction summary:\n"
            f"{status_df.to_string(index=False)}\n"
            f"Aggregate predicted labels: {aggregate_counts}\n"
            "Give a concise 3-sentence summary."
        )

        with st.spinner(f"Generating insights using {selected_ollama_model}..."):
            ok, insight_text, error, latency = _call_ollama(insight_prompt, selected_ollama_model)

        if ok and insight_text:
            st.success(insight_text)
            st.caption(f"Insight generated by {selected_ollama_model} in {latency:.2f}s")
            insight_status = "ok"
        else:
            st.error(f"Error calling Ollama: {error}. Please ensure Ollama is running.")
            insight_text = "Insight unavailable."
            insight_status = f"error: {error}"

        output_content = (
            "# Batch Run Summary\n\n"
            f"Model: {selected_ollama_model}\n\n"
            "## Per-file status\n"
            f"```text\n{status_df.to_string(index=False)}\n```\n\n"
            "## Aggregate predicted label counts\n"
            f"```text\n{aggregate_counts}\n```\n\n"
            "## AI Insights\n"
            f"Status: {insight_status}\n\n"
            f"{insight_text}\n"
        )
        _write_outputs_md(output_content)
        st.caption("Saved: outputs.md")

        batch_pdf_sections = [
            ("Model", f"TabFM backend: PyTorch\\nOllama model: {selected_ollama_model}"),
            ("Batch Status", status_df.to_string(index=False)),
            ("Aggregate Label Counts", str(aggregate_counts)),
            ("AI Insight", insight_text),
        ]
        batch_pdf = _build_pdf_bytes("TabFM Batch Report", batch_pdf_sections)
        st.download_button(
            "Download Batch Insights PDF",
            data=batch_pdf,
            file_name=f"tabfm_batch_insights_{_utc_timestamp()}.pdf",
            mime="application/pdf",
            key="download_batch_pdf",
        )
