from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

def download_data():
    # Codigo para download de dados do GCS ou Pub/Sub
    pass

def process_data():
    # Codigo para processamento de dados usando Dataflow
    pass

def update_dashboard():
    # Codigo para atualizar dashboards com dados do BigQuery
    pass

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='Pipeline de dados completo',
    schedule_interval='@daily',
)

t1 = PythonOperator(
    task_id='download_data',
    python_callable=download_data,
    dag=dag,
)

t2 = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

t3 = PythonOperator(
    task_id='update_dashboard',
    python_callable=update_dashboard,
    dag=dag,
)

t1 >> t2 >> t3
