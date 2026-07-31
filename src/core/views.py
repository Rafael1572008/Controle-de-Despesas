from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Models
from .models import Usuario

def inicio(request):
    return render(request, 'core/inicio.html')  

def sobre(request):
    return HttpResponse("Esta página foi criada para apresentar o sistema.")

def lista_Usuarios(request):
    Usuarios = Usuario.objects.all()
    return render(request, 'core/lista_Usuarios.html', {'Usuarios': Usuarios})



# Create your views here.
