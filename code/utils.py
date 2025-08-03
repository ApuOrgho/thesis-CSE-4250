from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

def recursive_feature_elimination(X, y, n_features_to_select=10):
    model = LogisticRegression(max_iter=1000)
    selector = RFE(model, n_features_to_select=n_features_to_select)
    selector = selector.fit(X, y)
    selected_features = X.columns[selector.support_]
    return selected_features
