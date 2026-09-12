from django import forms
from django.utils import timezone

from jobsapp.models import Applicant, Job


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{css} form-control'.strip()


class CreateJobForm(StyledModelForm):
    last_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Application deadline',
    )
    salary_min = forms.IntegerField(min_value=0, required=False, label='Minimum salary (₹/year)')
    salary_max = forms.IntegerField(min_value=0, required=False, label='Maximum salary (₹/year)')

    class Meta:
        model = Job
        exclude = ('user', 'created_at', 'updated_at', 'filled')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 7}),
            'company_description': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.TextInput(attrs={'placeholder': 'Python, Django, REST API, SQL'}),
        }

    def clean(self):
        cleaned = super().clean()
        deadline = cleaned.get('last_date')
        minimum = cleaned.get('salary_min')
        maximum = cleaned.get('salary_max')
        if deadline and deadline <= timezone.now():
            self.add_error('last_date', 'The application deadline must be in the future.')
        if minimum and maximum and minimum > maximum:
            self.add_error('salary_max', 'Maximum salary must be greater than or equal to minimum salary.')
        return cleaned


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('status',)
        widgets = {'status': forms.Select(attrs={'class': 'form-control form-control-sm'})}
