from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.predict import MODEL_PATH, load_model  # noqa: E402

st.set_page_config(
    page_title="製造設備 故障予測AI",
    page_icon="⚙️",
    layout="wide",
)

st.title("⚙️ 製造設備 故障予測AI")
st.write(
    "センサーデータから、製造機械が故障する確率を予測します。"
)

if not MODEL_PATH.exists():
    st.error(
        "学習済みモデルがありません。ターミナルで "
        "`python -m src.train` を実行してください。"
    )
    st.stop()

model = load_model()

left, right = st.columns(2)

with left:
    product_type = st.selectbox(
        "製品タイプ",
        options=["L", "M", "H"],
        index=1,
    )

    air_temperature = st.number_input(
        "外気温度 [K]",
        min_value=250.0,
        max_value=350.0,
        value=300.0,
        step=0.1,
    )

    process_temperature = st.number_input(
        "工程温度 [K]",
        min_value=250.0,
        max_value=400.0,
        value=310.0,
        step=0.1,
    )

with right:
    rotational_speed = st.number_input(
        "回転速度 [rpm]",
        min_value=500,
        max_value=4000,
        value=1500,
        step=10,
    )

    torque = st.number_input(
        "トルク [Nm]",
        min_value=0.0,
        max_value=100.0,
        value=40.0,
        step=0.1,
    )

    tool_wear = st.number_input(
        "工具摩耗時間 [min]",
        min_value=0,
        max_value=300,
        value=100,
        step=1,
    )

threshold = st.slider(
    "要点検と判定するしきい値",
    min_value=0.05,
    max_value=0.95,
    value=0.40,
    step=0.05,
)

if st.button("故障リスクを診断", type="primary"):
    input_data = pd.DataFrame(
        [
            {
                "Type": product_type,
                "Air temperature [K]": air_temperature,
                "Process temperature [K]": process_temperature,
                "Rotational speed [rpm]": rotational_speed,
                "Torque [Nm]": torque,
                "Tool wear [min]": tool_wear,
            }
        ]
    )

    probability = float(model.predict_proba(input_data)[0, 1])

    st.subheader("診断結果")
    st.metric("故障確率", f"{probability:.1%}")

    if probability >= threshold:
        st.error("故障リスクが高いため、点検を推奨します。")
    else:
        st.success("現在の故障リスクは低いと予測されました。")

    st.progress(min(max(probability, 0.0), 1.0))

    st.caption(
        "この結果は学習データに基づく予測です。"
        "実際の設備判断では専門家による確認が必要です。"
    )
