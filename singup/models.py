from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
