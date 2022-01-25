__version__ = "0.1.0"

from pyramid_api.api.resources.country import country_include
from pyramid_api.models.country import Base, DBSession
from pyramid.config import Configurator
from sqlalchemy import engine_from_config


def main(global_config, **settings):
    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.configure_celery(global_config["__file__"])

    config.include("cornice")
    config.include("pyramid_celery")
    config.configure_celery(global_config["__file__"])

    config.include(country_include, route_prefix="/countries")
    config.scan()

    return config.make_wsgi_app()
