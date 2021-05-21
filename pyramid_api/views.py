import logging
from pyramid_api.models import Country
from pyramid_api.schemas import CountrySchema
from pyramid_api.controller import (
    create_country,
    delete_country, 
    get_country, 
    list_countries, 
    update_country
)
log = logging.getLogger(__name__)

from pyramid.view import view_config, view_defaults
from cornice import Service
from cornice.validators import marshmallow_body_validator

countries = Service(name='country', path='/country', description="Country CRUD")


@countries.post(
    accept='application/json',
    schema=CountrySchema,
    validators=(marshmallow_body_validator,)
)
def create_country_cornice(request):

    country = Country(
       name=request.validated['name'],
       official_language=request.validated['official_language'],
       population=request.validated['population'],
       currency=request.validated['currency'],
    )

    return CountrySchema().dump(country)

@view_defaults(renderer='json')
class CountryViews:
    def __init__(self, request) -> None:
        self.request = request

    @view_config(route_name='create', request_method='POST')
    def create_country(self):
        log.debug('Na view create')

        country = create_country(self.request)
        return {
            'content':'Created !!',
            'result': country
        }

    @view_config(route_name='get',request_method='GET')
    def get_country(self):
        log.debug('Na view get')
        countries = get_country(self.request)
        return {
            'content':'Ok',
            'result': countries
        }

    @view_config(route_name='get_list',request_method='GET')
    def get_countries(self):
        log.debug('Na view get_list')
        countries = list_countries()
        return {
            'content':'Ok',
            'result': countries
        }

    @view_config(route_name='update',request_method='PUT')
    def update_country(self):
        log.debug('Na view update')

        updated_country = update_country(self.request)
        return {
            'content': 'Updated !!',
            'result': updated_country
        }

    @view_config(route_name='delete',request_method='DELETE')
    def delete_country(self):
        log.debug('Na view delete')

        deleted_country = delete_country(self.request)
        return{
            'content': 'Deleted !!',
            'body': deleted_country
        }


def country_include(config):
    config.add_route('create', '/create')
    config.add_route('get', '/get/{id}')
    config.add_route('get_list', '/get')
    config.add_route('update', '/update')
    config.add_route('delete', '/delete')