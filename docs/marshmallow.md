# Marshmallow
 - É independente do ORM/Framework utilizado
 - Fornece validação de dados de entrada.
 - Desserialização dos dados de entrada para os objetos da aplicação.
 - Serialização dos objetos da aplicação para tipos primitivos do Python, como a utilização para retornar objetos JSON em uma API.


## Instalando Marshmallow

     - poetry add marshmallow

## Utilização

 - Criando primeiro `Schema`
    ```py
    from marshmallow import Schema, fields

    class CountrySchema(Schema):

        name = fields.Str(required=True)
        official_language = fields.Str(required=True)
        population = fields.Int(required=True)
    ```
 - Serialização dos objetos
   - Para fazer a serialização de um objeto, passamos um objeto para a função `dump`, que retorna um json formatado
        ```py
        new_country = Country(
            name='Brasil',
            official_language='Português',
            population=211755692
        )

        country_schema = CountrySchema()
        result = country_schema.dump(new_country)

        # o resultado é esse
            {
                "name":"Brasil",
                "official_language": "Português",
                "population":211755692
            }

        ```
- Desserialização dos objetos
  - Para fazer o oposto do `dump` utilizadmos a função `load`, ele recebe um dicionário formatado (o mesmo que o JSON).
  - O `load` retorna por padrão um outro dicionário fazendo a desserialização dos valores e aplicando a validação dos campos de acordo com o `schema`, podendo retornar um `ValidationError`.
    ```py
    new_country = {
        "name":"Brasil",
        "official_language": "Português",
        "population": 211755692
    }

    country_schema = CountrySchema()
    result = country_schema.load(new_country)

    # caso não tenha nenhum erro na validação o resultado é esse
        {
            "name":"Brasil",
            "official_language": "Português",
            "population":211755692
        }

    ```
### Para serializar uma lista de objetos é so passar a flag many=True para a função `dump`, o mesmo funciona para desserializar com `load`.

# Validação nas APIs - Marshmallow + Cornice

## Introdução rápida ao Cornice 🚴

 - É um framework REST para o Pyramid
 - Ele possui vários modulos para ajudar na criação e na documentação de REST APIs


## Configurando cornice no pyramid

 - Adicionar o Cornice no Configurator
```py
config = Configurator(settings=settings)
config.include("cornice")
```
## Criando um serviço no Cornice usando a validação do Marshmallow

```py
from cornice import Service
from cornice.validators import marshmallow_body_validator


# Criação do Service
countries = Service(name='country', path='/country', description="Country CRUD")

# Utilizamos o Service criado como decorator para criar as funções de acordo com os verbos HTTP
# Então a partir do @countries podemos usar .get, .put, .post, etc.


# No decorator passamos o tipo do validador (marshmallow_body_validator) e qual o schema que será validado(CountrySchema)
# Assim caso o request não esteja em padrão com schema, será retornado um 400 formatado com o erro da validação, mostrando oque está errado
# Por exemplo, caso o campo population, que está como obrigatório no schema, não for passado
"""
    {
        "status": "error",
        "errors": [
            {
                "location": "body",
                "name": "population",
                "description": [
                    "Missing data for required field."
                ]
            }
        ]
    }
"""
# Os validares funcionam usando o dicionário request.validated
@countries.post(
    accept='application/json',
    schema=CountrySchema,
    validators=(marshmallow_body_validator,)
)
def create_country(request):

    country = Country(
       name=request.validated['name'],
       official_language=request.validated['official_language'],
       population=request.validated['population'],
       currency=request.validated['currency'],
    )

    return CountrySchema().dump(country)

```
