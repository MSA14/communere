# Generated by Django 4.1 on 2022-10-02 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0005_project_completion'),
        ('Tasks', '0005_task_status'),
        ('Logs', '0002_log_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Projects.project'),
        ),
        migrations.AddField(
            model_name='log',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Tasks.task'),
        ),
    ]
