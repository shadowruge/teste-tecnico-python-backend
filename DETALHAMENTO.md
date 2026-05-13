# 🚀 FastAPI Productivity API

API RESTful construída com FastAPI, seguindo boas práticas de arquitetura backend moderna (DDD Light, separação de camadas e clean architecture).

---

## 📌 Sobre o Projeto

Esta API foi desenvolvida como evolução de um CRUD simples para uma arquitetura profissional, incluindo:

* Estrutura em camadas
* Separação de responsabilidades
* Tratamento de erros
* Paginação e filtros
* Organização inspirada em DDD (Domain Driven Design - Light)

---

## 🧠 Arquitetura

```text
Interface (FastAPI)
↓
Application (Use Cases)
↓
Domain (Regras de Negócio)
↓
Infrastructure (Banco de Dados)
```

---

## 📁 Estrutura do Projeto

```bash
app/
├── main.py
├── core/              # Exceptions, configs
├── db/                # Conexão com banco
├── models/            # Modelos SQLAlchemy
├── schemas/           # Pydantic schemas
├── repositories/      # Acesso a dados
├── services/          # Regras de negócio
├── routes/            # Endpoints FastAPI
```

---

## ⚙️ Tecnologias

* Python 3.11+
* FastAPI
* SQLAlchemy
* Pydantic

---

## 🚀 Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar a aplicação

```bash
uvicorn app.main:app --reload
```

---

## 📚 Documentação automática

Após subir o servidor:

* Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

FastAPI gera documentação automaticamente baseada nos schemas

---

## 🔥 Funcionalidades

### ✅ CRUD completo de Tasks

* Criar tarefa
* Listar tarefas
* Buscar por ID
* Atualizar tarefa
* Deletar tarefa

---

### 🔎 Paginação

```http
GET /tasks?skip=0&limit=10
```

---

### 🔍 Filtro

```http
GET /tasks?completed=true
```

---

### ⚠️ Tratamento de Erros

* 404 → recurso não encontrado
* 400 → requisição inválida
* 422 → validação automática (FastAPI)

---

## 🧪 Testes

```bash
pytest
```

---

## 🧠 Boas Práticas Aplicadas

* Separação de camadas (Router, Service, Repository)
* Uso de Pydantic para validação
* Dependency Injection (FastAPI Depends)
* Código desacoplado
* Organização escalável

---

## 💡 Exemplo de Endpoint

```http
POST /tasks
```

```json
{
  "title": "Estudar FastAPI",
  "description": "Aprender arquitetura backend"
}
```

---

## 📌 Melhorias Futuras

* [ ] Autenticação JWT
* [ ] Docker
* [ ] Alembic (migrations)
* [ ] Logging estruturado
* [ ] CI/CD

---

## 👨‍💻 Autor

Desenvolvido por [Seu Nome]

---

## 📄 Licença

MIT License
