from django.urls import include, path

from .views import *

app_name = 'jobs'


urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home'
    ),

    path(
        'search/',
        SearchView.as_view(),
        name='search'
    ),

    path(
        'jobs/',
        JobListView.as_view(),
        name='jobs'
    ),

    path(
        'jobs/<int:id>/',
        JobDetailsView.as_view(),
        name='jobs-detail'
    ),

    path(
        'apply/<int:job_id>/',
        ApplyJobView.as_view(),
        name='apply-job'
    ),

    path(
        'employee/dashboard/',
        EmployeeDashboardView.as_view(),
        name='employee-dashboard'
    ),

    path(
        'employee/profile/',
        EditProfileView.as_view(),
        name='employee-profile'
    ),

    path(
        'employer/dashboard/',
        include([
            path(
                '',
                DashboardView.as_view(),
                name='employer-dashboard'
            ),

            path(
                'all-applicants/',
                ApplicantsListView.as_view(),
                name='employer-all-applicants'
            ),

            path(
                'applicants/<int:job_id>/',
                ApplicantPerJobView.as_view(),
                name='employer-dashboard-applicants'
            ),

            path(
                'applicant/<int:applicant_id>/',
                applicant_detail,
                name='employer-applicant-detail'
            ),

            path(
                'mark-filled/<int:job_id>/',
                filled,
                name='job-mark-filled'
            ),

            path(
                'application/<int:applicant_id>/status/',
                update_application_status,
                name='application-status'
            ),
        ])
    ),

    path(
        'employer/jobs/create/',
        JobCreateView.as_view(),
        name='employer-jobs-create'
    ),
]