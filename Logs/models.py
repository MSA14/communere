from django.db import models
from django.contrib.auth.models import User
from Projects.models import Project
from Tasks.models import Task
#######################################################################

class LogCategory(models.Model):

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 225)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

#=====================================================================#
class Log(models.Model):

    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )
    category = models.ForeignKey(
        LogCategory,
        on_delete = models.PROTECT,
        null = True,
        blank = True,
    )
    project = models.ForeignKey(
        Project,
        on_delete = models.PROTECT,
        null = True,
        blank = True,
    )
    task = models.ForeignKey(
        Task,
        on_delete = models.PROTECT,
        null = True,
        blank = True,
    )
    title = models.CharField(
        max_length = 225,
        null = True,
        blank = True,
    )
    description = models.TextField(
        null = True,
        blank = True,
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)