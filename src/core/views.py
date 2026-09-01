from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Usuario, Despesa, Top
from .forms import DespesaForm, TopForm, UsuarioForm

def inicio(request):
    return render(request, 'core/inicio.html')  

def sobre(request):
    return HttpResponse("Esta página foi criada para apresentar o sistema.")

@login_required
def lista_despesas(request):
    despesas = Despesa.objects.filter(usuario=request.user)
    return render(
        request,
        'core/lista_despesas.html',
        {'despesas': despesas}
    )

@login_required
def excluir_despesa(request, id):
    despesa = get_object_or_404(
        Despesa,
        id=id,
        usuario=request.user
    )
    
    if request.method == 'POST':
        despesa.delete()
        return redirect('lista_despesas')
    
    return redirect('lista_despesas')


@login_required   
def criar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(
            request.POST,
            usuario=request.user
        )

        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            return redirect('lista_despesas')

    else:
        form = DespesaForm(usuario=request.user)

    return render(request, 'core/form_despesa.html', {'form': form})


@login_required
def detalhe_despesa(request, id):
    despesa = get_object_or_404(
        Despesa,
        id=id,
        usuario=request.user
    )
    return render(request, 'core/detalhe_despesa.html', {'despesa': despesa})

@login_required
def editar_despesa(request, id):
    despesa = get_object_or_404(
        Despesa,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':
        form = DespesaForm(
            request.POST,
            instance=despesa,
            usuario=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('lista_despesas')

    else:
        form = DespesaForm(
            instance=despesa,
            usuario=request.user
        )

    return render(request, 'core/form_despesa.html', {'form': form})


# Tops
# Listar Tops
@login_required
def lista_tops(request):
    tops = Top.objects.filter(usuario=request.user)

    return render(
        request,
        'core/lista_tops.html',
        {'tops': tops}
    )


# Criar
@login_required
def criar_top(request):

    if request.method == 'POST':
        form = TopForm(request.POST)

        if form.is_valid():
            top = form.save(commit=False)
            top.usuario = request.user
            top.save()

            return redirect('lista_tops')

    else:
        form = TopForm()

    return render(
        request,
        'core/form_top.html',
        {'form': form}
    )

# Editar
@login_required
def editar_top(request, id):

    top = get_object_or_404(
        Top,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':
        form = TopForm(request.POST, instance=top)

        if form.is_valid():
            form.save()
            return redirect('lista_tops')

    else:
        form = TopForm(instance=top)

    return render(
        request,
        'core/form_top.html',
        {'form': form}
    )

# Excluir
@login_required
def excluir_top(request, id):

    top = get_object_or_404(
        Top,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':
        top.delete()
        return redirect('lista_tops')

    return redirect('lista_tops')

# Usuário
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UsuarioForm()

    return render(request, 'core/cadastro.html', {'form': form})

def lista_Usuarios(request):
    Usuarios = Usuario.objects.all()
    return render(request, 'core/lista_Usuarios.html', {'Usuarios': Usuarios})