from django.db import models
from django.contrib.auth.models import User
import secrets,pathlib,os
from Projects.models import Project

class Task (models.Model):

    def file_location(instance, filename):
        path = f"tasks/appendix/{instance.user.id}/"
        format = secrets.token_urlsafe(16)+pathlib.Path(filename).suffix
        return os.path.join(path, format)

    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "task_creator"
    )
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,
    )
    title = models.CharField(max_length = 225)
    description = models.TextField(
        null = True,
        blank = True,
    )
    appendix = models.FileField(
        upload_to = file_location,
        null = True,
        blank = True,
    )
    developers = models.ManyToManyField(
        User,
        blank = True,
        related_name = 'task_developers'
    )
    completion = models.IntegerField(default = 0)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)