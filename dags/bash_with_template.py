from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import dag, task

@dag(
    dag_id="with_template",
    tags=["inflearn"]
)
def with_template():
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo "data_interval_end: {{ data_interval_end }}"",
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        env={
            'START_DATE':'{{data_interval_start | ds }}',
            'END_DATE':'{{data_interval_end | ds }}'
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    bash_t1 >> bash_t2

with_template()
