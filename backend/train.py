from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path("../data/iris.csv")
MODEL_PATH = Path("models/iris_model.joblib")


def load_data():
    if DATA_PATH.exists():
        df = pd.read_csv(DATA_PATH)
    else:
        iris = load_iris(as_frame=True)
        df = iris.frame
        df["target_name"] = df["target"].map(dict(enumerate(iris.target_names)))

    df = df.drop_duplicates().dropna()

    X = df[["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]]
    y = df["target"]
    return X, y


def main():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    mlflow.set_experiment("iris-training")

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        mlflow.log_param("model", "RandomForestClassifier")
        mlflow.log_param("test_size", 0.2)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, MODEL_PATH)

        print(f"Accuracy: {acc:.4f}")
        print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()