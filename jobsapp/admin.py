from django.contrib import admin

from .models import Applicant, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'work_mode', 'type', 'last_date', 'filled')
    list_filter = ('work_mode', 'type', 'category', 'filled')
    search_fields = ('title', 'company_name', 'location', 'skills')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('user__email', 'user__first_name', 'job__title', 'job__company_name')
    readonly_fields = ('created_at', 'updated_at')
