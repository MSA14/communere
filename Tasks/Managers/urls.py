from django.urls import path
from .views import *
#######################################################################

urlpatterns = [
    path("",TaskView.as_view()),
    path("assign/",AssignView.as_view()),
]