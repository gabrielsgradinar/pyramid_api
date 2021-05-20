from marshmallow import Schema, fields


class CountrySchema(Schema):
    class Meta:
        ordered = True 

    name = fields.Str()
    official_language = fields.Str()
    population = fields.Int()
