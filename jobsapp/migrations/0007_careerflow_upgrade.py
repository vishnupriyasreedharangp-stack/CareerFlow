from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [('jobsapp', '0006_auto_20190408_2005'), ('accounts', '0003_careerflow_profile')]

    operations = [
        migrations.AlterField(
            model_name='job', name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(model_name='job', name='experience', field=models.CharField(default='0-2 years', max_length=100)),
        migrations.AddField(model_name='job', name='salary_min', field=models.PositiveIntegerField(blank=True, null=True)),
        migrations.AddField(model_name='job', name='salary_max', field=models.PositiveIntegerField(blank=True, null=True)),
        migrations.AddField(model_name='job', name='skills', field=models.CharField(blank=True, default='', max_length=500)),
        migrations.AddField(model_name='job', name='work_mode', field=models.CharField(choices=[('onsite', 'On-site'), ('hybrid', 'Hybrid'), ('remote', 'Remote')], default='onsite', max_length=20)),
        migrations.AddField(model_name='job', name='updated_at', field=models.DateTimeField(auto_now=True)),
        migrations.AlterField(model_name='job', name='company_description', field=models.CharField(max_length=500)),
        migrations.AlterField(model_name='job', name='website', field=models.URLField(blank=True, default='')),
        migrations.AlterField(model_name='applicant', name='user', field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
        migrations.AddField(model_name='applicant', name='status', field=models.CharField(choices=[('submitted', 'Submitted'), ('reviewing', 'Under review'), ('shortlisted', 'Shortlisted'), ('rejected', 'Rejected'), ('hired', 'Hired')], default='submitted', max_length=20)),
        migrations.AddField(model_name='applicant', name='updated_at', field=models.DateTimeField(auto_now=True)),
        migrations.AddConstraint(model_name='applicant', constraint=models.UniqueConstraint(fields=('user', 'job'), name='unique_user_job_application')),
        migrations.AddIndex(model_name='job', index=models.Index(fields=['category'], name='jobsapp_job_categor_9d8b7a_idx')),
        migrations.AddIndex(model_name='job', index=models.Index(fields=['location'], name='jobsapp_job_locatio_4d1a70_idx')),
        migrations.AddIndex(model_name='job', index=models.Index(fields=['work_mode'], name='jobsapp_job_work_m_3a1b2c_idx')),
        migrations.AddIndex(model_name='job', index=models.Index(fields=['last_date'], name='jobsapp_job_last_da_7e4f91_idx')),
    ]
