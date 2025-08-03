from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

def get_models():
    models = {
        "logistic_regression": LogisticRegression(max_iter=1000),
        "random_forest": RandomForestClassifier(),
        "gradient_boosting": GradientBoostingClassifier(),
        "svm": SVC(probability=True),
        "knn": KNeighborsClassifier(),
        "xgboost": XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    }
    return models

def get_stacking_model(base_models, final_estimator):
    estimators = [(name, model) for name, model in base_models.items()]
    return StackingClassifier(estimators=estimators, final_estimator=final_estimator, cv=5)
