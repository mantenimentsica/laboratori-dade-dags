from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "send_email-0629120258",
}

dag = DAG(
    "send_email-0629120258",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using send_email.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_b9db174e_117a_45d3_a304_2d37c56d7add = NotebookOp(
    name="Hello_World_R",
    namespace="default",
    task_id="Hello_World_R",
    notebook="notebooks/examples/Hello World R.ipynb",
    cos_endpoint="http://172.30.0.18:9000",
    cos_bucket="jupyer-pre",
    cos_directory="send_email-0629120258",
    cos_dependencies_archive="Hello World R-b9db174e-117a-45d3-a304-2d37c56d7add.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="jupyter/r-notebook",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "miniopass",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)


notebook_op_f9b30289_fcf5_40cc_a5fb_063e89d3c5fa = NotebookOp(
    name="send_email",
    namespace="default",
    task_id="send_email",
    notebook="scripts/examples/send_email.py",
    cos_endpoint="http://172.30.0.18:9000",
    cos_bucket="jupyer-pre",
    cos_directory="send_email-0629120258",
    cos_dependencies_archive="send_email-f9b30289-fcf5-40cc-a5fb-063e89d3c5fa.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="continuumio/anaconda3:2020.07",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "miniopass",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

(
    notebook_op_f9b30289_fcf5_40cc_a5fb_063e89d3c5fa
    << notebook_op_b9db174e_117a_45d3_a304_2d37c56d7add
)
