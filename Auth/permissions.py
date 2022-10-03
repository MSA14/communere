from rest_framework import permissions
from .models import Profile


class IsProjectManager(permissions.BasePermission):

    message='You Do Not Have The Permission To Access This End-Point'

    def has_permission(self, request, view):
        try :
            Profile.objects.get(
            user = request.user,
            role__title = "Project Manager")
            return True
        except:
            return False

#=====================================================================#
class IsDeveloper(permissions.BasePermission):

    message='You Do Not Have The Permission To Access This End-Point'

    def has_permission(self, request, view):
        try :
            Profile.objects.get(
            user = request.user,
            role__title = "Developer")
            return True
        except:
            return False

