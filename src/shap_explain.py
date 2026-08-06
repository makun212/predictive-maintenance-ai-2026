from __future__ import annotations

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import shap
from sklearn.model_selection import train_test_split

from src.features import TARGET, make_features, validate_columns
from src.train import DATA_PATH, MODEL_PATH


PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = PROJECT_ROOT / "images"
OUTPUT_PATH = IMAGES_DIR / "shap-summary.png"


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"データが見つかりません: {DATA_PATH}"
        )

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "学習済みモデルがありません。"
            "先に `python -m src.train` を実行してください。"
        )

    IMAGES_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    validate_columns(df)

    X = make_features(df)
    y = df[TARGET].astype(int)

    _, X_test, _, _ = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    pipeline = joblib.load(MODEL_PATH)

    preprocessor = pipeline.named_steps["preprocessor"]
    classifier = pipeline.named_steps["classifier"]

    # 処理時間を抑えるため、最大300件を使用
    sample = X_test.sample(
        n=min(300, len(X_test)),
        random_state=42,
    )

    transformed = preprocessor.transform(sample)
    feature_names = preprocessor.get_feature_names_out()

    transformed_df = pd.DataFrame(
        transformed,
        columns=feature_names,
        index=sample.index,
    )

    explainer = shap.TreeExplainer(classifier)
    shap_values = explainer(transformed_df)

    # 二値分類の故障クラス（1）だけを使用
    if shap_values.values.ndim == 3:
        failure_explanation = shap.Explanation(
            values=shap_values.values[:, :, 1],
            base_values=shap_values.base_values[:, 1],
            data=shap_values.data,
            feature_names=shap_values.feature_names,
        )
    else:
        failure_explanation = shap_values

    shap.plots.beeswarm(
        failure_explanation,
        max_display=10,
        show=False,
    )

    plt.title("SHAP Summary: Machine Failure")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_PATH,
        dpi=200,
        bbox_inches="tight",
    )
    plt.close()

    print("SHAP画像を生成しました。")
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()