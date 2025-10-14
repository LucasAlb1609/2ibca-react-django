# 🌐 Site da Segunda Igreja Batista em Casa Amarela (React + Django)

Este repositório contém o código-fonte da nova versão do site da **2ª Igreja Batista em Casa Amarela (2IBCA)**, desenvolvido com uma arquitetura moderna que combina **React (Vite + TailwindCSS 4)** no frontend e **Django REST Framework** no backend.

---

## 🧭 Atualização Recente — Migração para TailwindCSS v4

O projeto foi totalmente atualizado da **versão 3 para a 4 do TailwindCSS**, adotando a nova estrutura de diretivas e o suporte nativo a temas e variáveis CSS.

### 🔄 Principais mudanças na migração
- Substituição de:
  ```css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  ```
  por:
  ```css
  @import "tailwindcss";
  ```
- Ajuste do `index.css` para usar a nova sintaxe do Tailwind 4 e manter compatibilidade com o Vite.  
- Limpeza e reinstalação do ambiente:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```
- Atualização das dependências:
  ```bash
  npm install tailwindcss@latest @tailwindcss/postcss@latest
  ```
- Testes realizados com sucesso em React (Vite), confirmando o funcionamento de classes utilitárias (`font-sans`, `font-light`, `italic`, `bg-*`, `text-*`, `p-*`, etc).
- Ajuste de compatibilidade com o PostCSS e o plugin oficial `@tailwindcss/postcss@4`.

✅ **Resultado:** Projeto 100% funcional com o TailwindCSS **v4.1.14** integrado ao React + Vite.  

---

## ✅ Progresso da Migração de Páginas

- [x] **Página Inicial (`/`)**
- [x] **Página de História (`/historia`)**
- [ ] Página de Liderança (`/lideranca`)
- [ ] Página de Departamentos (`/departamentos`)
- [ ] Página de Agenda (`/agenda`)
- [ ] Páginas de Congregações, EBD, etc.

---

## ✨ Tecnologias Principais

### **Frontend**
- **Framework:** React (com Vite)
- **Estilização:** TailwindCSS v4.1.14
- **Roteamento:** React Router
- **Componentes adicionais:** React Slick (para carrosséis)
- **Fonte principal:** [Poppins (Google Fonts)](https://fonts.google.com/specimen/Poppins)

### **Backend**
- **Framework:** Django + Django REST Framework
- **Banco de dados:** SQLite (modo desenvolvimento)

---

## 📋 Pré-requisitos

Garanta que as seguintes ferramentas estejam instaladas:

- [Python ≥ 3.10](https://www.python.org/downloads/)
- [Node.js ≥ 18](https://nodejs.org/en/)
- [Git](https://git-scm.com/downloads/)

---

## ⚙️ Guia de Instalação e Configuração

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/LucasAlb1609/2ibca-react-django.git
cd 2ibca-react-django
```

### 2️⃣ Configuração do Backend (Django)
```bash
cd igreja_back
python -m venv venv
.env\Scriptsctivate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

---

### 3️⃣ Configuração do Frontend (React + Tailwind v4)
```bash
cd 2ibca
npm install
```

> ⚠️ Se o projeto estiver vindo de uma versão antiga do Tailwind, remova antes as pastas antigas:
> ```bash
> rm -rf node_modules package-lock.json
> npm install
> ```

---

## 🏃 Rodando o Ambiente de Desenvolvimento

Use **dois terminais** abertos simultaneamente.

**🖥️ Terminal 1 — Backend (Django)**
```bash
cd igreja_back
.env\Scriptsctivate
python manage.py runserver
```
> Acesse em `http://127.0.0.1:8000/`

**💻 Terminal 2 — Frontend (React + Vite + Tailwind 4)**
```bash
cd 2ibca
npm run dev
```
> O frontend estará disponível em `http://localhost:5173/`

---

## 📦 Estrutura Atualizada

```
2ibca-react-django/
│
├── igreja_back/           # Backend Django
│   ├── manage.py
│   ├── igreja/            # Configurações do projeto
│   └── api/               # Endpoints REST
│
├── 2ibca/                 # Frontend React + Tailwind 4
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── index.css      # Atualizado para Tailwind v4
│   ├── vite.config.js
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

---

## 🧩 Status Atual

✅ **Tailwind v4.1.14 instalado e configurado corretamente**  
✅ **Frontend (React + Vite) em pleno funcionamento**  
✅ **Backend (Django REST Framework) ativo**  
✅ **Integração frontend-backend estável**  
🔄 **Páginas adicionais em desenvolvimento**

---

## 🤝 Contribuição

Para contribuir, crie uma nova branch a partir de `tailwind-update`:
```bash
git checkout -b nome-da-sua-branch
```

Faça suas alterações, crie um commit e envie:
```bash
git add .
git commit -m "Descrição das alterações"
git push origin nome-da-sua-branch
```

---

## 📜 Licença

Este projeto é de uso interno da **Segunda Igreja Batista em Casa Amarela (2IBCA)** e não possui licença pública aberta no momento.
