from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Todo
from .serializers import TodoSerialiazer

class ListReleaseView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiazer

class CreateReleaseView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiazer

class UpdateReleaseView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiazer

class DeleteReleaseView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialiazer
