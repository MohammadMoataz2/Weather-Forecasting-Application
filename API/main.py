# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models import prediciton
from pipelines import fit_preprocessor
from fastapi.responses import FileResponse
import os




app = FastAPI()

# CORS configuration
#python -m uvicorn main:app --reload

origins = [
    "http://localhost",
    'http://127.0.0.1:5501',
    'http://127.0.0.1:5502',
    'http://127.0.0.1:5500',
    "preprocess.py"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class pred_data(BaseModel):
    city: str
    date : str


@app.post("/predict/")
async def predict(data: pred_data):
    try:
        city = data.city
        date = data.date

        print("Data before ETL:", city, date)
        print("_________")
        temp, pres, wdir, wspd = prediciton(city, date)
        print("_________")
        print(temp, pres, wdir, wspd)

        return {"avg_temp": round(temp[0],2), "avg_pres": round(pres[0],2), "avg_wdir": round(wdir[0],2), "avg_wspd": round(wspd[0],2)}

    except Exception as e:
        raise e
