import logging
from typing import Dict

import transaction

from pyramid_api.models.country import Country, DBSession
from time import sleep

from pyramid_celery import celery_app as app

logger = logging.getLogger(__name__)

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]
    
@app.task
def create_country_task(country_request: Dict):
    sleep(10)
    
    new_country = Country(
        name=country_request['name'], 
        official_language=country_request['official_language'],
        population=country_request['population']
    )

    with transaction.manager:
        DBSession.add(new_country)