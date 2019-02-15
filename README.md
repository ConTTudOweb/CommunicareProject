# CommunicareProject

[![Build Status](https://travis-ci.org/ConTTudOweb/CommunicareProject.svg?branch=master)](https://travis-ci.org/ConTTudOweb/CommunicareProject)


## Como desenvolver?

01. Clone o repositorio;
02. Crie uma env com Python 3;
03. Instale as dependências;
04. Ative a env;
05. Configure a instancia com o .env;
06. Crie a tabela de cache;
07. Rode os testes;
08. Aplique as migrações e crie o banco;
09. Crie o superuser;
10. Execute o servidor.

```console
git clone https://github.com/ConTTudOweb/ConTTudOwebProject.git
cd ConTTudOwebProject
pipenv --three
pipenv install
pipenv shell
cp contrib/env-sample .env
python manage.py createcachetable
python manage.py test
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


## Como rodar o projeto para trabalhar no Frontend?

1. Navegue até a pasta pelo terminal;
4. Ative a env;
9. Execute o servidor.

```console
cd ConTTudOwebProject
pipenv shell
python manage.py runserver
```