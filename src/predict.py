from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "model.joblib"


def load_model() -> Any:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "学習済みモデルがありません。先に `python -m src.train` を実行してください。"
        )

    return joblib.load(MODEL_PATH)


def predict_failure_probability(input_data: dict[str, float | str]) -> float:
    model = load_model()
    frame = pd.DataFrame([input_data])
    probability = model.predict_proba(frame)[0, 1]
    return float(probability)
