from rest_framework import serializers
from Tasks.models import Task
from Projects.models import Project
#######################################################################

class TasksSerializer(serializers.ModelSerializer):

    class Meta :
        model = Task
        fields = "__all__"