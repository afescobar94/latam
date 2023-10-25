from fastapi import FastAPI, HTTPException, Depends, Body
import sys
import os
import pandas as pd
from typing import List

current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir)
sys.path.append(data_path)
from model import DelayModel

app = FastAPI()

model = DelayModel()

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }

@app.post("/predict", status_code=200)
async def post_predict(data: List[dict]) -> dict:
    try:
        df = pd.DataFrame(data)
        preprocessed_data = model.preprocess(df)
        predictions = model.predict(preprocessed_data)

        return {
            "predictions": predictions
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return