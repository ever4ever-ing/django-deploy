from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('producto/nuevo/', views.crear_producto, name='crear_producto'),
]