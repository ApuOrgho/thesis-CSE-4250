# 🧠 Predictive Modeling of Stroke Risk in High-Risk Populations Using Machine Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](#)

This project explores the application of machine learning techniques to predict the risk of stroke in high-risk individuals using a real-world medical dataset. Our pipeline emphasizes data preprocessing, class imbalance correction, robust model training, performance evaluation, and interpretability using explainable AI (XAI) tools.

---

## 📝 Table of Contents

- [Project Overview](#-project-overview)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [How to Run](#️-how-to-run)
- [Models Implemented](#-models-implemented)
- [Key Features](#-key-features)
- [Results & Visualizations](#-results--visualizations)
- [Contributors](#-contributors)
- [Supervisor](#-supervisor)
- [License](#-license)

---

## 🔍 Project Overview

Stroke is a leading cause of death and long-term disability worldwide. Early prediction of stroke risk can significantly improve clinical decision-making and preventive care. This project investigates various supervised machine learning models to predict the likelihood of stroke based on patient attributes. We aim to build an accurate, interpretable, and reproducible stroke prediction pipeline.

---

## 📁 Project Structure

```
thesis-CSE-4250/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── raw/                 # Original dataset(s)
│   └── processed/           # Cleaned & engineered data
├── docs/
│   ├── defence/
│   ├── pre-defence/
│   └── thesis proposal/
├── notebooks/
│   └── thesis_experiments.ipynb
├── code/
│   ├── data_preprocessing.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
```

---

## 💻 Installation & Setup

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/ApuOrgho/thesis-cse-4250.git
cd thesis-CSE-4250
\`\`\`

### 2. Set Up a Virtual Environment (Optional but Recommended)

\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
\`\`\`

### 3. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## ⚙️ How to Run

### Step 1: Add Dataset

Place your dataset (e.g., \`stroke_data.csv\`) inside:

\`\`\`bash
data/raw/
\`\`\`

### Step 2: Preprocess the Data

\`\`\`bash
python code/data_preprocessing.py
\`\`\`

### Step 3: Train Models

\`\`\`bash
python code/train.py
\`\`\`

### Step 4: Evaluate Performance

You can either:
- Use evaluation functions from \`evaluate.py\`, or
- Open the \`notebooks/thesis_experiments.ipynb\` notebook to explore results interactively.

---

## 🧠 Models Implemented

- ✅ Logistic Regression
- ✅ Support Vector Machine (SVM)
- ✅ K-Nearest Neighbors (KNN)
- ✅ Random Forest
- ✅ Gradient Boosting
- ✅ XGBoost
- ✅ Stacking Classifier

---

## 🚀 Key Features

- ✅ Feature selection using **Recursive Feature Elimination (RFE)**
- ✅ Class balancing with **SMOTE + Tomek Links**
- ✅ Modular architecture for preprocessing, training, and evaluation
- ✅ Model explainability with **SHAP** or **LIME**
- ✅ Evaluation metrics: **Accuracy**, **Precision**, **Recall**, **F1-Score**, **ROC-AUC**
- ✅ Confusion matrix and ROC curve visualizations
- ✅ Reproducibility across runs

---

## 📊 Results & Visualizations

- 📈 ROC curves and confusion matrices are generated automatically
- 📊 Feature importance plots for interpretability
- 🧮 Classification reports with precision-recall trade-offs

> Detailed results can be explored in the [\`notebooks/thesis_experiments.ipynb\`](notebooks/thesis_experiments.ipynb) notebook.

---

## 👨‍💻 Contributors

- **Antika Ghosh** — \`190104005\`  
- **Purna Chandra Saha** — \`20200104141\`  
- **Apu Das** — \`20200204108\`

---

## 👨‍🏫 Supervisor

**Prof. Dr. S. M. A. AL-Mamun**  
*Department of Computer Science & Engineering*  
*Ahsanullah University of Science & Technology (AUST)*

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> _Developed as part of the undergraduate thesis for CSE 4250: Machine Learning, AUST (2025)._
"""
file_path
