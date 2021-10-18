import numpy as np
import pandas as pd
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from urllib.parse import urlparse

# tracking_uri = 'http://127.0.0.1:5000'
# mlflow.set_tracking_uri(tracking_uri)

# read csv
features = pd.read_csv('temps.csv')
features = pd.get_dummies(features)

labels = np.array(features['actual'])
features = features.drop('actual', axis=1)

feature_list = list(features.columns)
features = np.array(features)

# train test split
train_features, test_features, train_labels, test_labels = train_test_split(features,
                                                                            labels, test_size=0.25,
                                                                            random_state=42)

with mlflow.start_run():
    dtc = DecisionTreeClassifier(max_depth=3, random_state=42)
    dtc.fit(train_features, train_labels)

    predictions = dtc.predict(test_features)
    accuracy = metrics.accuracy_score(test_labels, predictions)

    mlflow.log_metric("accuracy", accuracy)
    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    # Model registry does not work with file store
    if tracking_url_type_store != "file":
        mlflow.sklearn.log_model(dtc, "model", registered_model_name="DecisionTreeClassifier")
    else:
        mlflow.sklearn.log_model(dtc, "model", registered_model_name="DecisionTreeClassifier")
