import joblib
import pandas as pd
import yaml
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


# Training function
def train(config):
    print("Training....")
    # Reading the train data
    train_data = pd.read_csv(config["data"]["train_csv_save_path"])

    # Splitting the features and label into X and y respectively
    X = train_data.iloc[:, :-1]
    y = train_data["good-quality"].values

    # Get the model selected in config file and hyperparameter with respect to the model selected
    model_name = config["train"]["model_choice"]
    model_hyperparameters = config["train"][model_name]

    # Train the model based on the model choice
    if model_name == "logistic_regression":
        model = LogisticRegression(
            penalty=model_hyperparameters["penalty"],
            C=model_hyperparameters["C"],
            solver=model_hyperparameters["solver"],
        )
        model.fit(X, y)
    elif model_name == "svm":
        model = SVC(
            kernel=model_hyperparameters["kernel"],
            C=model_hyperparameters["C"],
            degree=model_hyperparameters["degree"],
            gamma=model_hyperparameters["gamma"],
        )
        model.fit(X, y)
    else:
        model = KNeighborsClassifier(
            n_neighbors=model_hyperparameters["nearest_neighbors"]
        )
        model.fit(X, y)

    # Save the model
    joblib.dump(model, config["train"]["model_save_path"])


# Main function
def main():
    # Reading the params file
    with open("params.yaml", "r") as file:
        config = yaml.safe_load(file)
        train(config=config)


if __name__ == "__main__":
    main()
