from django.urls import path
from . import views

urlpatterns = [
    # Ejemplo de URL para la vista 'home'
    path('', views.index, name='home'),
    # Agrega aquí más rutas según tus vistas
]