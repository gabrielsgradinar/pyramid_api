import transaction
from typing import List
from pyramid.request import Request
from pyramid_api.models import Country, CountrySchema, DBSession


def create_country(request: Request) -> Country:
    new_country = Country(
        name=request.json_body['name'], 
        official_language=request.json['official_language'],
        population=request.json['population']
    )

    with transaction.manager:
        DBSession.add(new_country)

    return CountrySchema().dump(
        DBSession.query(Country).filter_by(
            name=request.json_body['name']
        ).one()
    )


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
        DBSession.query(Country).filter_by(
            id=id
        ).one()
    )

def delete_country(request: Request):
    id = request.json_body['id']

    with transaction.manager:
        deleted = DBSession.query(Country).filter(Country.id == id).delete()
    return deleted