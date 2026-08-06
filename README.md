# ⚙️ Predictive Maintenance AI

製造設備のセンサーデータから故障リスクを予測する機械学習Webアプリケーションです。

本プロジェクトでは AI4I 2020 Predictive Maintenance Dataset を用いて、設備故障を予測する Random Forest モデルを構築し、Streamlit により誰でも利用できるWebアプリとして実装しました。

---

## 🚀 Overview

このアプリでは以下のセンサーデータを入力すると、設備故障の確率を予測できます。

- Product Type
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

学習済みモデルを利用してリアルタイムに推論を行い、故障リスクを分かりやすく表示します。

---

# 🖥️ Application

## 入力画面

![Application](images/app-screen.png)

---

## 推論結果

![Prediction Result](images/prediction-result.png)

---

# 🧠 Machine Learning

## 使用アルゴリズム

- Random Forest Classifier

## 前処理

- OneHotEncoder
- Train/Test Split
- Pipeline
- Joblibによるモデル保存

---

# 📊 Model Performance

| Metric | Score |
|---------|-------:|
| Accuracy | 97.4% |
| Precision | 58.9% |
| Recall | 77.9% |
| F1-score | 67.1% |
| ROC-AUC | 0.962 |

---

# 📂 Project Structure

```text
predictive-maintenance-ai
│
├── app
│   └── app.py
│
├── data
│   ├── ai4i2020.csv
│   └── README.txt
│
├── images
│   ├── app-screen.png
│   └── prediction-result.png
│
├── models
│   └── model.joblib
│
├── src
│   ├── train.py
│   ├── predict.py
│   ├── features.py
│   └── __init__.py
│
├── tests
│   └── test_features.py
│
├── README.md
└── requirements.txt
```

---

# ⚙️ Tech Stack

### Language

- Python

### Machine Learning

- scikit-learn
- pandas
- NumPy

### Visualization

- Matplotlib

### Web Application

- Streamlit

### Development

- Git
- GitHub
- VS Code

---

# ▶️ How to Run

```bash
git clone https://github.com/makun212/predictive-maintenance-ai-2026.git

cd predictive-maintenance-ai

python -m venv .venv

source .venv/Scripts/activate

pip install -r requirements.txt

python -m src.train

streamlit run app/app.py
```

---

# 📄 Dataset

AI4I 2020 Predictive Maintenance Dataset

https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

---

# 💡 What I Learned

このプロジェクトを通して以下のスキルを身につけました。

- 機械学習モデルの構築
- データ前処理
- 特徴量エンジニアリング
- モデル評価
- StreamlitによるWebアプリ開発
- Joblibによるモデル保存
- Git / GitHub を利用したバージョン管理

---

# 🔮 Future Improvements

今後は以下の機能追加を予定しています。

- SHAPによる予測根拠の可視化
- XGBoostとの性能比較
- FastAPIによるAPI化
- Docker対応
- Streamlit Cloudへのデプロイ
- LLMを利用した保守レポート自動生成

---

# 👤 Author

**博政 尾方**

Tokyo University of Science

Department of Information and Computer Science

### Interests

- Machine Learning
- Data Science
- Generative AI
- Predictive Maintenance
