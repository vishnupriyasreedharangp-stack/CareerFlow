# CareerFlow

A modern, role-based job marketplace built with Django that connects candidates with employers through a complete job application and hiring workflow.

CareerFlow was substantially redesigned and extended from an older Django job-portal codebase into a portfolio-ready application with improved UI, authentication, authorization, application tracking, employer workflows, and production-aware configuration.

---

## 🚀 Project Highlights

CareerFlow supports two primary user roles:

### 👤 Candidates

- Register and sign in using email-based authentication
- Browse and search open jobs
- Filter jobs by location, work mode, job type, and skills
- View detailed job information
- Apply to jobs
- Prevent duplicate applications
- Track application history
- Monitor application status:
  - Submitted
  - Under Review
  - Shortlisted
  - Rejected
  - Hired

### 🏢 Employers

- Register as an employer
- Create and manage job openings
- Define salary, experience, skills, work mode, and application deadline
- View employer dashboard metrics
- View applicants for individual jobs
- Open detailed candidate review pages
- Move candidates through the hiring pipeline
- Mark jobs as open or filled

---

## 🔄 Complete Hiring Workflow

```text
Candidate Registration
        ↓
Browse / Search Jobs
        ↓
View Job Details
        ↓
Submit Application
        ↓
Employer Reviews Application
        ↓
Under Review
        ↓
Shortlisted
        ↓
Hired
        ↓
Candidate Sees Updated Status
