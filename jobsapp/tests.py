from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from jobsapp.models import Applicant, Job


class JobPortalTests(TestCase):
    def setUp(self):
        self.employer = User.objects.create_user(
            email='employer@example.com', password='StrongPass123!', role='employer', first_name='Acme'
        )
        self.employee = User.objects.create_user(
            email='candidate@example.com', password='StrongPass123!', role='employee', first_name='Aarav'
        )
        self.job = Job.objects.create(
            user=self.employer,
            title='Django Developer',
            description='Build web applications.',
            location='Pune',
            type='1',
            category='web-development',
            work_mode='hybrid',
            experience='0-2 years',
            skills='Python, Django, REST API',
            salary_min=400000,
            salary_max=700000,
            last_date=timezone.now() + timedelta(days=10),
            company_name='Acme Labs',
            company_description='Product team',
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse('jobs:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django Developer')

    def test_employee_can_apply_only_once(self):
        self.client.login(email='candidate@example.com', password='StrongPass123!')
        url = reverse('jobs:apply-job', args=[self.job.id])
        self.client.post(url)
        self.client.post(url)
        self.assertEqual(Applicant.objects.filter(user=self.employee, job=self.job).count(), 1)

    def test_employer_cannot_apply(self):
        self.client.login(email='employer@example.com', password='StrongPass123!')
        response = self.client.post(reverse('jobs:apply-job', args=[self.job.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Applicant.objects.filter(user=self.employer, job=self.job).exists())

    def test_employer_sees_only_own_applicants(self):
        other = User.objects.create_user(email='other@example.com', password='StrongPass123!', role='employer')
        other_job = Job.objects.create(
            user=other, title='Other Role', description='Role', location='Mumbai', type='1', category='data',
            work_mode='remote', experience='1-3 years', last_date=timezone.now() + timedelta(days=5),
            company_name='Other Co', company_description='Other team'
        )
        Applicant.objects.create(user=self.employee, job=other_job)
        self.client.login(email='employer@example.com', password='StrongPass123!')
        response = self.client.get(reverse('jobs:employer-dashboard-applicants', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Other Role')
