from django.contrib import auth, messages
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.shortcuts import redirect, render
from django.views.generic import CreateView, FormView

from accounts.forms import EmployeeRegistrationForm, EmployerRegistrationForm, UserLoginForm
from accounts.models import User


class RegisterEmployeeView(CreateView):
    model = User
    form_class = EmployeeRegistrationForm
    template_name = 'accounts/employee/register.html'
    success_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)


class RegisterEmployerView(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name = 'accounts/employer/register.html'
    success_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)


class LoginView(FormView):
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.GET.get('next') or self.success_url

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(DjangoLogoutView):
    next_page = '/'

    def dispatch(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You have been signed out successfully.')
        return redirect(self.next_page)
