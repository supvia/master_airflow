import pendulum
import random

from airflow.providers.standard.operators.python import PythonOperator
from airflow.sdk import DAG

with DAG(
    dag_id="python_operator",
    schedule=None,
    tags=["inflearn"],
    catchup=False,
) as dags:
    def select_fruit():
        fruit = ["APPLE", "BANANA", "ORANGE", "AVOCADO"]
        rand_int = random.randint(0, len(fruit) - 1)
        print(f"Selected fruit: {fruit[rand_int]}")
    
    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit
    )
    
    py_t1
