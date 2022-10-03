from django.urls import path,include
from Tasks.Developers.urls import urlpatterns as developers_url_patterns
from Tasks.Managers.urls import urlpatterns as managers_url_patterns

urlpatterns = [
    path("developers/",include(developers_url_patterns)),
    path("managers/",include(managers_url_patterns)),
]