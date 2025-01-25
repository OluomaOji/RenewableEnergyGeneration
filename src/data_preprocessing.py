import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessing:
    def __init__(self):
        """
        Initialising the Data Preprocessing class
        """
        pass

    @staticmethod
    def handle_missing_values(data):
        """
        Handle missing values in the data by dropping rows with NaN
        """
        try:
            data=data.dropna()

            print('Missing Values Handled.')
            return data
        except Exception as e:
            print(f'Error handling Missing Values: {e}')
            return None

    @staticmethod    
    def negative_Value_power(data):
        """
        Handle the Negative Value of Power
        """
        try:
            if 'ActivePower' not in data.columns:
                raise ValueError("'ActivePower' column is not in the dataset.")
            data=data[data['ActivePower']>=0]
            print[f'Negative Power Handled']
            return data
        except Exception as e:
            print(f'Error Handling the Negative Values. ')
            return None

    @staticmethod
    def scale_features(data):
        """
        Scales numerical features using StandardScaler.
        """
        try:
            scaler = StandardScaler()
            scaled_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
            print("Features scaled.")
            return scaled_data
        except Exception as e:
            print(f"Error scaling features: {e}")
            return None