from django.urls import path
from perfil import views

urlpatterns = [
    path("", views.inicio, name='inicioperfil'),
    path("perfiles/", views.perfiles, name='perfiles'),
    path("userform/", views.userform, name='userform'),
    path("postform/", views.postform, name='postform'),
    path("categoryform/", views.categoryform, name='categoryform'),
]