# PASSO A PASSO DO PROJETO:
## CONFIGURAR O AMBIENTE DE DESENVOLVIMENTO:
* 1º passo: `python -m venv venv` //criação do ambiente virtual,
* 2º passo: `venv/Scripts/activate` //ativar ambiente virtual,
* 3º passo: `pip install django` //instalar django no ambiente virtual, 
* 4º passo: `django-admin startproject pontos_turisticos .` //criar o projeto django,
* 5º passo: `python manage.py migrate` //rodar as migrações do banco de dados,
* 6º passo: `python manage.py createsuperuser` //criar usuário admin pra acessar banco de dados,
* 7º passo: `python manage.py runserver` //rodar o servidor,

## CONFIGURAR O DJANGO REST FRAMEWORK NO PROJETO:
* 1º passo: `pip install djangorestframework` //instalar o framework django rest,
* 2º passo: adicionar em `pontos_turisticos/settings.py/INSTALLED_APPS`: 'rest_framework',

## CRIANDO E CONFIGURANDO OS APPS DO PROJETO:

### CONFIGURANDO O APP ATRACOES
* 1º passo: `python manage.py startapp atracoes` //iniciar app atracoes,
* 2º passo: adicionar em `pontos_turisticos/settings.py/INSTALLED_APPS`: 'atracoes',
* 3º passo: criar a Model Atracao em `atracoes/models.py`,
* 4º passo: registrar a Model Atracao no `atracoes/admin.py`,
* 5º passo: `python manage.py makemigrations` e `python manage.py migrate` //fazer as migrações no terminal,
* 6º passo: criar pasta api em atracoes,
* 7º passo: criar os arquivos `viewsets.py` e `serializers.py` em `atracoes/api`, 

### CONFIGURANDO O APP CORE
* 1º passo: `python manage.py startapp core` //iniciar app core,
* 2º passo: adicionar em `pontos_turisticos/settings.py/INSTALLED_APPS`: 'core',
* 3º passo: criar a Model PontosTuristicos em `core/models.py`,
* 4º passo: registrar a Model PontosTuristicos no `core/admin.py`,
* 5º passo: `python manage.py makemigrations` e `python manage.py migrate` //fazer as migrações no terminal,
* 6º passo: criar pasta api em core,
* 7º passo: criar os arquivos `viewsets.py` e `serializers.py` em `core/api`, 

### CONFIGURANDO O APP COMENTARIOS
* 1º passo: `python manage.py startapp comentarios` //iniciar app comentarios,
* 2º passo: adicionar em `pontos_turisticos/settings.py/INSTALLED_APPS`: 'comentarios',
* 3º passo: criar a Model Comentarios em `comentarios/models.py`,
* 4º passo: registrar a Model Comentarios no `comentarios/admin.py`,
* 5º passo: `python manage.py makemigrations` e `python manage.py migrate` //fazer as migrações no terminal,
* 6º passo: criar pasta api em comentarios,
* 7º passo: criar os arquivos `viewsets.py` e `serializers.py` em `comentarios/api`, 

### CONFIGURANDO O APP AVALIACOES
* 1º passo: `python manage.py startapp avaliacoes` //iniciar app avaliacoes,
* 2º passo: adicionar em `pontos_turisticos/settings.py/INSTALLED_APPS`: 'avaliacoes',
* 3º passo: criar a Model Avaliacoes em `avaliacoes/models.py`,
* 4º passo: registrar a Model Avaliacoes no `avaliacoes/admin.py`,
* 5º passo: `python manage.py makemigrations` e `python manage.py migrate` //fazer as migrações no terminal,
* 6º passo: criar pasta api em avaliacoes,
* 7º passo: criar os arquivos `viewsets.py` e `serializers.py` em `avaliacoes/api`, 

### CONFIGURANDO O APP ENDERECOS
* 1º passo: `python manage.py startapp enderecos` //iniciar app enderecos,
* 2º passo: adicionar em `pontos_turisticos/settings.py/INSTALLED_APPS`: 'enderecos',
* 3º passo: criar a Model enderecos em `enderecos/models.py`,
* 4º passo: registrar a Model enderecos no `enderecos/admin.py`,
* 5º passo: `python manage.py makemigrations` e `python manage.py migrate` //fazer as migrações no terminal,
* 6º passo: criar pasta api em enderecos,
* 7º passo: criar os arquivos `viewsets.py` e `serializers.py` em `enderecos/api`, 


## CONFIGURANDO AS ROTAS DAS URLS (ENDPOINTS) PARA OS APPS CRIADOS ACIMA
* 1º passo: adicionar em `urls.py` os routers,
* 2º passo: configurar os viewsets e serializers,
* 3º passo: importar em `urls.py` o viewset e serializer configurado,
* 4º passo:
* 5º passo:



### TODO: CRIAR APPS CONFORME FOR AVANÇANDO NO PROJETO
