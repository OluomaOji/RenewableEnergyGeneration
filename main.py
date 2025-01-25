from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataPreprocessing
from params import FILE_PATH, TRAIN_DATA_FILE, TEST_DATA_FILE,PROCESSED_TRAIN_DATA_FILE

def main():
    # Initialize DataIngestion with parameters from params.py
    data_ingestion = DataIngestion(file_path=FILE_PATH)
    
    # Load the data
    data = data_ingestion.load_data()
    if data is not None:
        # Split the data into training and testing sets
        train_data, test_data = data_ingestion.split_data(data)
        if train_data is not None and test_data is not None:
            # Save the split data
            data_ingestion.save_data(train_data, test_data, train_path=TRAIN_DATA_FILE, test_path=TEST_DATA_FILE)

# Initialize Preprocessor
    preprocessor = DataPreprocessing()

    # Handle Missing Values
    data = preprocessor.handle_missing_values(data)

    # Handle Negative Power Values
    data = preprocessor.handle_negative_power(data)

    # Encode Categorical Features
    data = preprocessor.encode_categorical(data)

    # Scale Numerical Features
    data = preprocessor.scale_features(data)

    # Save Preprocessed Data
    if data is not None:
        data.to_csv('Dataset/preprocessed_data.csv', index=False)
        print('Preprocessed data saved.')

    # Save the preprocessed data
    if data is not None:
        data.to_csv(PROCESSED_TRAIN_DATA_FILE, index=False)
        print(f"Preprocessed data saved to {PROCESSED_TRAIN_DATA_FILE}")
    

if __name__ == "__main__":
    main()
