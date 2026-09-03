from django.urls import path
from .views import * # Puxar tudo de views

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre/', sobre, name='sobre'),

    # Despesas
    path('despesas/', lista_despesas, name='lista_despesas'),
    path('despesas/novo/', criar_despesa, name='criar_despesa'),
    path(
        'despesas/<int:id>/',
        detalhe_despesa,
        name='detalhe_despesa'
    ),
    path(
        'despesas/editar/<int:id>/',
        editar_despesa,
        name='editar_despesa'
    ),
    path(
        'despesas/excluir/<int:id>/',
        excluir_despesa,
        name='excluir_despesa'
    ),

    # Tops
    path('tops/', lista_tops, name='lista_tops'),
    path('tops/novo/', criar_top, name='criar_top'),
    path('tops/editar/<int:id>/', editar_top, name='editar_top'),
    path('tops/excluir/<int:id>/', excluir_top, name='excluir_top'),

    # Usuário
    path('usuarios/', lista_Usuarios, name='lista_Usuarios'),
    path(
        'cadastro/',
        cadastrar_usuario,
        name='cadastrar_usuario'
    ),
]