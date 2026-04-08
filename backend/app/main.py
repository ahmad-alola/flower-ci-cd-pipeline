from pathlib import Path

import joblib
from fastapi import FastAPI
from .schemas import IrisInput, predictionOutput

app = FastAPI(title="Iris API")

model = joblib.load(Path(__file__).resolve().parent.parent / "models" / "iris_model.joblib")
labels = ["setosa", "versicolor", "virginica"]

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/predict", response_model=predictionOutput)
def predict(data: IrisInput):
    values = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width,
    ]]
    result = model.predict(values)[0]
    return {"prediction": labels[result]}