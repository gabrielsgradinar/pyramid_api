from pyramid.httpexceptions import HTTPBadRequest
from json.decoder import JSONDecodeError
import transaction
from typing import List
from pyramid.request import Request
from pyramid_api.models.country import Country, DBSession
from pyramid_api.api.schemas.country import CountrySchema


def create_country(request: Request) -> Country:

    country_request = request.json_body

    new_country = Country(
        name=country_request['name'], 
        official_language=country_request['official_language'],
        population=country_request['population']
    )

    #with transaction.manager:
    DBSession.add(new_country)

    return country_request['name'] 


def list_countries() -> List[Country]:

    countries = DBSession.query(Country).all()

    return CountrySchema().dump(countries, many=True)

def get_country(request: Request) -> Country:
    id = request.matchdict.get('id', "")

    country = DBSession.query(Country).filter_by(id=id).one()

    return CountrySchema().dump(country)

def update_country(request: Request) -> Country:
    
    id = request.json_body['id']

    for campo in request.json_body:
        if campo == "" or campo == "id":
            del campo

    campos = request.json_body

    with transaction.manager:
        DBSession.query(Country).filter(Country.id == id).update(campos)


    return CountrySchema().dump(
        DBSession.query(Country).filter_by(id=id).one()
    )

def delete_country(request: Request):

    try:
        country_id = request.json_body['id']
    except JSONDecodeError:
        raise HTTPBadRequest("Id cannot be null")

    with transaction.manager:
        deleted = DBSession.query(Country).filter(Country.id == country_id).delete()

    if deleted == 0:
        raise HTTPBadRequest(f"No contry to delete with id {country_id}")
    
    return deleted