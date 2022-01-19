from django.urls import path
from perfil import views

urlpatterns = [
    path("", views.inicio, name='inicioperfil'),
    path("userform/", views.userform, name='userform'),
    path("postform/", views.postform, name='postform'),
    path("categoryform/", views.categoryform, name='categoryform'),
    path("userbusqueda/", views.userbusqueda, name='userbusqueda'),
    path("buscar/", views.buscar, name='buscar'),
]