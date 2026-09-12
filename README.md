# CareerFlow

CareerFlow is a role-based job marketplace built with Django. It connects candidates and employers through a complete job application and hiring workflow.

## Features

### Candidates

- Email-based registration and login
- Browse and search jobs
- Filter by location, work mode, job type, and skills
- View detailed job information
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
```
## Tech Stack

- Python
- Django 5.2
- SQLite for local development
- PostgreSQL support for production
- Bootstrap
- HTML / CSS
- WhiteNoise
- Gunicorn
- Git / GitHub

## Run Locally

### 1. Clone the repository

```bash
git clone <repository-url>
cd CareerFlow
```
### 2. Windows

py -m venv .venv
.venv\Scripts\activate

### 3. macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Load demo data

```bash
python manage.py seed_demo
```

### 6. Start the server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Security

CareerFlow includes:

- Role-based access control
- Employer ownership checks
- Candidate application protection
- Duplicate application prevention
- CSRF protection
- Environment-based configuration

For production:

- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS`
- Configure `CSRF_TRUSTED_ORIGINS`
- Store secrets in environment variables
- Use PostgreSQL
- Never commit `.env`, database credentials, secret keys, or real passwords

## Project Highlights

- Candidate and employer dashboards
- Application tracking
- Candidate review workflow
- Hiring-status pipeline
- Job search and filtering
- Responsive UI
- Demo-data management command
- Production-aware Django configuration
- Automated tests
- Employer-specific applicant access control

## Project Structure

```text
CareerFlow/
│
├── accounts/
├── jobs/
├── jobsapp/
│   ├── management/
│   │   └── commands/
│   │       └── seed_demo.py
│   ├── migrations/
│   ├── templatetags/
│   └── views/
│
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── Procfile
├── .env.example
├── PROJECT_NOTES.md
├── LICENSE
└── README.md
```

## Project Status

CareerFlow has been tested locally through the main candidate and employer workflows.

```text
Candidate Registration
        ↓
Job Search
        ↓
Application Submission
        ↓
Employer Review
        ↓
Shortlisting
        ↓
Hiring
        ↓
Candidate Sees Updated Status
```

## Attribution

This project was substantially adapted and redesigned from an older Django job-portal codebase.

The current version includes significant changes to the UI, workflows, data model, access control, configuration, candidate and employer dashboards, application-status management, demo-data support, and portfolio functionality.

The original project's licensing and attribution requirements are retained in the `LICENSE` file.

## Author

**Vishnupriya**
