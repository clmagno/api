from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializer import EventSerializer  
# Create your views here.
class drink_list(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        drinks = Event.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def allEvent(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvent(request,id):
    event = Event.objects.filter(id=id).values()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def putEvent(request,id):
    serializer = EventSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)