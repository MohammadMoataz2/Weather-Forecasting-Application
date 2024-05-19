# pipelines.py
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from transformers import DateTransformer
import pandas as pd

# Define pipeline for transforming dates
date_pipeline = Pipeline([
    ('date_transformer', DateTransformer())
])

# Define pipeline for one-hot encoding City
city_pipeline = Pipeline([
    ('one_hot_encoder', OneHotEncoder())
])

# Combine pipelines using ColumnTransformer
preprocessor = ColumnTransformer([
    ('date_pipeline', date_pipeline, ['date']),
    ('city_pipeline', city_pipeline, ['City'])
])

# Fit and transform the data
def fit_preprocessor(df):
    df["date"] = pd.to_datetime(df["date"])
    preprocessor.fit_transform(df)

    return preprocessor