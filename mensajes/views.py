from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(req):
 return HttpResponse(f'Inicio Mensajes')
 
def usuarios(req):
 return HttpResponse(f'Formulario Mensajes')
