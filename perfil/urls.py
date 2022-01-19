from django.urls import path
from perfil import views

urlpatterns = [
    path("", views.inicio, name='inicioperfil'),
    path("perfiles/", views.perfiles, name='perfiles'),
    path("perfilesformulario/", views.perfilesformulario, name='perfilesformulario')
]