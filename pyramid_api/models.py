from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql.sqltypes import BigInteger, Float
from zope.sqlalchemy import register
from marshmallow import Schema, fields


DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    official_language = Column(Text)
    population = Column(BigInteger)
    currency = Column(Text)

    def __init__(self, name, official_language, population, currency) -> None:
        self.name = name
        self.official_language = official_language
        self.population = population
        self.currency = currency


class CountrySchema(Schema):
    class Meta:
        ordered = True 

    name = fields.Str()
    official_language = fields.Str()
    population = fields.Int()
