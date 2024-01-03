## 102: Data Pipelines using DVC

### Overview
DVC pipelines are seamlessly integrated with Git, providing an efficient way to organize and version your projects. By leveraging the power of Git, you can capture and reproduce entire workflows and results at your convenience.

### Features
- `Versioned Pipelines:` Git-DVC enables versioning for pipelines, allowing you to track changes systematically.

- `Organized Projects:` Whether it's a simple ETL workflow or a complex DAG pipeline, Git-DVC helps you maintain a structured and organized project.

### Getting Started
I am currently working on the `Red Wine Quality` dataset. These datasets involve the red and white variants of the Portuguese "Vinho Verde" wine, presenting classification or regression tasks.

### Input variables (based on physicochemical tests):
- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol

### Output variable (based on sensory data):
- quality (score between 0 and 10)

**Goal:** The objective of this project is to create a robust data pipeline using DVC. This pipeline will involve:
1. **Data Preparation:** Clean and preprocess the red wine dataset to ensure it's ready for training.
2. **Model Training:** Develop a machine learning model using the prepared data to predict wine quality.
3. **Model Evaluation:** Assess the model's performance and accuracy in predicting wine quality.

Through the use of a DVC pipeline, we aim to achieve not only a well-organized and versioned project but also a reproducible and scalable workflow for future enhancements and experiments.

#### Step 1. Install the DVC library
```
pip install dvc
```

#### Step 2: Initialize DVC
``` 
dvc init
```
