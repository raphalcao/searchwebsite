Sistema de busca desenvolvido em python, no framework django com conexão ao MongoDB.

Para o MongoDB foi utilizado o software Robo 3T (https://robomongo.org/).

A rota ('/') é a tela inicial, com um campo de busca. Caso a busca retorne resultado, o mesmo aparecerá abaixo do campo.

A rota('/search/') retorna um json, gerado através do framework rest-framework com todos os dados cadastrados na base de dados.



Atualização


IMPLEMENTANDO O DOCKER

Para criar o arquivo de imagem, utilizar o seguinte comando:

docker build -t <nome da imagem>

Ex: docker build -t docker-search

