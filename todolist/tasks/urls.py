from django.urls import path, include
# Clase que genera automáticamente las rutas necesarias para manejar operaciones CRUD en la API.
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Instancia de DefaultRouter que encargará de registrar y generar automáticamente 
# las rutas necesarias para los endpoints RESTful basados en un ViewSet.
# TaskViewSet manejará todas las operaciones CRUD para tareas.
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# Creamos una ruta base API que incluirá las rutas generadas por DefaultRouter.
urlpatterns = [
    path('api/', include(router.urls)),
]
