from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from Auth.views import IndexView

admin.site.site_header = 'Communere Test Task'
admin.site.index_title = 'Dashboard'
admin.site.site_title = 'Communere'

urlpatterns = [
    path("",IndexView.as_view()),
    path('admin/', admin.site.urls),
    path("auth/",include("Auth.urls")),
    path("projects/",include("Projects.urls")),
    path("tasks/",include("Tasks.urls")),
]
