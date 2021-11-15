from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/tasks/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskIndex(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskShow(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)
