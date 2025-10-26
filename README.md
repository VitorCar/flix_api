# 🎬 Flix API

API de filmes desenvolvida com **Django Rest Framework (DRF)  
O objetivo do projeto é colocar em prática o desenvolvimento de **APIs RESTful completas**, incluindo CRUD, autenticação JWT, permissões de usuário, versionamento e deploy.

---

## 🚀 Tecnologias Utilizadas

- **Python 3+**
- **Django**
- **Django Rest Framework (DRF)**
- **Postman**
- **JWT (JSON Web Token)**
- **Flake8 (PEP8 Linter)**
- **PythonAnywhere** (Deploy)
- **GitHub** (Controle de versão)

---

## 🎯 Objetivo do Projeto

A **Flix API** foi desenvolvida para consolidar o aprendizado sobre o **Django Rest Framework** e demonstrar a criação de uma API modular, escalável e segura.  
O projeto segue o modelo RESTful e foi construído com múltiplos aplicativos, cada um responsável por uma entidade específica do domínio de filmes.

---

## 🧩 Estrutura da API

A aplicação possui CRUD completo das seguintes entidades:

| Entidade  | Descrição |
|------------|------------|
| **Genres** | Gêneros de filmes |
| **Actors** | Atores e atrizes |
| **Directors** | Diretores de filmes |
| **Movies** | Filmes cadastrados |
| **Reviews** | Avaliações e notas dos usuários |
| **Stats** | Estatísticas de avaliações e médias |

---

## ⚙️ Funcionalidades Principais

- **CRUD completo** (Create, Read, Update, Delete)  
- **Endpoints RESTful** organizados e versionados  
- **Autenticação JWT (JSON Web Token)**  
- **Permissões e grupos de usuários personalizados**  
- **Serializers dinâmicos e campos calculados**  
- **Validações customizadas com DRF**  
- **Boas práticas PEP8 e Flake8**  
- **Deploy no PythonAnywhere**  

---

## 🧠 Principais Conceitos Aplicados

### 🔹 Django Rest Framework
- Generic Views: `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`
- ModelSerializer e validações
- SerializerMethodField (campos calculados)
- Serializers dinâmicos

### 🔹 Autenticação e Permissões
- Autenticação via JWT (Simple JWT)
- Proteção de endpoints
- Criação de permission classes customizadas
- Grupos e permissões globais

### 🔹 Boas Práticas e Organização
- Estrutura modular por apps
- Uso de `requirements.txt` e `requirements_dev.txt`
- Aplicação da PEP8 e configuração do Flake8
- Django Commands personalizados

### 🔹 Deploy
- Preparação para produção
- Hospedagem no **PythonAnywhere**
- Publicação no GitHub

---

## 🧪 Testes de API com Postman

Todos os endpoints da API foram testados utilizando o **Postman**, validando:
- Requisições **GET**, **POST**, **PUT** e **DELETE**
- Respostas em formato **JSON**
- Autenticação e autorização via **JWT**
- Permissões específicas de usuários e grupos

> 💡 O Postman foi essencial para garantir a integridade dos endpoints e o correto funcionamento das permissões.

---

## 📁 Estrutura de Pastas (simplificada)


---

## ⚡ Instalação e Execução

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/flix-api.git
```
Acesse a pasta do projeto
cd flix-api

Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

Instale as dependências
pip install -r requirements.txt

Execute as migrações e inicie o servidor
python manage.py migrate
python manage.py runserver

Autenticação JWT

Para acessar endpoints protegidos:

Gere o token JWT em api/v1/authentication/token/ com as credenciais de usuário.
{
    "username": "teste",
    "password": "vto@20ABC"
}

Use o token no cabeçalho das requisições:
Authorization: Bearer seu_token_aqui


✨ Autor

Vitor Carvalho
📍 Desenvolvedor Backend | Python | Django | Django Rest Framework (DRF)




