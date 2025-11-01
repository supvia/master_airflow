"""Python Task Decorator Example"""
from airflow.sdk import dag, task

@dag(
    dag_id="task_decorator",
    tags=["inflearn"],
)
def python_task_decorator():
    @task(task_id="print_context")
    def print_context(some_input):
        print(some_input)
        return

    python_task_1 = print_context('task_decorator 실행')

python_task_decorator()
