Sistema de busca desenvolvido em python, no framework django com conexão ao MongoDB.

Para o MongoDB foi utilizado o software Robo 3T (https://robomongo.org/).

A rota ('/') é a tela inicial, com um campo de busca. Caso a busca retorne resultado, o mesmo aparecerá abaixo do campo.

A rota('/search/') retorna um json, gerado através do framework rest-framework com todos os dados cadastrados na base de dados.



Atualização #1


IMPLEMENTANDO O DOCKER

Para criar o arquivo de imagem, utilizar o seguinte comando:

docker build -t <nome da imagem>

Ex: docker build -t docker-search



Atualização #2

IMPLEMENTANDO TESTES AUTOMATIZADOS



Nesta atualização foram implementados testes automatizados.
Instalado o framework covarage e mommy

Para rodar os testes automatizados, executar o comando: coverage run manage.py test
Para exibir um relatório com os status dos relatórios, executar o comando coverage report

STATUS ATUAL DE TESTES 

Name                      Stmts   Miss  Cover
---------------------------------------------
search\urls.py                4      0   100%
search\views.py               0      0   100%
searchwebsite\models.py      10      0   100%
searchwebsite\views.py       15      6    60%
---------------------------------------------
TOTAL                        29      6    79%