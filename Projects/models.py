from django.db import models
from django.contrib.auth.models import User
import secrets,os,pathlib

class Project (models.Model):

    def file_location(instance, filename):
        path = f"projects/appendix/{instance.user.id}/"
        format = secrets.token_urlsafe(16)+pathlib.Path(filename).suffix
        return os.path.join(path, format)

    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "project_manager"
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
        related_name = 'project_developers'
    )
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title