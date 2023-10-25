# main.py documentation 

`model.py` contains code for preprocessing raw flight data and making delay predictions based on the processed data using a logistic regression model. Below is a detailed breakdown of the code and its functionalities.

---

## **Imports:**

- **pandas** as **pd**: Used for data manipulation.
- **datetime**: For handling date and time operations.
- **typing**: Provides type hints.
- **numpy** as **np**: Library for numerical computing.
- **os**: For OS operations.
- **sklearn.model_selection.train_test_split**: Splits data into training and test sets.
- **sklearn.linear_model.LogisticRegression**: Logistic regression model for prediction.
- **joblib.dump, load**: Save and load trained models.
- **sklearn.metrics.confusion_matrix, classification_report**: Evaluates the model's performance.

---

## **DelayModel Class**

### **Attributes:**

- **_model**: Stores the trained logistic regression model.
- **top_10_features**: Top features for the model.

### **Methods:**

#### **_get_period_day(date: str) -> str**

- Determines the time of day from the input date-time.
- **Inputs**: 
  - `date`: A date-time string (`%Y-%m-%d %H:%M:%S` format).
- **Outputs**: One of the strings: `mañana`, `tarde`, or `noche`.

#### **_is_high_season(fecha: str) -> int**

- Checks if the date is during the high season.
- **Inputs**: 
  - `fecha`: A date-time string (`%Y-%m-%d %H:%M:%S` format).
- **Outputs**: `1` if it's the high season, otherwise `0`.

#### **_get_min_diff(row: pd.Series) -> float**

- Calculates the difference in minutes between two date-time columns.
- **Inputs**: 
  - `row`: A pandas series with 'Fecha-O' and 'Fecha-I'.
- **Outputs**: Difference in minutes.

#### **preprocess(data: pd.DataFrame, target_column: str = None) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]**

- Processes raw data for model training or prediction.
- **Inputs**: 
  - `data`: Raw flight data dataframe.
  - `target_column` (optional): If set, extracts this column as the target.
- **Outputs**: Features and target (if `target_column` is set), else just features.

#### **fit(features: pd.DataFrame, target: pd.DataFrame) -> None**

- Trains the logistic regression model.
- **Inputs**: 
  - `features`: Preprocessed features dataframe.
  - `target`: Target column dataframe.
- **Side Effects**: Saves the model to 'logistic_regression_model.joblib' and the `_model` attribute.

#### **predict(features: pd.DataFrame) -> List[int]**

- Predicts flight delays using the trained model.
- **Inputs**: 
  - `features`: Preprocessed features dataframe.
- **Outputs**: A list of delay predictions (either 0 or 1).

---

## **Usage**

1. Instantiate the `DelayModel` class.
2. Use `preprocess` for raw data processing.
3. If needed, train with `fit` using preprocessed data.
4. Predict new data using `predict`.

