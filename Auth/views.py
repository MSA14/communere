from django.shortcuts import render
from .models import Profile, RoleCategory
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Logs.models import *
#######################################################################

class IndexView(APIView):

    def get(self,request):
        return render(request,"index.html")

class SignUpView(APIView):

    def get(self,request):
        return Response(
            [
                {
                    "METHOD" : "POST",
                    "DETAIL" : "SIGING UP NEW USER",
                    "FIELDS" : "first_name (str) | last_name (str) | email (str) | username (str) | password1 (str) | password2 (str) | role_category_id (str)",
                    "HINT" : "role_category_id = 1 (Project Manager) | role_category_id = 2 (Developer)",
                }
            ]
            
        )

    #-----------------------------------------------------------------#
    def put(self,request):
        data = request.data
        if data["password1"] == data["password2"]:
            try:
                new_user = User.objects.create(
                    username = data["username"],
                    first_name = data["first_name"],
                    last_name = data["last_name"],
                    email = data["email"]
                )
                new_user.set_password(data["password2"])
                new_user.save()
                role_category = RoleCategory.objects.get(id = data["role_category_id"])
                Profile.objects.create(
                    user = new_user,
                    role = role_category
                )
                try:
                    log_category = LogCategory.objects.get(title = "user-sign-up")
                    Log.objects.create(
                        user = new_user,
                        category = log_category,
                        title = role_category.title,
                    )
                except :
                    pass
                return Response(status = status.HTTP_201_CREATED)
            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    "message":"passwords mismatch"
                },
                status = status.HTTP_400_BAD_REQUEST
            )