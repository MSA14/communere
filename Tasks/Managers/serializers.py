from Tasks.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
#######################################################################

class TasksSerializer(serializers.ModelSerializer):

    class Meta :
        model = Task
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
    
    developers = UserSerializer(many = True)

