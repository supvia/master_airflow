"""Example DAG using BashOperator."""
import datetime
import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",  # Midnight every day. Cron schedule expression.
    start_date=pendulum.datetime(2025, 10, 1, tz="Asia/Seoul"),  # Remember to set your timezone(e.g., Asia/Seoul, UTC).
    catchup=False,  # Do not perform backfill. NOTE: If this field is true, it doesn't run parallelly.
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],  # For searching purposes in the Airflow UI.
    params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    bash_t1 >> bash_t2
