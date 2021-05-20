import os
import sys
from pyramid_api.models import Base
from pyramid.paster import get_appsettings
from pyramid.scripts.common import parse_vars
from sqlalchemy import engine_from_config


def main():
    config_uri = sys.argv[1]
    options = parse_vars(sys.argv[2:])
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    if bool(os.environ.get('DEBUG', '')):
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)