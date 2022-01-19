from django.shortcuts import render
from django.http import HttpResponse

from perfil.models import *
from perfil.forms import *

# Create your views here.

def inicio(request):
 return render(request, 'perfil/inicio.html')
 
def perfiles(request):
 return render(request, 'perfil/perfiles.html')
 
def userform(request):

    if (request.method == 'POST'):
        usertemplate = myuserform(request.POST)
        if usertemplate.is_valid():
            data = usertemplate.cleaned_data
            ususario = User(username=data["Contraseña"], password=data["contraseña"])
            ususario.save()
            return render(request, 'perfil/inicio.html')
        else:
            return HttpResponse('Form no valido')
    else:
        usertemplate = myuserform()
    return render(request, 'perfil/userform.html', {"usertemplate":usertemplate})


def postform(request):

    if (request.method == 'POST'):
        posttemplate = mypostform(request.POST)
        if posttemplate.is_valid():
            data = posttemplate.cleaned_data
            post = Post(username=data["Ususario"], title=data["Titulo"], content=data["Contenido"], imagen=data["Imagen"], fecha=data["Fecha"])
            post.save()
            return render(request, 'perfil/inicio.html')
        else:
            return HttpResponse('Form no valido')
    else:
        posttemplate = mypostform()
    return render(request, 'perfil/postform.html', {"posttemplate":posttemplate})
 
def categoryform(request):

    if (request.method == 'POST'):
        categorytemplate = mycategoryform(request.POST)
        if categorytemplate.is_valid():
            data = categorytemplate.cleaned_data
            categoria = Category(nombre=data["Categoria"])
            categoria.save()
            return render(request, 'perfil/inicio.html')
        else:
            return HttpResponse('Form no valido')
    else:
        categorytemplate = mycategoryform()
    return render(request, 'perfil/categoryform.html', {"categorytemplate":categorytemplate})