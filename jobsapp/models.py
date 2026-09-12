from django.conf import settings
from django.db import models
from django.utils import timezone

JOB_TYPE = (
    ('1', 'Full time'),
    ('2', 'Part time'),
    ('3', 'Internship'),
)

WORK_MODE = (
    ('onsite', 'On-site'),
    ('hybrid', 'Hybrid'),
    ('remote', 'Remote'),
)

APPLICATION_STATUS = (
    ('submitted', 'Submitted'),
    ('reviewing', 'Under review'),
    ('shortlisted', 'Shortlisted'),
    ('rejected', 'Rejected'),
    ('hired', 'Hired'),
)


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    work_mode = models.CharField(choices=WORK_MODE, max_length=20, default='onsite')
    experience = models.CharField(max_length=100, default='0-2 years')
    skills = models.CharField(max_length=500, blank=True, default='')
    salary_min = models.PositiveIntegerField(blank=True, null=True)
    salary_max = models.PositiveIntegerField(blank=True, null=True)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=500)
    website = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    filled = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['location']),
            models.Index(fields=['work_mode']),
            models.Index(fields=['last_date']),
        ]

    def __str__(self):
        return self.title

    @property
    def is_open(self):
        return not self.filled and self.last_date >= timezone.now()

    @property
    def salary_display(self):
        if self.salary_min is not None and self.salary_max is not None:
            return f'₹{self.salary_min:,} - ₹{self.salary_max:,} / year'
        if self.salary_min is not None:
            return f'From ₹{self.salary_min:,} / year'
        return 'Salary not disclosed'

    @property
    def skills_list(self):
        return [skill.strip() for skill in self.skills.split(',') if skill.strip()]


class Applicant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='submitted')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['user', 'job'], name='unique_user_job_application'),
        ]

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.job.title}'
