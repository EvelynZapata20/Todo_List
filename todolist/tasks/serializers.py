from rest_framework import serializers
from .models import Task

# Definimos la clase TaskSerializer que hereda de ModelSerializer.
# Es la encargada transformar los datos del modelo Task a JSON.
class TaskSerializer(serializers.ModelSerializer):
    # Meta clase que define el modelo y los campos a serializar.
    class Meta:
        model = Task
        fields = '__all__'
