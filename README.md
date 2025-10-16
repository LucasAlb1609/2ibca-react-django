# 🌐 Site da Segunda Igreja Batista em Casa Amarela (React + Django)

Este repositório contém o código-fonte da nova versão do site da **2ª Igreja Batista em Casa Amarela (2IBCA)**, desenvolvido com uma arquitetura moderna que combina **React (Vite + TailwindCSS)** no frontend e **Django REST Framework** no backend.

---

## ✅ Progresso da Migração

### Páginas Públicas
- [x] **Página Inicial (`/`)** - Concluída
- [x] **Página de História (`/historia`)** - Concluída
- [x] **Página de Liderança (`/lideranca`)** - Concluída
- [x] **Página de Departamentos (`/departamentos`)** - Concluída
- [x] **Página da Agenda (`/agenda`)** - Concluída
- 🔲 Páginas de Congregações, EBD, etc.

### Sistema de Usuários
- ✅ **Base de Autenticação e Cadastro:**
  - [x] Backend: Configurar Autenticação por Token (JWT) e enriquecer o token.
  - [x] Backend: Criar API de Cadastro (`/api/auth/register/`).
  - [x] Frontend: Configurar `AuthContext` для gerenciamento global de login.
  - [x] Frontend: Implementar páginas de Cadastro, Login e Sucesso.
- ✅ **Rotas Protegidas e Dashboards:**
  - [x] Frontend: Implementar `RotaProtegida` para restringir acesso.
  - [x] Backend: Criar API de estatísticas para o dashboard do Secretário.
  - [x] Frontend: Construir Dashboard inteligente com visão condicional para Secretário.
- ✅ **Perfil do Usuário:**
  - [x] Backend: Criar API para visualização de perfil (`/api/users/me/`).
  - [x] Frontend: Construir a página de visualização de Perfil (`/perfil`).
- 🔲 **Funcionalidades Futuras:**
  - [ ] Edição de Perfil pelo próprio usuário.
  - [ ] Módulo completo de Gestão de Usuários para Secretários (CRUD).
  - [ ] Sistema de Geração de Documentos.

---

## ✨ Tecnologias Principais

* **Frontend:**
    * **Framework:** React (com Vite)
    * **Estilização:** Tailwind CSS
    * **Roteamento:** React Router
    * **Componentes:** React Slick (para carrosséis), jwt-decode
* **Backend:**
    * **Framework:** Python com Django & Django REST Framework
    * **Autenticação:** Simple JWT (JSON Web Tokens)
    * **Banco de Dados:** SQLite (desenvolvimento)

---

## 🚀 Guia de Instalação e Configuração

### 1. Clone o Repositório

```bash
git clone [https://github.com/LucasAlb1609/2ibca-react-django](https://github.com/LucasAlb1609/2ibca-react-django)
cd 2ibca-react-django

# ⚙️ Configuração do Ambiente

## 🛠️ 2. Configuração do Backend (Django)

O backend requer um ambiente virtual isolado para gerenciar suas dependências.

### 1. Navegue até a pasta do backend

```bash
cd igreja_back
```

### 2. Crie e ative o ambiente virtual

```bash
# Criar o ambiente
python -m venv venv

# Ativar o ambiente (Windows - PowerShell)
.env\Scripts\activate
```

### 3. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 4. Crie as tabelas no banco de dados

```bash
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

---

## ⚛️ 3. Configuração do Frontend (React)

Abra um **novo terminal**.

### 1. Navegue até a pasta do frontend

```bash
cd 2ibca
```

### 2. Instale as dependências JavaScript

```bash
npm install
```

---

## 🏃 Como Rodar o Ambiente de Desenvolvimento

Para trabalhar no projeto, você precisará de **dois terminais** rodando simultaneamente.

### 🖥️ Terminal 1 - Backend (Django)

```bash
# Navegue até a pasta do backend
cd igreja_back

# Ative o ambiente virtual (se ainda não estiver ativo)
.env\Scripts\activate

# Inicie o servidor Django
python manage.py runserver
```

ℹ️ O backend estará disponível em:  
**http://127.0.0.1:8000/**

---

### 💻 Terminal 2 - Frontend (React)

```bash
# Navegue até a pasta do frontend
cd 2ibca

# Inicie o servidor de desenvolvimento do Vite
npm run dev
```

ℹ️ O frontend estará disponível em:  
**http://localhost:5173/**  
> É este o endereço que você deve abrir no navegador para ver o site.

---

## 🧪 Como Testar a API (Usando Insomnia ou Postman)

O backend é uma **API REST**.  
Para testar os endpoints (principalmente os protegidos), você pode usar o **Insomnia** ou o **Postman**.

---

### 🔑 1. Obter o Token de Autenticação (Login)

Para acessar rotas protegidas, primeiro você precisa de um *token de acesso*.

**Método:** `POST`  
**URL:** `http://127.0.0.1:8000/api/token/`

**Body (JSON):**
```json
{
    "username": "seu_usuario_aqui",
    "password": "sua_senha_aqui"
}
```

**Resposta esperada:**
Você receberá um **access token**.  
Copie esse valor.

---

### 🔒 2. Fazer uma Requisição Autenticada

Agora, para acessar uma rota protegida, envie o token que você recebeu.

**Método:** `GET` (ou `POST`, `PUT`, etc.)  
**URL (Exemplo):** `http://127.0.0.1:8000/api/users/me/`

#### Autenticação
- Vá para a aba **Auth**.  
- Selecione o tipo **Bearer Token**.  
- Cole o token no campo **TOKEN**.

Se tudo estiver certo, você receberá uma resposta:

```
200 OK
```

com os dados solicitados.

Se aparecer:

```
401 Unauthorized
```

significa que o token expirou — basta gerar um novo fazendo login novamente.

---

Pronto! Agora o backend, o frontend e os testes de API estão configurados e prontos pra rodar.
