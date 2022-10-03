from rest_framework.views import APIView
from rest_framework.response import Response
from Projects.models import *
from .serializers import *
from rest_framework import status
from Auth.permissions import IsProjectManager
from Core.texts import *
from Logs.models import *
#######################################################################

class ProjectView(APIView):

    permission_classes = [IsProjectManager]

    def get(self,request):
        return Response(
            [
                {
                    "METHOD" : "POST",
                    "DETAIL" : "RETRIEVE ALL OF YOUR PROJECTS",
                },
                {
                    "METHOD" : "PUT",
                    "DETAIL" : "CREATE NEW PROJECT",
                    "FIELDS" : "title (str) | description (str) | appendix (file)",
                }
            ]
        )

    def post(self,request):
        try:
            queryset  = Project.objects.filter(user = request.user)
            serializer = ProjectsSerializer(
                queryset,
                many = True,
            )
            try:
                log_category = LogCategory.objects.get(title = "retrieve-projects")
                Log.objects.create(
                    user = request.user,
                    category = log_category
                )
            except:
                pass
            return Response(serializer.data)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    #-----------------------------------------------------------------#
    def put(self,request):
        data = request.data
        try:
            new_project = Project.objects.create(
                user = request.user,
                title = data["title"],
                description = data["description"],
                appendix = data["appendix"]
            )
            try:
                log_category = LogCategory.objects.get(title = "create-new-project")
                Log.objects.create(
                    user = request.user,
                    category = log_category,
                    project = new_project,
                )
            except:
                pass
            serializer = ProjectsSerializer(
                new_project,
                many = False
            )
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

#=====================================================================#
class AssignView(APIView):

    permission_classes = [IsProjectManager]

    def get(self,request):
        return Response(
            [
                {
                    "METHOD" : "POST",
                    "DETAIL" : "REMOVE DEVELOPER FROM YOUR PROJECTS",
                    "FIELDS" : "project_id (str) | developer_id (str)",
                },
                {
                    "METHOD" : "PUT",
                    "DETAIL" : "ADD DEVELOPER TO YOUR PROJECTS",
                    "FIELDS" : "project_id (str) | developer_id (str)",
                }
            ]
        )

    #-----------------------------------------------------------------#
    def post(self,request):
        data = request.data
        try :
            the_project = Project.objects.get(id = data["project_id"])
            if the_project.user == request.user :
                the_developer = User.objects.get(
                    id = data["developer_id"]
                )
                the_project.developers.remove(the_developer)
                try:
                    log_category = LogCategory.objects.get(title = "remove-developer-from-project")
                    Log.objects.create(
                        user = request.user,
                        category = log_category,
                        project = the_project,
                    )
                except:
                    pass
                return Response(
                    {
                        "detail" : developer_removed_from_project
                    }
                )
            else:
                return Response(
                    {
                        "detail" : project_permission_denied
                    },
                    status = status.HTTP_403_FORBIDDEN
                )
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    #-----------------------------------------------------------------#
    def put(self,request):
        data = request.data
        try:
            the_project = Project.objects.get(id = data["project_id"])
            if the_project.user == request.user :
                the_developer = User.objects.get(
                    id = data["developer_id"]
                )
                the_project.developers.add(the_developer)
                try:
                    log_category = LogCategory.objects.get(title = "add-developer-to-project")
                    Log.objects.create(
                        user = request.user,
                        category = log_category,
                        project = the_project,
                    )
                except:
                    pass
                return Response(
                    {
                        "detail" : developer_added_to_project
                    },
                    status = status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "detail" : project_permission_denied
                    },
                    status = status.HTTP_403_FORBIDDEN
                )
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    
