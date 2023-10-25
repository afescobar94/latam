from fastapi import FastAPI, HTTPException
import sys
import os
import pandas as pd
from typing import List
from typing import Union

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
async def post_predict(data: Union[List[dict], dict]) -> dict:
    try:
        if 'flights' in data:
            df = pd.DataFrame(data['flights'])
        else:
            df = pd.DataFrame(data)

        default_columns = {
            "Fecha-I": "2000-01-01 00:00:00",
            "Fecha-O": "2000-01-01 00:00:00",

        }
        for column, default_value in default_columns.items():
            if column not in df.columns:
                df[column] = default_value

        for mes in df['MES']:
            if mes is None or mes < 1 or mes > 12:
                raise HTTPException(status_code=400)
                return

        preprocessed_data = model.preprocess(df)
        predictions = model.predict(preprocessed_data)

        return {
            "predict": predictions
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return