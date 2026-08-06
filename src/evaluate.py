from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
)
from sklearn.model_selection import train_test_split

from src.features import TARGET, make_features, validate_columns
from src.train import DATA_PATH, MODEL_PATH

PROJECT_ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = PROJECT_ROOT / "images"


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

    _, X_test, _, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = joblib.load(MODEL_PATH)

    # 混同行列
    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test,
        y_test,
        display_labels=["Normal", "Failure"],
    )
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig(
        IMAGES_DIR / "confusion-matrix.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close()

    # ROC曲線
    RocCurveDisplay.from_estimator(
        model,
        X_test,
        y_test,
    )
    plt.title("ROC Curve")
    plt.tight_layout()
    plt.savefig(
        IMAGES_DIR / "roc-curve.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close()

    # 特徴量重要度
    preprocessor = model.named_steps["preprocessor"]
    classifier = model.named_steps["classifier"]

    feature_names = preprocessor.get_feature_names_out()
    importances = classifier.feature_importances_

    importance_df = pd.DataFrame(
        {
            "feature": feature_names,
            "importance": importances,
        }
    ).sort_values(
        "importance",
        ascending=True,
    )

    plt.figure(figsize=(8, 5))
    plt.barh(
        importance_df["feature"],
        importance_df["importance"],
    )
    plt.xlabel("Importance")
    plt.title("Feature Importance")
    plt.tight_layout()
    plt.savefig(
        IMAGES_DIR / "feature-importance.png",
        dpi=200,
        bbox_inches="tight",
    )
    plt.close()

    print("評価画像を生成しました。")
    print(IMAGES_DIR / "confusion-matrix.png")
    print(IMAGES_DIR / "roc-curve.png")
    print(IMAGES_DIR / "feature-importance.png")


if __name__ == "__main__":
    main()