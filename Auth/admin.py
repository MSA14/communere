from django.contrib import admin
from .models import *

#---------------------------------------------------------------------#
@admin.register(RoleCategory)
class RoleCategoryAdmin(admin.ModelAdmin):
    
    list_display = [
        "id",
        "title",
        "created_at",
        "updated_at",
    ]

#---------------------------------------------------------------------#
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "role",
    ]

    list_filter = [
        "role"
    ]

    search_fields = [
        "user__username",
        "user__first_name",
        "user__last_name",
    ]

#---------------------------------------------------------------------#