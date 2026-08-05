from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from src.features import (
    CATEGORICAL_FEATURES,
    NUMERIC_FEATURES,
    TARGET,
    make_features,
    validate_columns,
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "ai4i2020.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "model.joblib"


def build_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "category",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES,
            ),
            (
                "numeric",
                "passthrough",
                NUMERIC_FEATURES,
            ),
        ]
    )

    classifier = RandomForestClassifier(
        n_estimators=300,
        class_weight="balanced",
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1,
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", classifier),
        ]
    )


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"データが見つかりません: {DATA_PATH}\n"
            "data/ai4i2020.csv にCSVを置いてください。"
        )

    df = pd.read_csv(DATA_PATH)
    validate_columns(df)

    X = make_features(df)
    y = df[TARGET].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = build_pipeline()
    model.fit(X_train, y_train)

    predicted = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print("=== Classification Report ===")
    print(classification_report(y_test, predicted, digits=4))

    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, predicted))

    if y_test.nunique() == 2:
        print(f"ROC-AUC: {roc_auc_score(y_test, probabilities):.4f}")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"\nモデルを保存しました: {MODEL_PATH}")


if __name__ == "__main__":
    main()
