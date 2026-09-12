from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class AuthenticationTests(TestCase):
    def test_employee_registration(self):
        response = self.client.post(reverse('accounts:employee-register'), {
            'first_name': 'Priya', 'last_name': 'Patil', 'email': 'priya@example.com',
            'password1': 'StrongPass123!', 'password2': 'StrongPass123!', 'gender': 'female',
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(email='priya@example.com')
        self.assertEqual(user.role, 'employee')
        self.assertTrue(user.check_password('StrongPass123!'))

    def test_login_uses_email(self):
        User.objects.create_user(email='user@example.com', password='StrongPass123!', role='employee')
        response = self.client.post(reverse('accounts:login'), {'email': 'user@example.com', 'password': 'StrongPass123!'})
        self.assertRedirects(response, '/')
