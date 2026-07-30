from django.shortcuts import render 
from django.http import HttpResponse

def inicio(request):
    return render(request, 'core/inicio.html')  

def sobre(request):
    return HttpResponse("Esta página foi criada para apresentar o sistema.")

# Create your views here.
