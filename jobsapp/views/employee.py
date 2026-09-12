from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView

from accounts.forms import EmployeeProfileUpdateForm
from accounts.models import User
from jobsapp.models import Applicant


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class EmployeeDashboardView(ListView):
    model = Applicant
    template_name = 'jobs/employee/dashboard.html'
    context_object_name = 'applications'
    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employee':
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Applicant.objects.filter(user=self.request.user).select_related('job').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        applications = Applicant.objects.filter(user=self.request.user)
        context['total_applications'] = applications.count()
        context['shortlisted'] = applications.filter(status='shortlisted').count()
        context['hired'] = applications.filter(status='hired').count()
        return context


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class EditProfileView(UpdateView):
    model = User
    form_class = EmployeeProfileUpdateForm
    context_object_name = 'employee'
    template_name = 'jobs/employee/edit-profile.html'
    success_url = reverse_lazy('jobs:employee-dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employee':
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)
