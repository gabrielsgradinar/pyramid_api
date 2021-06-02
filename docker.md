# Docker

## Conceitos

### Container
    É um ambiente completamente isolado que contém tudo oque é preciso para rodar uma aplicação. Ele é totalmente independente do que está instalado ou não instalado no computador ou no sistema operacional.

### Dockerfile
    O Dockerfile nada mais é do que um meio que utilizamos para criar nossas próprias imagens. Em outras palavras, ele serve como a receita para construir um container, permitindo definir um ambiente personalizado para a aplicação

### Image
    - Comando para buildar a imagem a partir do Dockerfile: docker build -t "nome_da_imagem" caminho_da_pasta_onde_o_dockerfile_esta
    - 