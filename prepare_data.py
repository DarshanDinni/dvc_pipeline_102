import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

# Function to prepare the data for training
def prepare_data(config):
    print("Preparing data")

    # Reading the data through yaml file
    data = pd.read_csv(config['data']['csv_file_path'])
    
    # Data manipulation
    data['quality'] = data['quality'].apply(lambda x: 1 if x >= 7 else 0)
    data.rename(columns={'quality': 'good-quality'}, inplace=True)
    
    # Spliting the data into train and test data
    train_data, test_data = train_test_split(data, test_size=config['data']['test_set_ratio'], 
                                            random_state=42)
    
    # Saving the train and test to file
    train_data.to_csv(config['data']['train_csv_save_path'], index=False)
    test_data.to_csv(config['data']['test_csv_save_path'], index=False)

# Main function
if __name__ == "__main__":
    # Reading the params file
    with open('params.yaml', 'r') as file:
        config = yaml.safe_load(file)
        prepare_data(config=config)