from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'core/inicio.html')

def sobre(request):
    return render(request, 'core/sobre.html')

def curso(request):
    contexto = {
        'nome_curso': 'Curso Técnico em Desenvolvimento de Sistemas',
        'professor': 'Professor Exemplo',
        'carga_horaria': 1200,
        'disciplinas': ['Python', 'Banco de Dados', 'Django', 'HTML e CSS'],
        'turno': 'Noturno'
    }
    return render(request, 'core/curso.html', contexto)


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'core/lista_livros.html', {'livros': livros})
def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'core/detalhe_livro.html', {'livro': livro})

@login_required   
def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_livros')

    else:
        form = LivroForm()

    return render(request, 'core/form_livro.html', {'form': form})

@login_required
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            form.save()
            return redirect('lista_livros')

    else:
        form = LivroForm(instance=livro)

    return render(request, 'core/form_livro.html', {'form': form})

@login_required
def excluir_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')

    return render(request, 'core/excluir_livro.html', {'livro': livro})