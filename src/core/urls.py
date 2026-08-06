from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre/', sobre, name='sobre'),
    path('despesas/', lista_despesas, name='lista_despesas'),
    path('despesas/novo/', criar_despesa, name='criar_despesa'),
    path('despesas/<int:id>/', detalhe_despesa, name='detalhe_depesa'),
    path('despesas/editar/<int:id>/', editar_despesa, name='editar_despesa')
]