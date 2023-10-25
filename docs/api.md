# Documentation for `api.py`

## Overview

The `api.py` module provides a FastAPI-based web application that serves a health endpoint and a prediction endpoint related to flight delays. The prediction functionality uses a model from the `model` module, named `DelayModel`, and is designed to take input in the form of flight data and produce delay predictions based on this data.

## Dependencies

- **fastapi**: Provides the web framework.
- **HTTPException**: Allows for raising HTTP errors directly.
- **sys**: System-specific parameters and functions.
- **os**: Provides functions to interact with the operating system.
- **pandas**: A data manipulation and analysis library.
- **typing**: Provides support for type hints.

## Data Paths Setup

``` 
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir)
sys.path.append(data_path)
```

## API Initialization
- app = FastAPI()

- model = DelayModel()

Endpoints
1. **Health Endpoint**
- Endpoint: /health
- HTTP Method: GET
- Status Code: 200
- Response:

```
{
    "status": "OK"
}
```

This is a simple health check endpoint that returns a status of "OK" to indicate that the API is functioning properly.

```
@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }
```

2. **Prediction Endpoint**

- Endpoint: /predict

- HTTP Method: POST

- Status Code: 200

**Input:**

- data: A dictionary or a list of dictionaries containing flight data.
**Output:**
```
{
    "predict": [predictions]
}
```

Here, [predictions] is a list of predicted delays based on the provided input data.

**Function Details:**

- Converts the input data into a pandas DataFrame.
- Sets default values for columns "Fecha-I" and "Fecha-O" if they are not present in the data.
- Checks the 'MES' column values to ensure they are valid month numbers (1-12).
- Preprocesses the data using the model.preprocess function.
- Predicts flight delays using the model.predict function.
- Returns the predictions.
- In case of an error (e.g., invalid data or a prediction error), an HTTP 400 error is raised with details of the exception.
```
@app.post("/predict", status_code=200)
async def post_predict(data: Union[List[dict], dict]) -> dict:
    ...
```

### Exceptions
If any step in the prediction process fails, an exception is raised and an HTTP 400 status is returned to the client with the error detail.
