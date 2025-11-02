import pendulum

from airflow.sdk import dag, task

@dag(
    dag_id="python_show_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 11, 1, tz="Asia/Seoul"),
    tags=["inflearn"],
    catchup=True
)
def python_show_template():
    @task(task_id="show_template")
    def show_template(**kkwargs):
        print(kkwargs)
        return
    
    show_template_task = show_template()

python_show_template()
