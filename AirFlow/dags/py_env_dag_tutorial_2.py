from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import ExternalPythonOperator

with DAG(dag_id="py_env_dag_tutorial_2",
         start_date=datetime(2021,1,1),
         schedule_interval="@hourly",
         catchup=False) as dag:

    @task.external_python(task_id="external_python", python="/usr/bin/python")
    def callable_external_python():
        """
        Example function that will be performed in a virtual environment.

        Importing at the module level ensures that it will not attempt to import the
        library before it is installed.
        """
		
        """
        # following codes using print with f"" and flush only works in python > 3.x
        # these don't work in pythn <3
        import sys
        from time import sleep
        
        print(f"Running task via {sys.executable}")
        print("Sleeping")
        for _ in range(4):
            print("Please wait...", flush=True)
            sleep(1)
        print("Finished")
        """
		
        # The following codes works in python version 2.x
        import sys
        from time import sleep
        
        print("Following is the python executable path")
        print(sys.executable)
        print("Sleeping")
        for _ in range(4):
            print("Please wait...")
            sleep(1)
        print("Finished")
        
    external_python_task = callable_external_python()
	
	# external_classic = ExternalPythonOperator(
	#	task_id="external_python_classic",
	#	python=PATH_TO_PYTHON_BINARY,
	#	python_callable=x,
        #)
external_python_task
