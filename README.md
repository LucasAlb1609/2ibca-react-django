# Site da Segunda Igreja Batista em Casa Amarela (Versão React + Django)

Este repositório contém o código-fonte da nova versão do site da 2IBCA, construído com uma arquitetura moderna utilizando React para o frontend e Django (REST Framework) para o backend.

## Tecnologias Utilizadas

* **Frontend:** React, Vite, Tailwind CSS, React Router
* **Backend:** Python, Django, Django REST Framework
* **Banco de Dados:** SQLite (desenvolvimento), PostgreSQL (produção - a definir)

## Como Rodar o Projeto Localmente

### Backend (Django)
1.  Navegue até a pasta `igreja_back`.
2.  Crie e ative um ambiente virtual.
3.  Instale as dependências: `pip install -r requirements.txt`
4.  Execute as migrações: `python manage.py migrate`
5.  Inicie o servidor: `python manage.py runserver`

### Frontend (React)
1.  Navegue até a pasta `2ibca`.
2.  Instale as dependências: `npm install`
3.  Inicie o servidor de desenvolvimento: `npm run dev`

## Estrutura do Repositório

-   `/2ibca`: Contém todo o código do frontend em React.
-   `/igreja_back`: Contém todo o código do backend em Django.