from django.shortcuts import render

from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# Definimos la clase TaskViewSet que me dara el conjunto de vistas para manejar las operaciones CRUD.
class TaskViewSet(viewsets.ModelViewSet):
    # Defino que datos se van a mostrar y que serializador se va a utilizar.
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
