from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   
from .views import *
#######################################################################

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name='auth-token'),
    path("token/refresh/", TokenRefreshView.as_view(), name='refresh-token'),
    path("sign-up/",SignUpView.as_view(),name = "sign-up"),
]