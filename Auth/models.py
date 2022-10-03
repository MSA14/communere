from django.db import models
from django.contrib.auth.models import User

#---------------------------------------------------------------------#
class RoleCategory (models.Model):

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 225)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

#---------------------------------------------------------------------#
class Profile (models.Model) :

    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    role = models.ForeignKey(
        RoleCategory,
        on_delete = models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username

#---------------------------------------------------------------------#