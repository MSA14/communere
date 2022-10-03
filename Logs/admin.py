from django.contrib import admin
from .models import *
#######################################################################

admin.site.register(LogCategory)

#=====================================================================#
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    
    list_display = [
        "id",
        "user",
        "category",
        "title",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "category"
    ]

    search_fields = [
        "user__username",
        "user__first_name",
        "user__last_name",
        "title",
    ]

