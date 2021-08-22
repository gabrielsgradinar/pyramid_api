import logging
from time import sleep

from pyramid_celery import celery_app as app

logger = logging.getLogger(__name__)

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]
