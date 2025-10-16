# Progresso da Implementação - Sistema de Usuários

Este documento acompanha a migração e implementação do sistema de gestão de usuários, cadastro e autenticação para a nova arquitetura React + Django API.

**Legenda:**
- ✅ **Concluído:** Funcionalidade implementada e testada.
- 🔄 **Em Progresso:** Em desenvolvimento ativo.
- 🔲 **Pendente:** Próximas etapas a serem iniciadas.

---

### Fase 1: Autenticação, Cadastro e Login (Base)

- ✅ **Backend: Configurar Autenticação por Token (JWT)**
  - ✅ Instalar e configurar `djangorestframework-simplejwt`.
  - ✅ Personalizar o token para incluir `nome_completo` e `papel`.
  - ✅ Criar endpoints de login (`/api/token/`) e refresh.

- ✅ **Backend: Criar API de Cadastro**
  - ✅ Criar `UserRegistrationSerializer` com validação de senha.
  - ✅ Criar endpoint público `/api/auth/register/`.

- ✅ **Frontend: Configurar Contexto de Autenticação**
  - ✅ Criar `AuthContext` para gerenciar o estado global de login (usuário e tokens).
  - ✅ Implementar `AuthProvider` e envolver a aplicação.
  - ✅ Criar hook `useAuth` para acesso fácil ao contexto.

- ✅ **Frontend: Implementar Páginas Públicas**
  - ✅ Criar a página de Cadastro (`/cadastro`) com formulário completo.
  - ✅ Criar a página de Login (`/login`) que interage com o `AuthContext`.
  - ✅ Criar a página de Sucesso Pós-Cadastro (`/cadastro-sucesso`).

- ✅ **Frontend: Implementar Rotas Protegidas**
  - ✅ Criar o componente "guardião" `RotaProtegida`.
  - ✅ Proteger a rota `/dashboard`, redirecionando usuários não logados.

---

### Fase 2: Dashboards e Perfis de Usuário

- ✅ **Backend: Criar API para Dashboard do Secretário**
  - ✅ Criar endpoint protegido `/api/admin/dashboard-stats/` que retorna estatísticas.

- ✅ **Frontend: Construir Dashboard Inteligente**
  - ✅ A página `/dashboard` renderiza conteúdo diferente com base no papel do usuário (Secretário vs. outros).
  - ✅ Dashboard do Secretário busca e exibe as estatísticas da API.

- 🔲 **Backend: Criar API para Perfil do Usuário**
  - 🔲 Criar endpoint `/api/users/me/` para retornar os dados do usuário logado.
  - 🔲 Criar endpoint para o usuário editar seu próprio perfil.

- 🔲 **Frontend: Construir Páginas de Perfil**
  - 🔲 Criar a página `/perfil` para o usuário visualizar seus dados.
  - 🔲 Criar a página `/perfil/editar` com o formulário de edição.

---

### Fase 3: Gestão de Secretário (Admin no Frontend)

- 🔲 **Backend: Criar APIs de Gestão**
  - 🔲 Endpoint para listar todos os usuários (`/api/admin/users/`).
  - 🔲 Endpoint para listar apenas usuários pendentes (`/api/admin/pending-users/`).
  - 🔲 Endpoints de ação para aprovar, rejeitar e alterar o papel de um usuário.
  - 🔲 Endpoints para criar, editar e excluir usuários (CRUD completo).

- 🔲 **Frontend: Construir Módulo de Administração**
  - 🔲 Criar a página `/admin/todos-usuarios` com uma tabela de todos os usuários.
  - 🔲 Criar a página `/admin/usuarios-pendentes` com as ações de aprovação/rejeição.
  - 🔲 Criar o formulário para um secretário criar/editar um usuário.

---

### Fase 4: Funcionalidades Adicionais (Futuro)

- 🔲 **Geração de Documentos**
  - 🔲 Backend: Criar API para gerar os PDFs.
  - 🔲 Frontend: Implementar a interface para o secretário solicitar documentos para um membro.

- 🔲 **Recuperação de Senha**
  - 🔲 Backend: Configurar endpoints de "esqueci minha senha" e reset.
  - 🔲 Frontend: Criar as páginas e formulários para o fluxo de recuperação.