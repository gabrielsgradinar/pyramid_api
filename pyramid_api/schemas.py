from marshmallow import Schema, fields


class CountrySchema(Schema):
    class Meta:
        ordered = True 

    name = fields.Str(required=True)
    official_language = fields.Str(required=True)
    population = fields.Int(required=True)