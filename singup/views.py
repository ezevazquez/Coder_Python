from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(req):
 return render(req, 'singup/inicio.html')
 
def usuarios(req):
 return render(req, 'singup/usuarios.html')
