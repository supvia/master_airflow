from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_import_func",
    tags=["inflearn"]
):
    task_get_sftp = PythonOperator(
        task_id="task_get_sftp",
        python_callable=get_sftp
    )
