from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class BaseRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['email'].widget.attrs['placeholder'] = 'you@example.com'

        self.fields['password1'].widget.attrs['placeholder'] = 'Create a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'


class EmployeeRegistrationForm(BaseRegistrationForm):
    first_name = forms.CharField(
        label='First name',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your first name',
            }
        ),
    )

    last_name = forms.CharField(
        label='Last name',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your last name',
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'gender',
        ]

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError('Please select a gender.')
        return gender

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employee'

        if commit:
            user.save()

        return user


class EmployerRegistrationForm(BaseRegistrationForm):
    first_name = forms.CharField(
        label='Company name',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your company name',
                'autocomplete': 'organization',
            }
        ),
    )

    last_name = forms.CharField(
        label='Company location / address',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'City, State',
                'autocomplete': 'street-address',
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employer'

        if commit:
            user.save()

        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your password',
            }
        )
    )

    def clean(self):
        cleaned = super().clean()

        email = cleaned.get('email')
        password = cleaned.get('password')

        if email and password:
            self.user = authenticate(
                email=email,
                password=password
            )

            if self.user is None:
                raise forms.ValidationError(
                    'Invalid email or password.'
                )

            if not self.user.is_active:
                raise forms.ValidationError(
                    'This account is inactive.'
                )

        return cleaned

    def get_user(self):
        return getattr(self, 'user', None)


class EmployeeProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender']

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'gender': forms.Select(
                attrs={'class': 'form-control'},
                choices=(
                    ('', 'Select gender'),
                    ('male', 'Male'),
                    ('female', 'Female'),
                ),
            ),
        }