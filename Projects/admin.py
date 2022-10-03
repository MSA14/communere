from django.contrib import admin
from .models import *
#######################################################################

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "title",
        "created_at",
        "updated_at",
        "status",
    ]

    search_fields = [
        "id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "title",
    ]

    list_filter = [
        "status",
    ]