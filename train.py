import pandas as pd
import yaml
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


# Training function
def train(config):
    pass


if __name__ == "__main__":
    with open("params.yaml", "r") as file:
        config = yaml.safe_load(file)
        train(config=config)
