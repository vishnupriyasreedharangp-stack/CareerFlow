import secrets
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from accounts.models import User
from jobsapp.models import Applicant, Job


JOBS = [
    ('Junior Django Developer', 'Pune', 'web-development', 'hybrid', '0-2 years', 'Python, Django, REST API, PostgreSQL'),
    ('Backend Engineer', 'Bengaluru', 'web-development', 'remote', '2-4 years', 'Python, Django, Celery, Redis, PostgreSQL'),
    ('Frontend Developer', 'Mumbai', 'web-development', 'hybrid', '1-3 years', 'JavaScript, React, HTML, CSS'),
    ('UI/UX Designer', 'Pune', 'design', 'onsite', '1-3 years', 'Figma, UX Research, Prototyping'),
    ('QA Automation Engineer', 'Hyderabad', 'quality-assurance', 'hybrid', '2-4 years', 'Python, Selenium, PyTest, API Testing'),
    ('Data Analyst', 'Mumbai', 'data', 'remote', '1-3 years', 'SQL, Python, Power BI, Excel'),
    ('HR Operations Associate', 'Pune', 'human-resources', 'onsite', '0-2 years', 'Recruitment, Excel, Communication'),
    ('Product Support Engineer', 'Chennai', 'support', 'hybrid', '0-2 years', 'Linux, SQL, Troubleshooting, APIs'),
    ('Mobile App Intern', 'Bengaluru', 'mobile', 'onsite', 'Internship', 'Flutter, Dart, Firebase'),
    ('Cloud & DevOps Engineer', 'Remote', 'devops', 'remote', '2-5 years', 'AWS, Docker, Linux, CI/CD'),
]


class Command(BaseCommand):
    help = 'Create a polished demo dataset for local development and portfolio demos.'

    def handle(self, *args, **options):
        employer_password = secrets.token_urlsafe(10)
        candidate_password = secrets.token_urlsafe(10)
        employer, created = User.objects.get_or_create(
            email='demo.employer@careerflow.local',
            defaults={'first_name': 'Northstar Labs', 'last_name': 'Pune', 'role': 'employer', 'is_active': True},
        )
        if created:
            employer.set_password(employer_password)
            employer.save()
        else:
            employer_password = '<existing-password>'

        candidate, candidate_created = User.objects.get_or_create(
            email='demo.candidate@careerflow.local',
            defaults={'first_name': 'Aarav', 'last_name': 'Sharma', 'role': 'employee', 'gender': 'male', 'is_active': True},
        )
        if candidate_created:
            candidate.set_password(candidate_password)
            candidate.save()
        else:
            candidate_password = '<existing-password>'

        created_jobs = []
        for index, (title, location, category, work_mode, experience, skills) in enumerate(JOBS):
            job, was_created = Job.objects.get_or_create(
                user=employer,
                title=title,
                defaults={
                    'description': f'Join {employer.first_name} as a {title}. You will collaborate with a cross-functional team, ship production-quality work, and contribute to measurable product outcomes.',
                    'location': location,
                    'type': '3' if 'Intern' in title else '1',
                    'category': category,
                    'work_mode': work_mode,
                    'experience': experience,
                    'skills': skills,
                    'salary_min': 300000 + index * 50000,
                    'salary_max': 600000 + index * 75000,
                    'last_date': timezone.now() + timedelta(days=20 + index),
                    'company_name': employer.first_name,
                    'company_description': 'A product-focused technology team building practical software for modern businesses.',
                    'website': 'https://example.com',
                },
            )
            if was_created:
                created_jobs.append(job)

        for job in created_jobs[:2]:
            Applicant.objects.get_or_create(user=candidate, job=job, defaults={'status': 'shortlisted' if job == created_jobs[0] else 'reviewing'})

        self.stdout.write(self.style.SUCCESS(f'Created {len(created_jobs)} demo jobs.'))
        self.stdout.write(self.style.SUCCESS('Demo employer: demo.employer@careerflow.local'))
        self.stdout.write(self.style.SUCCESS('Demo candidate: demo.candidate@careerflow.local'))
        if employer_password != '<existing-password>':
            self.stdout.write(self.style.WARNING(f'Employer password: {employer_password}'))
        else:
            self.stdout.write(self.style.WARNING('Employer account already existed, so its password was not changed.'))
        if candidate_password != '<existing-password>':
            self.stdout.write(self.style.WARNING(f'Candidate password: {candidate_password}'))
        else:
            self.stdout.write(self.style.WARNING('Candidate account already existed, so its password was not changed.'))
