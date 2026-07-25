# Performance Coach Platform

# Domain Model

Version: 1.0

Status: Draft

Author: Bryan Esser

Last Updated: 25 July 2026

---

# Purpose

This document defines the business domains that make up the Performance Coach Platform.

Each domain owns its own business rules, models, services, events, and repository interfaces.

The purpose of the Domain Model is to ensure the platform grows around business capabilities rather than technical components.

---

# Core Principles

Every domain should:

- Own a single business capability.
- Minimize dependencies on other domains.
- Expose clear interfaces.
- Hide implementation details.
- Be independently testable.

---

# Domain Overview

The platform is divided into the following domains.

```
Athlete
│
├── Goals
├── Training
├── Recovery
├── Performance
├── AI Coach
├── Notifications
├── Integrations
├── Reporting
└── Administration
```

---

# Domain Descriptions

## Athlete

Responsible for managing athlete information.

Responsibilities

- Athlete profile
- Demographics
- Physical characteristics
- Preferred units
- Training zones
- Equipment
- Connected providers

Owns

- Athlete
- AthleteProfile
- AthleteSettings

---

## Goals

Responsible for athlete objectives.

Examples

- Weight loss
- Marathon
- 5K
- 10K
- Half Marathon
- Ironman
- VO2 Max
- Weekly Distance

Owns

- Goal
- GoalProgress
- Milestones

---

## Training

Responsible for planning and recording training.

Owns

- Training Plans
- Training Sessions
- Activities
- Workouts
- Training Load

Business Rules

- Planned sessions
- Completed sessions
- Missed sessions
- Weekly load
- Compliance

---

## Recovery

Responsible for recovery readiness.

Owns

- Sleep
- HRV
- Resting Heart Rate
- Fatigue
- Recovery Score
- Wellness Surveys

Business Rules

- Recovery recommendations
- Readiness calculations
- Fatigue analysis

---

## Performance

Responsible for performance analytics.

Owns

- Race Results
- PBs
- Critical Speed
- Running Economy
- Thresholds
- VO2 Max
- Trends

Business Rules

- Performance calculations
- Progress tracking
- Benchmark comparisons

---

## AI Coach

Responsible for AI reasoning.

Owns

- Recommendations
- Insights
- Explanations
- Training Suggestions
- Goal Analysis
- Recovery Advice

Business Rules

- Never modify data directly.
- Explain recommendations.
- Support evidence-based coaching.

---

## Integrations

Responsible for external providers.

Examples

- Garmin
- COROS
- Polar
- Suunto
- Apple Health
- Google Health Connect
- Strava

Business Rules

Convert provider data into normalized platform models.

---

## Notifications

Responsible for communication.

Examples

- Workout reminders
- Goal milestones
- Recovery alerts
- Weekly reports
- AI recommendations

---

## Reporting

Responsible for dashboards.

Examples

- Weekly summaries
- Monthly summaries
- Training trends
- Goal progress
- Coach reports

---

## Administration

Responsible for platform administration.

Examples

- User management
- Roles
- Permissions
- Audit logs
- Feature flags
- System configuration

---

# Domain Relationships

```
Athlete
│
├── Goals
├── Training
│      │
│      └── Recovery
│
├── Performance
│
├── AI Coach
│
├── Notifications
│
├── Reporting
│
└── Integrations
```

---

# Domain Ownership

| Domain | Owns Data | Depends On |
|---------|-----------|------------|
| Athlete | Athlete | None |
| Goals | Goals | Athlete |
| Training | Sessions | Athlete |
| Recovery | Recovery Metrics | Athlete, Training |
| Performance | Performance Metrics | Athlete, Training |
| AI Coach | Insights | All Domains |
| Reporting | Reports | All Domains |
| Notifications | Notifications | All Domains |
| Integrations | Provider Data | None |
| Administration | Users & Roles | None |

---

# Guiding Rule

Every new feature added to the platform must belong to exactly one domain.

If a feature appears to belong to multiple domains, the design should be reconsidered before implementation.
