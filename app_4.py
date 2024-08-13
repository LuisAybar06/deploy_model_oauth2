import uvicorn
from fastapi import FastAPI
from Houses import House
import numpy as np
import pandas as pd
from joblib import load


app = FastAPI()

classifier = load("linear_regression.joblib")

x_train = pd.read_csv('xtrain.csv')
features = pd.read_csv('selected_features.csv')
features = features['0'].to_list()

x_train = x_train[features]

@app.get("/")
def read_root():
    return {"message": "Hello"}


@app.post("/predict")
def predict_bancknote():
    predictions = classifier.predict(x_train)
    return {
        "predictions": predictions.tolist()
    }