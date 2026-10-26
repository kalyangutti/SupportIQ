# SupportIQ — AI Customer Support Platform

SupportIQ is an AI-powered customer support platform designed to classify customer tickets, retrieve relevant knowledge, generate grounded responses, and automate support workflows with safety checks and human oversight.

## 🎯 Objectives

- Classify incoming customer tickets.
- Retrieve relevant information from a knowledge base.
- Generate responses with supporting citations.
- Escalate uncertain or sensitive requests to human agents.
- Build secure, reliable, and testable AI workflows.

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Vector Search:** pgvector
- **AI:** Large Language Models (LLMs)
- **Testing:** pytest
- **Code Quality:** Ruff
- **Infrastructure:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Workflow & Caching:** Python state machines and Redis

## 🏗️ Development Roadmap

- [x] **L0 — Foundations:** Project setup, configuration, Docker, PostgreSQL connectivity, and verified tests
- [ ] **L1 — Ticket Management:** Ticket CRUD, authentication, and authorization
- [ ] **L2 — LLM Integration:** Model integration and structured outputs
- [ ] **L3 — Knowledge Base:** Document ingestion and retrieval
- [ ] **L4 — Grounded Responses:** Citations, validation, and abstention
- [ ] **L5 — Workflow Orchestration:** State management, retries, and reliability
- [ ] **L6 — Tool Execution:** Controlled tool use and human approvals
- [ ] **L7 — Safety & Security:** Input validation, access control, and security hardening
- [ ] **L8 — Observability & Evaluation:** Logging, cost tracking, and quality evaluation
- [ ] **L9 — Review Interface:** Human review and feedback
- [ ] **L10 — Deployment:** Production deployment and final evaluation

## 🧱 Level 0 — Foundation Setup

The project foundation includes:

- FastAPI application and health endpoint.
- Configuration management using Pydantic Settings.
- Asynchronous SQLAlchemy database sessions.
- PostgreSQL 17 running in Docker.
- pgvector-enabled PostgreSQL image.
- Docker Compose configuration.
- Persistent database volume.
- PostgreSQL health check.
- Python-to-PostgreSQL integration test.

### Run PostgreSQL

Start the database container:

```bash
docker compose up -d postgres
```

Check its status:

```bash
docker compose ps
```

The PostgreSQL container should report a healthy status.

### Run Tests

Run the complete test suite:

```bash
python -m pytest -v
```

## 🔒 Security Principles

- Keep credentials and sensitive information out of Git.
- Store local secrets in `.env` and commit only `.env.example`.
- Enforce authentication and authorization for protected operations.
- Validate AI-generated outputs before using them.
- Require appropriate approval for sensitive actions.
- Test failure scenarios and prevent unsafe automation.

## 🚀 Project Status

**Current stage:** Level 0 — Foundation setup verified.

Docker Desktop is operational, PostgreSQL is running in a container, and the database connection integration test has passed.

Remaining foundation checks, such as linting, CI configuration, and documentation validation, should be completed before considering every Level 0 task finished.

## 📌 Future Goal

Build and deploy a production-oriented AI customer support system that demonstrates backend engineering, AI integration, reliable workflows, security, testing, and deployment.

---

*Built as a hands-on portfolio project for AI Engineering and Forward Deployed Engineering.*
