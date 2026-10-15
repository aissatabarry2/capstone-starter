import mlflow
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("capstone")
with mlflow.start_run():
    clf = LogisticRegression(max_iter=200).fit(Xtr, ytr)
    mlflow.log_param("model", "logreg")
    mlflow.log_metric("accuracy", clf.score(Xte, yte))
