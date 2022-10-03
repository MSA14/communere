from rest_framework.views import APIView
from rest_framework.response import Response
from Projects.models import Project
from Tasks.models import *
from .serializers import *
from rest_framework import status
from Auth.permissions import IsProjectManager
from Logs.models import *
from Core.texts import *
#######################################################################

class TaskView(APIView):

    permission_classes = [IsProjectManager]

    def get(self,request):
        return Response(
            [
                {
                    "METHOD" : "POST",
                    "DETAIL" : "RETRIEVING ALL TASKS OF A SPECIFIC PROJECT",
                    "FIELDS" : "project_id (str)"
                },
                {
                    "METHOD" : "PUT",
                    "DETAIL" : "ADD NEW TASK TO SPECIFIC PROJECT",
                    "FIELDS" : "project_id (str) | title (str) | description (str) | appendix (file)"
                }
            ]
        )

    #-----------------------------------------------------------------#
    def post(self,request):
        data = request.data
        try:
            the_project = Project.objects.get(id = data["project_id"])
            if the_project.user == request.user :
                querset = Task.objects.filter(project = the_project)
                serializer = TasksSerializer(
                    querset,
                    many = True
                )
                try:
                    log_category = LogCategory.objects.get(title = "retrieve-tasks")
                    Log.objects.create(
                        user = request.user,
                        category = log_category,
                    )
                except:
                    pass
                return Response(serializer.data)
            else :
                return Response(
                    {
                        "detail" : project_permission_denied,
                    }
                )
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    #-----------------------------------------------------------------#
    def put(self,request):
        data = request.data
        try:
            the_project = Project.objects.get(id = data["project_id"])
            if the_project.user == request.user :
                new_task = Task.objects.create(
                    user = request.user,
                    project = the_project,
                    title = data["title"],
                    description = data["description"],
                    appendix = data["appendix"],
                )
                try:
                    log_category = LogCategory.objects.get(title = "create-new-task")
                    Log.objects.create(
                        user = request.user,
                        category = log_category,
                        task = new_task
                    )
                except:
                    pass
                serializer = TasksSerializer(
                    new_task,
                    many = False
                )
                return Response(
                    serializer.data,
                    status = status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "detail" : project_permission_denied,
                    }
                )
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
                    "DETAIL" : "REMOVE DEVELOPER FROM A TASK",
                    "FIELDS" : "task_id (str) | developer_id (str)"
                },
                {
                    "METHOD" : "PUT",
                    "DETAIL" : "ADD DEVELOPER TO A TASK",
                    "FIELDS" : "task_id (str) | developer_id (str)"
                }
            ]
        )
    
    #-----------------------------------------------------------------#    
    def post(self,request):
        data = request.data
        the_task = Task.objects.get(id = data["task_id"])
        if the_task.project.user == request.user :
            the_developer = User.objects.get(id = data["developer_id"])
            the_task.developers.remove(the_developer)
            try:
                log_category = LogCategory.objects.get(title = "remove-developer-from-task")
                Log.objects.create(
                    user = request.user,
                    category = log_category,
                    task = the_task
                )
            except:
                pass
            return Response(
                {
                    "detail" : developer_removed_from_task
                },
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "detail" : project_permission_denied,
                },
                status = status.HTTP_403_FORBIDDEN
            )

    #-----------------------------------------------------------------#
    def put(self,request):
        data = request.data
        try:
            the_task = Task.objects.get(id = data["task_id"])
            if the_task.project.user == request.user :
                the_developer = User.objects.get(id = data["developer_id"])
                if the_task.project.developers.contains(the_developer):
                    the_task.developers.add(the_developer)
                    try:
                        log_category = LogCategory.objects.get(title = "add-developer-to-task")
                        Log.objects.create(
                            user = request.user,
                            category = log_category,
                            task = the_task
                        )
                    except:
                        pass
                    return Response(
                        {
                            'detail' : developer_added_to_task
                        },
                        status = status.HTTP_200_OK
                    )
                else:
                    return Response(
                    {
                        "detail" : developer_project_permission_denied,
                    },
                    status = status.HTTP_403_FORBIDDEN
                )
            else:
                return Response(
                    {
                        "detail" : project_permission_denied,
                    },
                    status = status.HTTP_403_FORBIDDEN
                ) 
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)             

    