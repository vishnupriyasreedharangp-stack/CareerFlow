from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from jobsapp.forms import CreateJobForm
from jobsapp.models import Applicant, Job


def open_jobs_queryset():
    return Job.objects.filter(filled=False, last_date__gte=timezone.now())


class HomeView(ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return open_jobs_queryset()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_jobs'] = open_jobs_queryset().count()
        context['total_companies'] = open_jobs_queryset().values('company_name').distinct().count()
        context['categories'] = (
            open_jobs_queryset().exclude(category='').values_list('category', flat=True).distinct().order_by('category')
        )
        context['latest_jobs'] = open_jobs_queryset()[:8]
        return context


class SearchView(ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'
    paginate_by = 8

    def get_queryset(self):
        queryset = open_jobs_queryset()
        position = self.request.GET.get('position', '').strip()
        location = self.request.GET.get('location', '').strip()
        category = self.request.GET.get('category', '').strip()
        work_mode = self.request.GET.get('work_mode', '').strip()
        job_type = self.request.GET.get('type', '').strip()

        if position:
            queryset = queryset.filter(
                Q(title__icontains=position)
                | Q(description__icontains=position)
                | Q(skills__icontains=position)
                | Q(company_name__icontains=position)
            )
        if location:
            queryset = queryset.filter(location__icontains=location)
        if category:
            queryset = queryset.filter(category=category)
        if work_mode:
            queryset = queryset.filter(work_mode=work_mode)
        if job_type:
            queryset = queryset.filter(type=job_type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Job.objects.values_list('category', flat=True).distinct().order_by('category')
        context['query'] = self.request.GET.get('position', '')
        return context


class JobListView(ListView):
    model = Job
    template_name = 'jobs/jobs.html'
    context_object_name = 'jobs'
    paginate_by = 8

    def get_queryset(self):
        return open_jobs_queryset()


class JobDetailsView(DetailView):
    model = Job
    template_name = 'jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exist")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_applied'] = bool(
            user.is_authenticated and Applicant.objects.filter(user=user, job=self.object).exists()
        )
        context['related_jobs'] = open_jobs_queryset().filter(category=self.object.category).exclude(pk=self.object.pk)[:3]
        return context


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class ApplyJobView(CreateView):
    model = Applicant

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employee':
            messages.error(request, 'Only employee accounts can apply for jobs.')
            return redirect('jobs:jobs-detail', id=kwargs['job_id'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=kwargs['job_id'])
        if not job.is_open:
            messages.error(request, 'This job is no longer accepting applications.')
        elif Applicant.objects.filter(user=request.user, job=job).exists():
            messages.info(request, 'You have already applied for this position.')
        else:
            Applicant.objects.create(user=request.user, job=job)
            messages.success(request, f'Application submitted for {job.title}.')
        return redirect('jobs:jobs-detail', id=job.id)


@method_decorator(login_required(login_url=reverse_lazy('accounts:login')), name='dispatch')
class JobCreateView(CreateView):
    template_name = 'jobs/create.html'
    form_class = CreateJobForm
    extra_context = {'title': 'Post a New Job'}
    success_url = reverse_lazy('jobs:employer-dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != 'employer':
            messages.error(request, 'Only employer accounts can post jobs.')
            return redirect('jobs:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
