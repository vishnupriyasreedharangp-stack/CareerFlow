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
### Windows

py -m venv .venv
.venv\Scripts\activate

### macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate
