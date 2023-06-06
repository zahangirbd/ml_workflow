from datetime import datetime
from textwrap import dedent

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def helloWorld():
    print("Hello World")
	
with DAG(dag_id="my_dag_tutorial_1",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:
		 
		 t1 = PythonOperator(
			task_id="hello_world",
			python_callable=helloWorld,
		 )
		 
		 t2 = BashOperator(
			task_id="print_date",
			bash_command="date",
		 )
		 
		 templated_command = dedent(
			"""
			{% for i in range(5) %}
				echo "{{ ds }}"
				echo "{{ macros.ds_add(ds, 7)}}"
			{% endfor %}
			"""
		 )

		 t3 = BashOperator(
			task_id="templated",
			depends_on_past=False,
			bash_command=templated_command,
		 )
t1 >> [t2, t3]
