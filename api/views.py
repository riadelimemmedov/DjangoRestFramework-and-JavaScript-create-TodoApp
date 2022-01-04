from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])#note method
def apiOverview(request):
    api_urls =  {
        'List':'/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>'
    }
    return Response(api_urls)   


#*GET method
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializerObj = TaskSerializer(tasks,many=True)#all data => many=True
    return Response(serializerObj.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializerObj = TaskSerializer(tasks,many=False)#single data => many=False
    return Response(serializerObj.data)

@api_view(['POST'])
def taskCreate(request):
    serializerObj = TaskSerializer(data=request.data)
    
    if serializerObj.is_valid():
        serializerObj.save()
    return Response(serializerObj.data)


#*POST method
@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializerObj = TaskSerializer(data=request.data,instance=task)
    
    if serializerObj.is_valid():
        serializerObj.save()
    return Response(serializerObj.data)


#*DELETE method
@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    
    return Response('Item successfully delete!')