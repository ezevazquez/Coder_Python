from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    nombre = models.CharField(max_length=50)
