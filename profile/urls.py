from django.urls import path
from profile import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("usuarios/", views.usuarios, name='usuarios')
]