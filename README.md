# Site da Segunda Igreja Batista em Casa Amarela (React + Django)

Este repositório contém o código-fonte da nova versão do site da 2IBCA, construído com uma arquitetura moderna que utiliza React para o frontend e Django (REST Framework) para o backend.

## ✨ Tecnologias Principais

* **Frontend:** React, Vite, Tailwind CSS, React Router
* **Backend:** Python, Django, Django REST Framework
* **Banco de Dados:** SQLite (desenvolvimento)

---

## 📋 Pré-requisitos

Antes de começar, garanta que você tenha as seguintes ferramentas instaladas na sua máquina:
* [Python](https://www.python.org/downloads/) (versão 3.10 ou superior)
* [Node.js](https://nodejs.org/en/) (versão 18 ou superior)
* [Git](https://git-scm.com/downloads/)

---

## 🚀 Guia de Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

### 1. Clone o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO_AQUI>
cd 2ibca-react-django
```

### 2. Configuração do Backend (Django)

O backend requer um ambiente virtual isolado para gerenciar suas dependências.

1.  **Navegue até a pasta do backend:**
    ```bash
    cd igreja_back
    ```

2.  **Crie o ambiente virtual:**
    *Este passo cria uma pasta `venv` que conterá todas as bibliotecas Python específicas para este projeto, evitando conflitos com outros projetos.*
    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    * **No Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\activate
        ```
    * **No macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências Python:**
    *O arquivo `requirements.txt` contém a lista exata de pacotes necessários.*
    ```bash
    pip install -r requirements.txt
    ```

5.  **Crie as tabelas no banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um superusuário** para acessar o painel de administração:
    ```bash
    python manage.py createsuperuser
    ```
    *Siga as instruções para criar seu usuário e senha.*

### 3. Configuração do Frontend (React)

1.  **Abra um novo terminal.**
2.  **Navegue até a pasta do frontend:**
    ```bash
    cd 2ibca 
    ```
    *(A partir da pasta raiz `2ibca-react-django`)*

3.  **Instale as dependências JavaScript:**
    *O `package.json` gerencia todos os pacotes necessários para o React.*
    ```bash
    npm install
    ```

---

## 🏃 Como Rodar o Ambiente de Desenvolvimento

Para trabalhar no projeto, você precisará de **dois terminais rodando simultaneamente**.

**Terminal 1 - Rodando o Backend (Django):**
```bash
# Navegue até a pasta do backend
cd igreja_back

# Ative o ambiente virtual (se ainda não estiver ativo)
.\venv\Scripts\activate

# Inicie o servidor Django
python manage.py runserver
```
> ℹ️ O backend estará disponível em `http://127.0.0.1:8000/`.

**Terminal 2 - Rodando o Frontend (React):**
```bash
# Navegue até a pasta do frontend
cd 2ibca

# Inicie o servidor de desenvolvimento do Vite
npm run dev
```
> ℹ️ O frontend estará disponível em `http://localhost:5173/`. **É este o endereço que você deve abrir no seu navegador para ver o site.**

---

## 🌐 Acessos Importantes

* **Site (Visualização):** `http://localhost:5173/`
* **Painel de Administração (Conteúdo):** `http://127.0.0.1:8000/admin/'