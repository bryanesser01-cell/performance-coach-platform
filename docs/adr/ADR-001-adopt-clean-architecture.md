# ADR-001: Adopt Clean Architecture

**Status:** Accepted

**Date:** 25 July 2026

**Decision Makers:**
- Bryan Esser

---

# Context

The Performance Coach Platform is expected to become a large, long-lived software system supporting multiple business domains, including:

- Athlete Management
- Training Planning
- Training Sessions
- Recovery
- Performance Analysis
- Goals
- AI Coaching
- Reporting
- Integrations
- Notifications

The platform will integrate with multiple external systems including wearable providers, AI services, databases, authentication providers, and web frameworks.

Without strong architectural boundaries, business logic becomes tightly coupled to implementation details such as databases, APIs, frameworks, and third-party services. This results in:

- Poor maintainability
- Difficult testing
- High coupling
- Low cohesion
- Expensive technology migrations
- Slower feature development

The platform requires an architecture that protects the business domain from technological change.

---

# Decision

The Performance Coach Platform will adopt **Clean Architecture** as its primary architectural style.

The architecture will ensure that:

- Business rules remain independent of infrastructure.
- Dependencies always point toward the business domain.
- External systems communicate through interfaces.
- Infrastructure can be replaced without affecting business logic.
- Business rules remain testable without databases or web frameworks.

The project will also incorporate concepts from:

- Domain-Driven Design (DDD)
- SOLID Principles
- Dependency Injection
- Repository Pattern
- CQRS where appropriate
- Event-Driven Architecture where beneficial

---

# Architectural Layers

The platform will be organized into the following logical layers.

```
Presentation
        │
        ▼
Application
        │
        ▼
Domain
        │
        ▼
Infrastructure
```

---

## Presentation Layer

Responsible for communication with users and external clients.

Examples:

- REST APIs
- Future GraphQL APIs
- CLI tools
- Admin dashboards
- Mobile applications

Responsibilities:

- Receive requests
- Validate inputs
- Return responses
- Never contain business rules

---

## Application Layer

Coordinates business use cases.

Responsibilities include:

- Executing use cases
- Transaction boundaries
- Authorization
- Orchestration
- Calling domain services

The Application Layer contains workflow but very little business logic.

---

## Domain Layer

The Domain Layer is the heart of the platform.

It contains:

- Entities
- Value Objects
- Aggregates
- Domain Services
- Domain Events
- Repository Interfaces
- Business Rules

The Domain Layer must never depend on:

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- External APIs
- AI providers

---

## Infrastructure Layer

Responsible for technical implementation.

Examples:

- PostgreSQL
- SQLAlchemy
- Redis
- Garmin Integration
- Strava Integration
- OpenAI
- Authentication
- Email
- Logging

Infrastructure exists to support the Domain Layer.

It must never contain business rules.

---

# Dependency Rule

All dependencies point inward.

```
Presentation
      ↓
Application
      ↓
Domain
      ↑
Infrastructure
```

The Domain Layer has no knowledge of the outer layers.

---

# Benefits

Adopting Clean Architecture provides:

## Maintainability

Business logic remains isolated and easier to understand.

## Testability

Business rules can be tested without infrastructure.

## Flexibility

Databases, frameworks, and providers can be replaced with minimal impact.

## Scalability

New domains can be added without restructuring the application.

## Longevity

Business rules outlive technology choices.

---

# Alternatives Considered

## Layered Architecture

Pros:

- Simple
- Familiar

Cons:

- Often becomes tightly coupled.
- Business logic leaks into controllers and repositories.

Decision:

Rejected.

---

## MVC Architecture

Pros:

- Good for small applications.

Cons:

- Poor separation of business rules in large systems.

Decision:

Rejected.

---

## Microservices

Pros:

- Independent deployment
- Scalability

Cons:

- Significant operational complexity.
- Premature for the current size of the platform.

Decision:

Deferred.

The platform will begin as a modular monolith.

---

# Consequences

Positive:

- Better testing
- Better maintainability
- Easier onboarding
- Clear architectural boundaries
- Easier future migrations
- Better AI integration

Negative:

- More initial structure
- More interfaces
- Slightly slower initial development
- Additional architectural discipline required

The long-term benefits outweigh the initial complexity.

---

# Guiding Principles

When making architectural decisions, developers should ask:

- Does this keep business rules independent?
- Does this increase coupling?
- Does this improve maintainability?
- Can this be tested without infrastructure?
- Will this still make sense in five years?

If the answer is "No" to any of these questions, the design should be reconsidered.

---

# Implementation Notes

The repository will follow a domain-oriented structure rather than a technical-layer structure.

Example:

```
app/
    athlete/
    training/
    recovery/
    goals/
    performance/
    integrations/
    ai/
    shared/
```

Each domain owns:

- Models
- Services
- Repository Interfaces
- Business Rules
- Tests

This aligns with both Clean Architecture and Domain-Driven Design.

---

# References

- Robert C. Martin — *Clean Architecture*
- Eric Evans — *Domain-Driven Design*
- Vaughn Vernon — *Implementing Domain-Driven Design*
- Martin Fowler — *Patterns of Enterprise Application Architecture*
