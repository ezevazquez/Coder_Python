from django.urls import path
from singup import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("usuarios/", views.usuarios, name='usuarios')
]