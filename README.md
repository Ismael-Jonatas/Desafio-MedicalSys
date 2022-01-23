# Desafio-MedicalSys

OBS: essas passos descritos abaixo foram feitos em sistema windows pelo poweshell. 

Forma de execução em localHost:

1) - bem o projeto tem o banco de dados postgresql, as configurações que usei para com meu banco de dados localhost foram as padrões:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'medicalBD',
        'USER': 'postgres',
        'PASSWORD': 'ifpb',
        'HOST': 'localhost'
    }
}
.

2) - o projeto está sendo executado em um ambiente virtual, foi instalado  uma venv no diretorio do projeto 
da seguinte forma com o comando "py -m venv ./venv".

- Em seguida foi dado start no ambiente virtual, comando utilizado "venv/Scripts/activate".

3) - depois da instalação e start da venv serem executados, foram instaladas as dependências do projeto, que podem ser lidas na pasta requeriments
no arquivo local.txt.

dependências instaladas:
- asgiref==3.4.1
- Django==4.0.1
- psycopg2==2.9.3
- psycopg2-binary==2.9.3
- sqlparse==0.4.2
- tzdata==2021.5

OBS: As dependências Django==4.0.1, sqlparse==0.4.2, tzdata==2021.5, asgiref==3.4.1, foram adiciondas quando foi instalado o django no ambiente virtual do projeto
com o comando "pip install django". As dependências psycopg2==2.9.3 e psycopg2-binary==2.9.3, foram instaladas apos a instalação do Django no ambiente virtual
com o comando: "pip install psycopg2", e depois "pip install psycopg2-binary". Essas ultimas dependências são para uso do banco de dados Postegresql.

4) - Por fim o projeto é executado no localhost utilizando o comando para iniciar o server local do projeto com o comando "py manage.py runserver".

OBS: o projeto também possui django admin instalado. comanado utilizado "pip install django-admin", no arquivo admin.py no diretorio do medicalApp/admin.py
está algumas configurações para uso do django-admin, não se esquecer de criar o user admin se caso venha usar o django-admin.
comando para criar o user admin é "py manage.py createsuperuser".
