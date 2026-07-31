from django.urls import path
from .views import inicio, sobre

from .views import  lista_Usuarios


urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre/', sobre, name='sobre'),
    path('usuarios/', lista_Usuarios, name='lista_Usuarios'),
]