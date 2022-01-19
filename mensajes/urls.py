from django.urls import path
from mensajes import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("usuarios/", views.usuarios, name='usuarios')
]