from django.shortcuts import render
from django.http import HttpResponse

from perfil.models import User

# Create your views here.

def inicio(request):
 return render(request, 'perfil/inicio.html')
 
def perfiles(request):
 return render(request, 'perfil/perfiles.html')
 
def perfilesformulario(request):

    print(request.POST)

    if request.method == 'POST':
        perfil = User(username=request.POST["nombre"], password=request.POST["contra"])
        
        perfil.save()
        return render(request, 'perfil/perfilesformulario.html')

    return render(request, 'perfil/perfilesformulario.html')
