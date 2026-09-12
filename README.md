# CareerFlow

CareerFlow is a role-based job marketplace built with Django. It was substantially redesigned and extended from an older job-portal codebase into a portfolio-ready application focused on candidate and employer workflows.

## What makes this version portfolio-worthy

- Candidate and employer authentication using a custom email-based user model
- Role-based access control for candidate and employer workflows
- Job search across title, description, company and skills
- Filters for location, work mode and job type
- Job deadlines and automatic open/closed status
- Salary range, experience level and skills metadata
- One-application-per-candidate protection at the database level
- Candidate dashboard with application history and status tracking
- Employer dashboard with hiring metrics
- Employer applicant pipeline: submitted → reviewing → shortlisted → rejected → hired
- Employer ownership checks so users cannot access another employer's applicants
- Django admin for jobs, users and applications
- Responsive UI with reusable components and a cleaner product-style visual system
- Production-aware settings using environment variables and WhiteNoise
- SQLite for local development with optional PostgreSQL through `DATABASE_URL`
- Automated tests for authentication, application rules and access control
- Demo-data management command for a repeatable portfolio walkthrough

## Tech stack

Python · Django 5.2 LTS · SQLite/PostgreSQL · Bootstrap · WhiteNoise · Gunicorn

Django 5.2 is an LTS release and supports modern Python versions including Python 3.12. See the official Django release notes for upgrade and compatibility details.

## Run locally

### 1. Create and activate a virtual environment

Windows:

```powershell
py -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` if you use an environment manager, or set the variables directly in your shell. For local development, the defaults are intentionally simple.

### 4. Create the database

```bash
python manage.py migrate
```

### 5. Load demo data

```bash
python manage.py seed_demo
```

The command prints generated passwords for newly created demo accounts. Do not use those demo credentials in production.

### 6. Start the server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Useful commands

```bash
python manage.py check
python manage.py test
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
```

## Main user flows

### Candidate

1. Create a candidate account.
2. Search or browse open jobs.
3. Open a job detail page.
4. Apply once.
5. Track the application from the candidate dashboard.
6. See status changes made by the employer.

### Employer

1. Create an employer account.
2. Post a job with deadline, skills, experience, salary and work mode.
3. View dashboard metrics.
4. Open an applicant list for a specific role.
5. Move applicants through the hiring pipeline.
6. Close or reopen a job.

## Security and production notes

Never commit a real `DJANGO_SECRET_KEY`, production database credentials or demo passwords. Set `DEBUG=False` in production and provide explicit `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` values.

For production, use PostgreSQL rather than relying on SQLite for concurrent application traffic.

## Attribution

This repository is an adapted and substantially modified portfolio project based on an older open-source Django job-portal implementation. The current version includes a new product identity, redesigned UI, updated Django configuration, new data fields, candidate/employer dashboards, application-status workflow, access-control fixes, demo seeding and automated tests.
