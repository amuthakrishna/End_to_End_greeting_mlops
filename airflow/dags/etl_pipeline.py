from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

# Container path
sys.path.append("/opt/airflow/ml-project/src")

from data_ingestion import load_data
from data_preparation import prepare_data
from train_model import train

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
}

with DAG(
    dag_id="ml_etl_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
) as dag:

    ingestion_task = PythonOperator(
        task_id="data_ingestion",
        python_callable=load_data,
        op_args=[
            "/opt/airflow/ml-project/data/raw_data.csv"
        ]
    )

    preparation_task = PythonOperator(
        task_id="data_preparation",
        python_callable=prepare_data,
        op_args=[
            "/opt/airflow/ml-project/data/raw_data.csv",
            "/opt/airflow/ml-project/data/clean_data.csv"
        ]
    )

    training_task = PythonOperator(
        task_id="model_training",
        python_callable=train,
        op_args=[
            "/opt/airflow/ml-project/data/clean_data.csv",
            "/opt/airflow/ml-project/model"
#            "/opt/airflow/ml-project/model/intent_model.pkl"
        ]
    )

    ingestion_task >> preparation_task >> training_task