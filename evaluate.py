import joblib
import pandas as pd
import yaml
from sklearn.metrics import accuracy_score, f1_score


# Evaluate function
def evaluate(config):
    # Geting the name of evaluation metrics to be used from the config file
    metric_name = config["evaluate"]["metrics"]
    metrics = {"accuracy_score": accuracy_score, "f1_score": f1_score}[metric_name]

    # Load the trained model
    model = joblib.load(config["train"]["model_save_path"])

    # Read the test data
    test_data = pd.read_csv(config["data"]["test_csv_save_path"])

    # Split the test data into features and label
    test_features = test_data.iloc[:, :-1]
    test_label = test_data["good-quality"].values

    # Predict the output on the trained model
    predicted_output = model.predict(test_features)

    # Evaluate the model based on the metrics selected
    results = metrics(test_label, predicted_output)

    # Save the results to the directory
    with open(config["evaluate"]["evaluate_save_path"], "w") as file:
        results_dict = {metric_name: str(results)}
        yaml.safe_dump(results_dict, file)


# Main function
def main():
    # Reading the params file
    with open("params.yaml", "r") as file:
        config = yaml.safe_load(file)
        evaluate(config=config)


if __name__ == "__main__":
    main()
