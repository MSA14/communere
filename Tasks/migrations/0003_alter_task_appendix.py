# Generated by Django 4.1 on 2022-09-30 12:56

import Tasks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='appendix',
            field=models.FileField(blank=True, null=True, upload_to=Tasks.models.Task.file_location),
        ),
    ]