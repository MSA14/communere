from rest_framework import serializers
from .models import *

class RoleCategoryListSerializer(serializers.ModelSerializer):

    class Meta :
        model = RoleCategory
        fields = [
            "id",
            "title",
        ]