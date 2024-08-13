import uvicorn
from fastapi import FastAPI
from Houses import House
import numpy as np
import pandas as pd
from joblib import load


app = FastAPI()

classifier = load("linear_regression.joblib")

@app.get("/")
def read_root():
    return {"message": "Hello"}


@app.post("/predict")
def predict_houseprices(data: House):
    MSSubClass=data.MSSubClass
    MSZoning=data.MSZoning
    LotArea=data.LotArea
    LotShape=data.LotShape
    LandContour=data.LandContour
    LotConfig=data.LotConfig
    Neighborhood=data.Neighborhood
    OverallQual=data.OverallQual
    OverallCond=data.OverallCond
    YearRemodAdd=data.YearRemodAdd
    RoofStyle=data.RoofStyle
    Exterior1st=data.Exterior1st
    ExterQual=data.ExterQual
    Foundation=data.Foundation
    BsmtQual=data.BsmtQual
    BsmtExposure=data.BsmtExposure
    BsmtFinType1=data.BsmtFinType1
    HeatingQC=data.HeatingQC 
    CentralAir=data.CentralAir 
    stFlrSF=data.stFlrSF 
    ndFlrSF=data.ndFlrSF 
    GrLivArea=data.GrLivArea 
    BsmtFullBath=data.BsmtFullBath 
    FullBath=data.FullBath 
    HalfBath=data.HalfBath 
    KitchenQual=data.KitchenQual 
    TotRmsAbvGrd=data.TotRmsAbvGrd 
    Functional=data.Functional 
    Fireplaces=data.Fireplaces 
    FireplaceQu=data.FireplaceQu 
    GarageFinish=data.GarageFinish 
    GarageCars=data.GarageCars 
    PavedDrive=data.PavedDrive 
    WoodDeckSF=data.WoodDeckSF 
    ScreenPorch=data.ScreenPorch 
    SaleCondition=data.SaleCondition 

    prediction = classifier.predict([[MSSubClass, MSZoning, LotArea, LotShape, LandContour, LotConfig, Neighborhood, OverallQual, OverallCond, YearRemodAdd,
    RoofStyle, Exterior1st, ExterQual, Foundation, BsmtQual, BsmtExposure, BsmtFinType1, HeatingQC, CentralAir, stFlrSF, ndFlrSF, GrLivArea, BsmtFullBath,
    FullBath, HalfBath, KitchenQual, TotRmsAbvGrd, Functional, Fireplaces, FireplaceQu, GarageFinish, GarageCars, PavedDrive, WoodDeckSF, ScreenPorch, SaleCondition]])

    return {
        'predictions': prediction.tolist()
    }