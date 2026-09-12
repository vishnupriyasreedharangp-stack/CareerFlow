from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from jobsapp.forms import ApplicationStatusForm
from jobsapp.models import Applicant, Job


@method_decorator(
    login_required(login_url=reverse_lazy('accounts:login')),
    name='dispatch'
)
class DashboardView(ListView):
    model = Job
    template_name = 'jobs/employer/dashboard.html'
    context_object_name = 'jobs'
    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employer':
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Job.objects
            .filter(user=self.request.user)
            .annotate(application_count=Count('applicants'))
            .order_by('-created_at')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        jobs = Job.objects.filter(user=self.request.user)

        context['total_jobs'] = jobs.count()

        context['open_jobs'] = jobs.filter(
            filled=False,
            last_date__gte=timezone.now()
        ).count()

        context['total_applications'] = Applicant.objects.filter(
            job__user=self.request.user
        ).count()

        context['shortlisted'] = Applicant.objects.filter(
            job__user=self.request.user,
            status='shortlisted'
        ).count()

        return context


@method_decorator(
    login_required(login_url=reverse_lazy('accounts:login')),
    name='dispatch'
)
class ApplicantPerJobView(ListView):
    model = Applicant
    template_name = 'jobs/employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employer':
            return redirect('jobs:home')

        self.job = get_object_or_404(
            Job,
            pk=kwargs['job_id'],
            user=request.user
        )

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Applicant.objects
            .filter(job=self.job)
            .select_related('user')
            .order_by('-created_at')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.job
        context['status_form'] = ApplicationStatusForm()
        return context


@method_decorator(
    login_required(login_url=reverse_lazy('accounts:login')),
    name='dispatch'
)
class ApplicantsListView(ListView):
    model = Applicant
    template_name = 'jobs/employer/all-applicants.html'
    context_object_name = 'applicants'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employer':
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            self.model.objects
            .filter(job__user=self.request.user)
            .select_related('user', 'job')
            .order_by('-created_at')
        )


@login_required(login_url=reverse_lazy('accounts:login'))
def applicant_detail(request, applicant_id):
    """
    Display a candidate application to the employer who owns the job.

    The job ownership check is important because an employer must never
    be able to view an applicant belonging to another employer's job.
    """
    if request.user.role != 'employer':
        return redirect('jobs:home')

    applicant = get_object_or_404(
        Applicant.objects.select_related('user', 'job'),
        id=applicant_id,
        job__user=request.user
    )

    return render(
        request,
        'jobs/employer/applicant-detail.html',
        {
            'applicant': applicant,
        }
    )


@login_required(login_url=reverse_lazy('accounts:login'))
def filled(request, job_id=None):
    if request.user.role != 'employer':
        return redirect('accounts:login')

    job = get_object_or_404(
        Job,
        user=request.user,
        id=job_id
    )

    job.filled = not job.filled

    job.save(
        update_fields=[
            'filled',
            'updated_at'
        ]
    )

    messages.success(
        request,
        f'Job marked as {"filled" if job.filled else "open"}.'
    )

    return redirect('jobs:employer-dashboard')


@login_required(login_url=reverse_lazy('accounts:login'))
def update_application_status(request, applicant_id):
    if request.user.role != 'employer':
        return redirect('accounts:login')

    applicant = get_object_or_404(
        Applicant,
        id=applicant_id,
        job__user=request.user
    )

    if request.method == 'POST':
        form = ApplicationStatusForm(
            request.POST,
            instance=applicant
        )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from jobsapp.forms import ApplicationStatusForm
from jobsapp.models import Applicant, Job


@method_decorator(
    login_required(login_url=reverse_lazy('accounts:login')),
    name='dispatch'
)
class DashboardView(ListView):
    model = Job
    template_name = 'jobs/employer/dashboard.html'
    context_object_name = 'jobs'
    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employer':
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Job.objects
            .filter(user=self.request.user)
            .annotate(application_count=Count('applicants'))
            .order_by('-created_at')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        jobs = Job.objects.filter(user=self.request.user)

        context['total_jobs'] = jobs.count()

        context['open_jobs'] = jobs.filter(
            filled=False,
            last_date__gte=timezone.now()
        ).count()

        context['total_applications'] = Applicant.objects.filter(
            job__user=self.request.user
        ).count()

        context['shortlisted'] = Applicant.objects.filter(
            job__user=self.request.user,
            status='shortlisted'
        ).count()

        return context


@method_decorator(
    login_required(login_url=reverse_lazy('accounts:login')),
    name='dispatch'
)
class ApplicantPerJobView(ListView):
    model = Applicant
    template_name = 'jobs/employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 8

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employer':
            return redirect('jobs:home')

        self.job = get_object_or_404(
            Job,
            pk=kwargs['job_id'],
            user=request.user
        )

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Applicant.objects
            .filter(job=self.job)
            .select_related('user')
            .order_by('-created_at')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job'] = self.job
        context['status_form'] = ApplicationStatusForm()
        return context


@method_decorator(
    login_required(login_url=reverse_lazy('accounts:login')),
    name='dispatch'
)
class ApplicantsListView(ListView):
    model = Applicant
    template_name = 'jobs/employer/all-applicants.html'
    context_object_name = 'applicants'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employer':
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return (
            Applicant.objects
            .filter(job__user=self.request.user)
            .select_related('user', 'job')
        )


@login_required(login_url=reverse_lazy('accounts:login'))
def applicant_detail(request, applicant_id):
    if request.user.role != 'employer':
        return redirect('jobs:home')

    applicant = get_object_or_404(
        Applicant.objects.select_related('user', 'job'),
        id=applicant_id,
        job__user=request.user
    )

    return render(
        request,
        'jobs/employer/applicant-detail.html',
        {
            'applicant': applicant,
        }
    )


@login_required(login_url=reverse_lazy('accounts:login'))
def filled(request, job_id=None):
    if request.user.role != 'employer':
        return redirect('accounts:login')

    job = get_object_or_404(
        Job,
        user=request.user,
        id=job_id
    )

    job.filled = not job.filled

    job.save(
        update_fields=[
            'filled',
            'updated_at'
        ]
    )

    messages.success(
        request,
        f'Job marked as {"filled" if job.filled else "open"}.'
    )

    return redirect('jobs:employer-dashboard')


@login_required(login_url=reverse_lazy('accounts:login'))
def update_application_status(request, applicant_id):
    if request.user.role != 'employer':
        return redirect('accounts:login')

    applicant = get_object_or_404(
        Applicant,
        id=applicant_id,
        job__user=request.user
    )

    if request.method == 'POST':
        form = ApplicationStatusForm(
            request.POST,
            instance=applicant
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Application status updated.'
            )

    return redirect(
        'jobs:employer-dashboard-applicants',
        job_id=applicant.job_id
    )
    if form.is_valid():
            form.save()

            messages.success(
                request,
                'Application status updated.'
            )

    return redirect(
        'jobs:employer-dashboard-applicants',
        job_id=applicant.job_id
    )