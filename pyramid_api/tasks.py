from datetime import datetime
from time import sleep
from pyramid_celery import celery_app as app

@app.task
def print_datetime():
    sleep(5)
    return datetime.now()