# File: inflestApp/analysis/analysis.py

import pandas as pd
import joblib
from statsmodels.tsa.api import VAR
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from ..models import MacroeconomicData
from statsmodels.tsa.vector_ar.var_model import VARResults
import pickle

# inflestApp/analysis/analysis.py

import pandas as pd
import numpy as np
import pickle
from statsmodels.tsa.statespace.varmax import VARMAX
from statsmodels.tsa.stattools import adfuller

# Function to check stationarity
def check_stationarity(data):
    result = adfuller(data)
    return result[1] <= 0.05  # Returns True if stationary

# Function to prepare data for VARMAX modeling
def check_stationarity(data):
    result = adfuller(data)
    return result[1] <= 0.05  # Returns True if stationary

# Function to prepare data for VARMAX modeling
def prepare_data(data):
    # Check and transform non-stationary variables
    for column in data.columns:
        if not check_stationarity(data[column]):
            # Apply differencing or other transformations
            data[column] = data[column].diff().dropna()
    
    # Create lagged variables (if necessary)
    # Split data into training and testing sets
    
    return data


from scipy.linalg import LinAlgError

# Function to train VARMAX model
def train_varmax_model(data):
    # try:
    model = VARMAX(data, order=(1, 1))  # Adjust order as needed
    results = model.fit(maxiter=100, disp=False)  # Adjust maxiter and other parameters
    model_path = 'varmax_model.pkl'
    with open(model_path, 'wb') as file:
        pickle.dump(results, file)
    return model_path
    # except Exception as e:
    #     print(f"Error during model training: {e}")
    #     return None
    # except Exception as e:
    #     print(f"Error during model training: {e}")
    #     return None


# Function to forecast using VARMAX model
def forecast_varmax_model(model_path, input_data):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        # input_df = pd.DataFrame([input_data])  # Ensure input_data is correctly formatted
        forecast = model.forecast(steps=1, new_data=input_data)  # Adjust steps and new_data format
        return forecast
    except Exception as e:
        print(f"Error during model forecasting: {e}")
        return None


# Example usage:
if __name__ == "__main__":
   hello = "hello"



# def clean_and_prepare_data(df):
#     # Drop 'country' if it's not needed for modeling
#     df = df.drop(columns=['country'])
    
#     # Convert to numeric and handle any non-numeric data
#     df = df.apply(pd.to_numeric, errors='coerce')
    
#     # Drop rows with NaN values
#     df.dropna(inplace=True)
    
#     return df



# Assuming you have imported necessary modules and models

# def train_and_save_model(model_path):
#     # Fetch data from MacroeconomicData model
#     data_objects = MacroeconomicData.objects.all()
    
#     # Convert fetched data into a pandas DataFrame
#     print(data_objects)
#     data = pd.DataFrame(list(data_objects.values()))
    
#     # Drop unnecessary columns (if any)
#     data.drop(['id'], axis=1, inplace=True)  # Adjust columns as per your model
    
#     # Optionally, preprocess or manipulate the data as needed
    
#     # Train VAR model
#     model = VAR(data)
#     results = model.fit(maxlags=5, ic='aic')  # Example parameters, adjust as needed
    
#     # Save trained model (optional)
#     with open(model_path, 'wb') as f:
#         pickle.dump(results, f)
    
#     return results  # Or any other return value as needed





# def forecast_var_model(model_path, input_data):
#     # Load the saved VAR model using pickle
#     with open(model_path, 'rb') as file:
#         model = pickle.load(file)
    
#     # Perform forecasting with the loaded model
#     forecast = model.forecast(input_data.values)
    
#     return forecast








# def build_var_model():
#     # Fetch data from Django model
#     data = list(MacroeconomicData.objects.all().values())
#     if not data:
#         return "No data available"

#     # Create DataFrame from fetched data
#     df = pd.DataFrame(data)

#     # Rename columns to match VAR requirements
#     required_columns = {
#         'inf': 'inflation_rate',
#         'interest_rate': 'interest_rate',
#         'exchange_rate': 'exchange_rate',
#         'real_gdp': 'real_gdp',
#         'fdi': 'fdi',
#         'fiscal_expenditure': 'fiscal_expenditure'
#     }
#     df.rename(columns=required_columns, inplace=True)

#     # Select necessary columns for modeling
#     selected_columns = list(required_columns.values()) + ['year', 'country']
#     df = df[selected_columns]

#     # Clean data: remove NaN and infinite values
#     df.dropna(inplace=True)
#     df.replace([float('inf'), float('-inf')], pd.NA, inplace=True)
#     df.dropna(inplace=True)

#     if df.empty:
#         return "No data available after cleaning"

#     # Set index if necessary (depends on your analysis needs)
#     df.set_index(['year', 'country'], inplace=True)

#     # Initialize VAR model
#     model = VAR(df)

#     # Fit VAR model
#     results = model.fit(maxlags=15, ic='aic')

#     return results

# def perform_svar_analysis():
#     data = list(MacroeconomicData.objects.all().values())
#     if not data:
#         return "No data available"

#     df = pd.DataFrame(data)
#     required_columns = {
#         'inf': 'inflation_rate',
#         'interest_rate': 'interest_rate',
#         'exchange_rate': 'exchange_rate',
#         'real_gdp': 'real_gdp',
#         'fdi': 'fdi',
#         'fiscal_expenditure': 'fiscal_expenditure'
#     }

#     df.rename(columns=required_columns, inplace=True)
#     selected_columns = list(required_columns.values()) + ['year', 'country']
#     df = df[selected_columns]
    
#     df.dropna(inplace=True)
#     df.replace([float('inf'), float('-inf')], pd.NA, inplace=True)
#     df.dropna(inplace=True)

#     if df.empty:
#         return "No data available after cleaning"

#     df.set_index(['year', 'country'], inplace=True)
#     model = VAR(df)
#     results = model.fit(maxlags=15, ic='aic')

#     return results


# def forecast_var_model(model, input_data):
#     input_df = pd.DataFrame(input_data)
#     forecast = model.predict(input_df)
#     return forecast


# def train_and_save_model(df):
#     model = VAR(df)
#     results = model.fit(maxlags=15, ic='aic')
#     # Save the model if needed
#     return model

# def forecast_var_model(model, input_data):
#     # Ensure input_data is in the correct format
#     input_df = pd.DataFrame(input_data, columns=model.endog_names)
#     forecast = model.forecast(input_df.values)
#     return forecast, None  # Assuming you don't calculate MSE here
