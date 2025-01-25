### Parameters for The Renewable Energy Forecasting Project

# File Paths
FILE_PATH = 'Dataset/Turbine_Data.csv'
TRAIN_DATA_FILE = 'Dataset/train_data.csv'
TEST_DATA_FILE = 'Dataset/test_data.csv'
PROCESSED_TRAIN_DATA_FILE = 'Dataset/preprocessed_data.csv'
MODEL_FILE = 'renewable_energy_forecast_model.pkl'


# Data splitting parameters
TEST_SIZE = 0.2  # Proportion of data to be used for testing
RANDOM_STATE = 42  # Seed for reproducibility

# Target column
TARGET_COLUMN = "ActivePower"  # Replace with the name of your target variable

# Supported models and their parameters
MODELS = {
    "RandomForestRegressor": {
        "n_estimators": 100,
        "max_depth": None,
        "random_state": RANDOM_STATE
    },
    "LinearRegression": {},
    "GradientBoostingRegressor": {
        "n_estimators": 100,
        "learning_rate": 0.1,
        "max_depth": 3,
        "random_state": RANDOM_STATE
    },
    "XGBRegressor": {
        "n_estimators": 100,
        "learning_rate": 0.1,
        "max_depth": 3,
        "random_state": RANDOM_STATE,
        "objective": "reg:squarederror"
    }
}

# MLflow experiment name
MLFLOW_EXPERIMENT_NAME = "Renewable_Energy_Forecasting_Experiment"