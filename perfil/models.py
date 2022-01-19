from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=60)
    # nombre = models.CharField(max_length=50)
    # apellido = models.CharField(max_length=50)
    # email = models.EmailField(max_length=255)
    # imagen_perfil = models.CharField(max_length=255)
    # link = models.CharField(max_length=255)
    # descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Post(models.Model):
    username = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    content = models.TextField()
    imagen = models.CharField(max_length=255)
    fecha = models.DateField(auto_now=False, auto_now_add=False)

class Category(models.Model):
    nombre = models.CharField(max_length=255)