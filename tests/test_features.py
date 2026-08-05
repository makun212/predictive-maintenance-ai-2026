import pandas as pd
import pytest

from src.features import make_features, validate_columns


def test_validate_columns_accepts_valid_dataframe() -> None:
    df = pd.DataFrame(
        {
            "Type": ["M"],
            "Air temperature [K]": [300.0],
            "Process temperature [K]": [310.0],
            "Rotational speed [rpm]": [1500],
            "Torque [Nm]": [40.0],
            "Tool wear [min]": [100],
            "Machine failure": [0],
        }
    )

    validate_columns(df)
    features = make_features(df)

    assert "Machine failure" not in features.columns
    assert len(features) == 1


def test_validate_columns_rejects_missing_columns() -> None:
    df = pd.DataFrame({"Type": ["M"]})

    with pytest.raises(ValueError):
        validate_columns(df)
