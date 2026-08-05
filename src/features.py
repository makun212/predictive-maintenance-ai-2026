from __future__ import annotations

import pandas as pd

NUMERIC_FEATURES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
]

CATEGORICAL_FEATURES = ["Type"]

TARGET = "Machine failure"

ALL_FEATURES = CATEGORICAL_FEATURES + NUMERIC_FEATURES


def validate_columns(df: pd.DataFrame) -> None:
    """学習・予測に必要な列が存在するか確認する。"""
    required = set(ALL_FEATURES + [TARGET])
    missing = sorted(required - set(df.columns))

    if missing:
        raise ValueError(
            "CSVに必要な列がありません: " + ", ".join(missing)
        )


def make_features(df: pd.DataFrame) -> pd.DataFrame:
    """モデル入力用の特徴量を返す。"""
    return df[ALL_FEATURES].copy()
