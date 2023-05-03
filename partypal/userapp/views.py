from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer


@api_view(['GET'])
def apiOverview(request):
    """
    List all code snippets, or create a new snippet.
    """
    api_urls = {
        'List':'/event-list/',  
        'Detail View':'/event-detail/<str:pk>/',
        'Create':'/event-create/',
        'Update':'/event-update/<str:pk>/',
        'Delete':'/event-delete/<str:pk>/',
    }
    return Response(api_urls) # safe=False allows for lists to be returned




# ------------- USER -----------------
@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def userDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer  = UserSerializer(users, many=False)


@api_view(['POST'])
def createUser(request):
    users = User.objects.all()
    # serializers = UserSerializer(data=request.data)
    # if serializers.is_valid():
    #     serializers.save()


    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors)
    # return Response(serializers.data)

@api_view(['PUT'])
def updateUser(request, pk):
    users = User.objects.get(id=pk)
    serializers = UserSerializer(instance=users, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


