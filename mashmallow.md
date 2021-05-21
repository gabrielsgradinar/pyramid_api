# Mashmallow
 - É independente do ORM/Framework utilizado
 - Fornece validação de dados de entrada.
 - Desserialização dos dados de entrada para os objetos da aplicação.
 - Serialização dos objetos da aplicação para tipos primitivos do Python, como a utilização para retornar objetos JSON em uma API.
 

## Instalando Alembic

     - poetry add marshmallow

## Utilização

 - Criando primeiro `shema`
    ```py
    from marshmallow import Schema, fields
    
    class CountrySchema(Schema):

        name = fields.Str()
        official_language = fields.Str()
        population = fields.Int()
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

# Validação nas APIs - Mashmallow + Cornice

# Introdução rápida ao Cornice 🚴

 - É um framework REST para o Pyramid
 - Ele possui vários modulos para ajudar na criação e na documentação de REST APIs


  