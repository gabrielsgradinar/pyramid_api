# Instalando poetry

 - Gestor de dependência que segue as expecificações do Python
 - Ele substitui a necessidade de arquivos como setup.py, requirements.txt, manifest.in e pipfile por apenas um arquivo, o pyproject.toml
 - Trabalha junto com o git
 - Possui um sistema legal de resolução de conflitos entre as dependências


Referências:

- <https://python-poetry.org/docs/>
- <https://www.youtube.com/watch?v=_XszPRFHQQ4>

## Linux

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

## Comandos poetry

- `poetry new nome_do_projeto` - cria um projeto com alguns arquivos necessários para o poetry
- `poetry env use 3.8` - inicializa um ambiente virtual com base na versão do python expecificado
- `poetry shell` - ativa o ambiente virtual
- `poetry add nome_do_pacote` - instala um pacote python e adiciona ele no arquivo pyproject.toml
- `poetry install` - ve se existe alguma dependência para ser atualizada
- `poetry export -f requirements.txt -o requirements.txt` - exporta as dependencias do poetry para o formato do requirements.txt
- `poetry search nome_do_pacote` - pesquisa tudo oque achar dentro do pypi
