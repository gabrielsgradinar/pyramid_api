from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPBadRequest, HTTPError, HTTPOk
import logging
from pyramid_api.models import (
    create_country,
    delete_country,
    get_country,
    list_countries,
    update_country,
)

logging = logging.getLogger(__name__)


@view_defaults(renderer="json")
class CountryViews:
    def __init__(self, request) -> None:
        self.request = request

    @view_config(route_name="hello", request_method="GET")
    def hello(self):

        return HTTPOk("Wellcome to Pyramid Countries API")

    @view_config(route_name="create", request_method="POST")
    def create_country(self):
        logging.debug("Na view create")

        country = create_country(self.request)
        return {"content": "Created !!", "result": country}

    @view_config(route_name="get", request_method="GET")
    def get_country(self):
        logging.debug("Na view get")

        countries = get_country(self.request)
        return {"content": "Ok", "result": countries}

    @view_config(route_name="get_list", request_method="GET")
    def get_countries(self):
        logging.debug("Na view get_list")

        countries = list_countries()
        return {"content": "Ok", "result": countries}

    @view_config(route_name="update", request_method="PUT")
    def update_country(self):
        logging.debug("Na view update")

        updated_country = update_country(self.request)
        return {"content": "Updated !!", "result": updated_country}

    @view_config(route_name="delete", request_method="DELETE")
    def delete_country(self):
        logging.debug("Na view delete")

        try:
            deleted_country = delete_country(self.request)
        except HTTPError as e:
            return HTTPBadRequest(e.message)

        return {"content": "Deleted !!", "body": deleted_country}


def country_include(config):
    config.add_route("hello", "/")
    config.add_route("create", "/create")
    config.add_route("get", "/get/{id}")
    config.add_route("get_list", "/get")
    config.add_route("update", "/update")
    config.add_route("delete", "/delete")
