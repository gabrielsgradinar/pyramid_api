from marshmallow import Schema, fields


class CountrySchema(Schema):
    class Meta:
        ordered = True 

    name = fields.Str(required=True)
    official_language = fields.Str(required=True)
    population = fields.Integer(required=True)
    currency = fields.Str(required=True)
