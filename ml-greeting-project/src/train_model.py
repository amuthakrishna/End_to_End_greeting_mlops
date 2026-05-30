import os
import joblib
import boto3
import pandas as pd
import mlflow
import mlflow.sklearn

from datetime import datetime

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def upload_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client("s3")

    s3.upload_file(
        Filename=file_path,
        Bucket=bucket_name,
        Key=s3_key
    )

    print(f"Uploaded to S3: s3://{bucket_name}/{s3_key}")


def train(input_file_path, output_dir):

    bucket_name = "greeting-model-s3"

    mlflow.set_experiment("Model Training")

    # Load dataset
    data = pd.read_csv(input_file_path)

    X = data["text"]
    y = data["label"]

    pipeline = Pipeline([
        ("vect", CountVectorizer()),
        ("clf", MultinomialNB())
    ])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_filename = f"intent_model_{timestamp}.pkl"

    os.makedirs(output_dir, exist_ok=True)

    output_file_path = os.path.join(output_dir, model_filename)

    with mlflow.start_run():

        pipeline.fit(X, y)

        y_pred = pipeline.predict(X)

        accuracy = accuracy_score(y, y_pred)

        joblib.dump(pipeline, output_file_path)

        mlflow.log_param("model", "MultinomialNB")
        mlflow.log_param("vectorizer", "CountVectorizer")
        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(
            sk_model=pipeline,
            artifact_path="intent_model"
        )

        s3_key = f"models/{model_filename}"

        try:
            upload_to_s3(output_file_path, bucket_name, s3_key)
        except Exception as e:
            print(f"S3 Upload Failed: {e}")

        print("\nModel Training Completed")
        print(f"Accuracy: {accuracy:.2f}")
        print(f"Saved locally at: {output_file_path}")
        print(f"S3: s3://{bucket_name}/{s3_key}")


if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_path = os.path.join(base_dir, "data", "clean_data.csv")
    model_dir = os.path.join(base_dir, "model")

    train(input_path, model_dir)