from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

ROLE_CHOICES = (
    ('employee', 'Candidate'),
    ('employer', 'Employer'),
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='employee')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, default='')
    email = models.EmailField(unique=True, error_messages={'unique': 'A user with that email already exists.'})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
