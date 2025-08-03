# Predictive Modeling of Stroke Risk in High-Risk Populations Using Machine Learning Techniques

## 🔍 Description

This project investigates the use of various machine learning algorithms to predict stroke risk using a publicly available dataset. It focuses on preprocessing techniques like SMOTE + Tomek Links, feature selection, model training, evaluation, and interpretability using explainable AI techniques.

## 📁 Project Structure

```
my-thesis/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── docs/
│   ├── defence/
│   └── pre-defence/
│   └── thesis proposal/
│   ├── data_preprocessing.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   ├── utils.py
├── notebooks/
│   └── thesis_experiments.ipynb
├── requirements.txt
├── .gitignore
```

## ⚙️ How to Run

1. Clone the repo:

```bash
git clone https://github.com/your-username/my-thesis.git
cd my-thesis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your dataset: Place your dataset (e.g., `stroke_data.csv`) in `data/raw/`

4. Train the model:

```bash
python code/train.py
```

5. Evaluate the model: Run the evaluation cells inside `notebooks/thesis_experiments.ipynb` or call functions from `evaluate.py`.

## 🧠 Models Used

- Logistic Regression
- Random Forest
- XGBoost
- SVM
- KNN
- Gradient Boosting
- Stacking Classifier

## 📌 Features

- Feature selection using RFE
- Class balancing with SMOTE + Tomek Links
- Hyperparameter tuning
- Confusion matrix, ROC-AUC

## 🧑‍💻 Authors

- Antika Ghosh (190104005)
- Purna Chandra Saha (20200104141)
- Apu Das (20200204108)

## 📚 Supervised by

Prof. Dr. S. M. A. AL-Mamun\
Department of CSE, AUST

---

_For academic use and reproducibility in predictive healthcare research._
