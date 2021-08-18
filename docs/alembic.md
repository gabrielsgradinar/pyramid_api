# Alembic

 - Fornece a criação, gerenciamento e utilização de scripts para as mudanças no banco de dados.
 - Usa o SQLAlchemy como base.

## Instalando Alembic

     - `poetry add alembic` - faz a instalação do pacote com o poetry

## Comandos Alembic

- `alembic init alembic` - cria o diretório das migrações chamado alembic e o arquivo de confuguração alembic.ini .
    - O diretório tem essa carinha:
        ```
        alembic
        |____env.py
        │____README.md
        │____fscript.py.mako  
        │
        └───versions
            │____migration_script_01.py

        ```
    - No arquivo .ini temos que configurar a conexão com o banco mudando o `sqlalchemy.url` com a url correta. ex: 
        ```
        sqlalchemy.url = mysql+mysqldb://root:root@localhost:3306/database_name
        ```
- `alembic revision -m "descrição da migração"` - cria o arquivo com o script da migração, dentro da pasta versions, ex: 1975ea83b712_descricao_da_migracao.py.
    - Nesse arquivo que é descrito oque vai acontecer na migração, a definição das tabelas do banco e suas expecificações, o arquivo tem essa cara:
        ```py
        revision = '1975ea83b712'
        down_revision = None
        branch_labels = None

        from alembic import op
        import sqlalchemy as sa

        def upgrade():
            pass

        def downgrade():
            pass

        ```
      - A função `upgrade` é onde definimos as tabelas que serão criadas e quais alterações seram aplicadas na migração.
      - No `downgrade` é definido oque acontecera ao voltarmos de uma versão mais atual das tabelas para essa versão.
      - Como o Alembic sabe para qual versão voltar ao fazer o downgrade ?
        Ao criar uma nova migração a variavel `down_revision` será preenchida com o id da ultima migração.

- `alembic revision — autogenerate -m "descrição da migração"` - cria o arquivo de revisão com base nos modelos do SQlAlchemy criados em outra parte do código.
    - Para fazer isso é preciso alterar a variável `target_metadata` no arquivo env.py do diretório alembic, passando um objeto de metadados de uma tabela criada.
    ```py
    from mymodel import Base
    target_metadata = [Base.metadata]
    ```
    - Esse `Base` contem o objeto `MetaData` que contem os objetos `Table` que definem o bando de dados.
  
- `alembic upgrade head` - Axecuta a migração da revisão mais recente do banco (`head`) com tudo oque foi definido na função `upgrade` do script.
- `alembic history --verbose` - mostra os histórico das migrações com vários detalhes, como a descrição e a data de criação da revisão.