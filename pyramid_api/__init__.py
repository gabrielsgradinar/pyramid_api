__version__ = '0.1.0'

from pyramid_api.views import country_include
from pyramid_api.models import Base, DBSession
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.add_route('welcome', '/')
    config.include(country_include, route_prefix='/countries')
    config.scan()
    
    return config.make_wsgi_app()