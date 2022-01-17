import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(req):
 return render(req, 'registro/inicio.hrml')
 
def usuarios(req):
 return render(req, 'registro/usuarios.html')
