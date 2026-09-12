# CareerFlow: portfolio notes

## How to present the project

Describe this as an **adapted and substantially extended Django job marketplace**, not as a project written from scratch. Be ready to explain the changes below and the decisions behind them.

## Engineering changes

1. Upgraded the project from Django 2.1-era configuration to Django 5.2 LTS-compatible settings.
2. Replaced hard-coded production-sensitive settings with environment variables.
3. Added PostgreSQL-ready `DATABASE_URL` support while retaining SQLite for local development.
4. Added WhiteNoise-based static-file handling and Gunicorn configuration.
5. Added role-based authorization for candidate and employer workflows.
6. Added database-level duplicate application protection with a unique constraint.
7. Added application lifecycle states and employer-side status management.
8. Added job metadata: salary range, experience, skills and work mode.
9. Added deadline validation and automatic job availability checks.
10. Added employer ownership checks around applicant data.
11. Added candidate application history and employer hiring metrics.
12. Added automated tests for authentication, authorization and application rules.
13. Added a repeatable `seed_demo` management command instead of committing demo database credentials/data.
14. Rebuilt the main UI around a consistent responsive product-style design.

## Interview talking points

### Why a unique constraint?
Application duplication is a business rule, not only a UI rule. The form/view prevents duplicate submissions during normal use, while the database constraint protects the rule even if two requests arrive close together.

### Why keep SQLite locally?
It removes setup friction for a portfolio reviewer. The same settings switch to PostgreSQL through `DATABASE_URL` for a production deployment.

### Why separate candidate and employer dashboards?
The two roles have different authorization boundaries and workflows. A candidate should only see their own applications, while an employer should only see applications belonging to jobs they own.

### What would be next?
Resume uploads, email notifications, saved jobs, employer company profiles, REST API endpoints, background tasks for notifications, object storage for media and richer analytics.
