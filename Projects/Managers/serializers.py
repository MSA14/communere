from rest_framework import serializers
from Projects.models import *
from django.contrib.auth.models import User

#=====================================================================#
class ProjectsSerializer(serializers.ModelSerializer):

    class Meta :
        model = Project
        fields = "__all__"

    class UserSerializer(serializers.ModelSerializer):
        
        class Meta :
            model = User
            fields = [
                "id",
                "username",
                "first_name",
                "last_name",
            ]

    user = UserSerializer()
    developers = UserSerializer(many = True)

#=====================================================================#
