from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from registro import views

urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("usuarios/", views.usuarios, name='usuarios')
]