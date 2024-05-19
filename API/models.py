# models.py
import joblib
import pandas as pd
from transformers import DateTransformer

from pipelines import fit_preprocessor

df = pd.read_csv("stations.csv")

def prediciton(city,date):


    

    preprocessor = fit_preprocessor(df)

    d_test = pd.DataFrame([[city,date]],columns=["City","date"])
    d_test["date"] = pd.to_datetime(d_test["date"])

    d_test = preprocessor.transform(d_test)

    tavg_model = joblib.load('tavg_model.pkl')
    pres_model = joblib.load('pres_model.pkl')
    wdir_model = joblib.load('wdir_model.pkl')
    wspd_model = joblib.load('wspd_model.pkl')

    tavg_value = tavg_model.predict(d_test)
    pres_value = pres_model.predict(d_test)
    wdir_value = wdir_model.predict(d_test)
    wspd_value = wspd_model.predict(d_test)

    return tavg_value, pres_value, wdir_value, wspd_value
