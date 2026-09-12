from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('accounts', '0002_auto_20190326_1754')]

    operations = [
        migrations.AlterField(
            model_name='user', name='role',
            field=models.CharField(choices=[('employee', 'Candidate'), ('employer', 'Employer')], default='employee', max_length=12),
        ),
        migrations.AlterField(
            model_name='user', name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='', max_length=10),
        ),
    ]
