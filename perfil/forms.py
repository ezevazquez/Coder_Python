from django import forms 

class myuserform(forms.Form):
    Usuario = forms.CharField(max_length=40)
    Contraseña = forms.CharField(max_length=60)

class mypostform(forms.Form):
    Usuario = forms.CharField(max_length=40)
    Titulo = forms.CharField(max_length=40)
    Contenido = forms.Textarea()
    Imagen = forms.CharField(max_length=255)
    Fecha = forms.DateField()

class mycategoryform(forms.Form):
    Categoria = forms.CharField(max_length=40)