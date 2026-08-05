# Predictive Maintenance AI

製造機械のセンサーデータから、故障リスクを予測する機械学習アプリです。

## 機能

- CSVデータからRandom Forestモデルを学習
- 故障確率を予測
- Precision / Recall / F1-score / ROC-AUCを表示
- Streamlit上でセンサー値を入力して診断
- 特徴量重要度を表示

## 使用技術

- Python
- pandas
- scikit-learn
- Streamlit
- joblib

## 1. VS Codeで開く

このフォルダをVS Codeで開きます。

## 2. 仮想環境を作成

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

PowerShellで実行が拒否された場合:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## 3. ライブラリをインストール

```powershell
pip install -r requirements.txt
```

## 4. データを準備

`data/ai4i2020.csv` にAI4I 2020 Predictive Maintenance DatasetのCSVを置いてください。

必要な列:

- Type
- Air temperature [K]
- Process temperature [K]
- Rotational speed [rpm]
- Torque [Nm]
- Tool wear [min]
- Machine failure

## 5. モデルを学習

```powershell
python -m src.train
```

学習済みモデルは `models/model.joblib` に保存されます。

## 6. アプリを起動

```powershell
streamlit run app/app.py
```

ブラウザで通常は以下が開きます。

```text
http://localhost:8501
```

## ディレクトリ構成

```text
predictive-maintenance-ai/
├── app/
│   └── app.py
├── data/
│   └── ai4i2020.csv
├── models/
│   └── model.joblib
├── src/
│   ├── __init__.py
│   ├── features.py
│   ├── predict.py
│   └── train.py
├── tests/
│   └── test_features.py
├── .gitignore
├── README.md
└── requirements.txt
```
