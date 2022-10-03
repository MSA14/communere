from django.urls import path
from .views import *

urlpatterns = [
    path("",ProjectView.as_view()),
    path("assign/",AssignView.as_view()),
]