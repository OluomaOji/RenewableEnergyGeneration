## Import libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from params import TEST_SIZE,FILE_PATH,RANDOM_STATE,TEST_DATA_FILE,TRAIN_DATA_FILE

class DataIngestion:
    def __init__(self, file_path=FILE_PATH,test_size=TEST_SIZE,random_state=RANDOM_STATE):
        """
        Initializing the Data Ingestion Class
        """
        self.file_path=file_path
        self.test_size=test_size
        self.random_state=random_state

    def load_data(self):
        """
        Load the Dataset from the File Path
        """
        try:
            data = pd.read_csv(FILE_PATH)
            print('Dataset Successfully Loaded')
            return data
        except Exception as e:
            print(f"Error Loading Dataset: {e}")
            return None

    def split_data(self,data):
        """
        Split the Dataset into Training and Testing Sets
        """
        try:
            train_data,test_data = train_test_split(
                data,test_size=self.test_size,
                random_state=self.random_state)
            print('Data Split into Training and Testing Sets')
            return train_data, test_data
        except Exception as e:
            print(f"Error Splitting Dataset: {e}")
            return None
            
    def save_data(self,train_data,test_data,train_path=TRAIN_DATA_FILE,test_path=TEST_DATA_FILE):
        """
        Saving the Training and Testing Datasets to CSV files
        """
        try:
            train_data.to_csv(train_path,index=False)
            test_data.to_csv(test_path,index=False)
        except Exception as e:
            
            print(f'Error Saving the Training and Testing Data.')


