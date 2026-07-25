# Folder Structure

**Status:** Approved
**Version:** 1.0
**Last Updated:** 25 July 2026

---

# Purpose

This document defines the standard folder structure for the Performance Coach Platform.

The structure follows the principles of:

- Clean Architecture
- Domain-Driven Design (DDD)
- SOLID
- Separation of Concerns

The objective is to keep business rules independent of frameworks, databases, and third-party services while enabling the platform to scale over time.

---

# Architecture Overview

```
Performance Coach Platform
│
├── backend
├── frontend
├── docs
├── infrastructure
└── scripts
```

---

# Backend Structure

```
backend/
│
├── app/
│   └── main.py
│
├── domain/
│
├── application/
│
├── infrastructure/
│
├── interfaces/
│
├── shared/
│
├── tests/
│
└── pyproject.toml
```

---

# Domain Layer

Contains all business logic.

No FastAPI.

No SQLAlchemy.

No PostgreSQL.

No HTTP.

No external APIs.

```
domain/
│
├── athlete/
├── goals/
├── training/
├── recovery/
├── performance/
├── workout/
├── analytics/
└── coaching/
```

Each domain owns:

- Entities
- Value Objects
- Domain Services
- Repository Interfaces
- Business Rules
- Domain Events

---

# Application Layer

Coordinates business operations.

Responsible for:

- Use Cases
- Commands
- Queries
- DTOs
- Validation
- Transactions

```
application/
│
├── commands/
├── queries/
├── dto/
└── services/
```

The application layer orchestrates domain objects but does not contain business rules.

---

# Infrastructure Layer

Contains technical implementations.

Examples:

- PostgreSQL
- SQLAlchemy
- JWT
- Email
- Garmin
- Apple Health
- Strava

```
infrastructure/
│
├── database/
├── repositories/
├── security/
├── integrations/
└── messaging/
```

Infrastructure depends on the Domain layer—not the other way around.

---

# Interface Layer

Responsible for communication with the outside world.

```
interfaces/
│
├── api/
├── schemas/
└── middleware/
```

Responsibilities include:

- FastAPI routers
- Request validation
- Response serialization
- Authentication middleware

No business logic belongs here.

---

# Shared Layer

Shared utilities used across the platform.

```
shared/
│
├── exceptions/
├── logging/
├── configuration/
├── utilities/
└── constants/
```

Shared code should remain small and generic.

---

# Tests

Testing mirrors the production structure.

```
tests/
│
├── unit/
├── integration/
├── api/
└── performance/
```

Each feature should include corresponding tests.

---

# Dependency Rule

Dependencies always point inward.

```
Interfaces
      ↓
Application
      ↓
Domain
      ↑
Infrastructure
```

The Domain layer has no dependencies on any outer layer.

---

# Folder Responsibilities

| Folder | Responsibility |
|---------|----------------|
| domain | Business rules |
| application | Use cases |
| infrastructure | Technical implementations |
| interfaces | API and external communication |
| shared | Common utilities |
| tests | Automated testing |

---

# Future Expansion

The structure is designed to support future capabilities including:

- AI Coaching
- Garmin Integration
- Apple Health
- Wearables
- Nutrition
- Injury Prevention
- Performance Prediction
- Multi-sport Support
- Team Management
- Coach Portal

No restructuring should be required to support these features.

---

# Guiding Principle

Business rules must remain independent of technology.

Frameworks, databases, APIs, and user interfaces are implementation details that can change without requiring modifications to the Domain layer.
