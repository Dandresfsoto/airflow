import time
from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from klym_telemetry.instrumenters import instrument_app

from src.dummy_class import DummyClass


def run_telemetry_task():
    """
    Executes the parsing process.
    """
    instrument_app(app_type="airflow", service_name="dag", endpoint="http://collector:4317")
    DummyClass()
    time.sleep(10)


# Dag config:
default_args = {
    'owner': 'business.intelligence',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 3,
    'retry_delay': timedelta(seconds=5)
}


with DAG(
        dag_id="instrumented_dag_example",
        catchup=False,
        default_args=default_args,
        schedule_interval=None,
) as dag:

    execute_parser = PythonOperator(
        task_id="instrumented_dag_example_task",
        provide_context=True,
        python_callable=run_telemetry_task,
    )
