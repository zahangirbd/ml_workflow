from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

def callable_virtualenv():
	"""
	Example function that will be performed in a virtual environment.

	Importing at the module level ensures that it will not attempt to import the
	library before it is installed.
	"""
	from time import sleep

	from colorama import Back, Fore, Style

	print(Fore.RED + "some red text")
	print(Back.GREEN + "and with a green background")
	print(Style.DIM + "and in dim text")
	print(Style.RESET_ALL)
	for _ in range(4):
		print(Style.DIM + "Please wait...", flush=True)
		sleep(1)
	print("Finished")

with DAG(dag_id="py_env_dag_tutorial_1",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:

		# virtualenv_task = callable_virtualenv()
		virtual_classic = PythonVirtualenvOperator(
			task_id="virtualenv_classic",
			requirements="colorama==0.4.0",
			python_callable=callable_virtualenv,
		)
virtual_classic