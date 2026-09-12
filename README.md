# CareerFlow

CareerFlow is a role-based job marketplace built with Django. It connects candidates and employers through a complete job application and hiring workflow.

## Features

### Candidates
- Email-based registration and login
- Browse and search jobs
- Filter by location, work mode, job type, and skills
- View job details
- Apply to jobs
- Prevent duplicate applications
- Track application status
- View shortlisted and hired applications

### Employers
- Employer registration and login
- Create and manage job openings
- Add salary, skills, experience, work mode, and deadlines
- View hiring dashboard metrics
- View applicants for each job
- Review candidate profiles
- Update application status
- Mark jobs as open or filled

## Hiring Workflow

```text
Candidate Registration
        ↓
Browse / Search Jobs
        ↓
View Job Details
        ↓
Apply
        ↓
Employer Review
        ↓
Under Review
        ↓
Shortlisted
        ↓
Hired
        ↓
Candidate Sees Updated Status

Tech Stack
Python
Django 5.2
SQLite for local development
PostgreSQL support for production
Bootstrap
HTML / CSS
WhiteNoise
Gunicorn
Run Locally
1. Clone the project
git clone <repository-url>
cd CareerFlow
2. Create a virtual environment

Windows:

py -m venv .venv
.venv\Scripts\activate

macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
4. Apply migrations
python manage.py migrate
5. Load demo data
python manage.py seed_demo
6. Start the server
python manage.py runserver

Open http://127.0.0.1:8000/.

Security

CareerFlow includes:

Role-based access control
Employer ownership checks
Candidate application protection
Duplicate application prevention
CSRF protection
Environment-based configuration

For production, configure DEBUG=False, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, and secure environment variables. PostgreSQL is recommended for production.

Project Highlights

The project was substantially redesigned and extended with:

Candidate and employer dashboards
Application tracking
Candidate review workflow
Hiring-status pipeline
Job search and filtering
Responsive UI
Demo-data management command
Production-aware Django configuration
Automated tests
Attribution

This project was substantially adapted and redesigned from an older Django job-portal codebase. The current version includes significant changes to the UI, workflows, data model, access control, configuration, and portfolio functionality.

Author

Vishnupriya



