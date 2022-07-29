from django.shortcuts import render
from .serializers import RoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class RoomsList(APIView):
    """
    List all rooms, or create a new room.
    """

    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        print()
        return Response(serializer.data)

    def post(self, request, format=None):
        print("peticion rooms", request.data)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)