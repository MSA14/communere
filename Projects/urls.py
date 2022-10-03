from django.urls import path,include
from Projects.Developers.urls import urlpatterns as developers_url_patterns
from Projects.Managers.urls import urlpatterns as managers_url_patterns

urlpatterns = [
    path("managers/",include(managers_url_patterns)),
    path("developers/",include(developers_url_patterns)),
]