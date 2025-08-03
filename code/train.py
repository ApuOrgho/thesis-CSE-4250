from code.data_preprocessing import load_data, encode_categorical, balance_data, split_data
from code.model import get_models
from sklearn.metrics import accuracy_score
import joblib

def train_and_save_model(filepath):
    df = load_data(filepath)
    df, encoders = encode_categorical(df)
    X_train, X_test, y_train, y_test = split_data(df, 'stroke')
    X_train, y_train = balance_data(X_train, y_train)

    models = get_models()
    best_model = None
    best_acc = 0

    for name, model in models.items():
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))
        print(f"{name}: {acc:.4f}")
        if acc > best_acc:
            best_model = model
            best_acc = acc

    joblib.dump(best_model, 'model/best_model.pkl')
    return best_model
