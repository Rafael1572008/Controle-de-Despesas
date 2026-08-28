from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Despesa
from .forms import DespesaForm
from django.contrib.auth.decorators import login_required

# Models
from .models import Usuario

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

def excluir_despesa(request, id):
    get_object_or_404(
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
        form = DespesaForm(request.POST)

        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.usuario = request.user
            despesa.save()
            return redirect('lista_despesas')

    else:
        form = DespesaForm()

    return render(request, 'core/form_despesa.html', {'form': form})
def lista_Usuarios(request):
    Usuarios = Usuario.objects.all()
    return render(request, 'core/lista_Usuarios.html', {'Usuarios': Usuarios})



# Create your views here.

@login_required
def detalhe_despesa(request, id):
    get_object_or_404(
        Despesa,
        id=id,
        usuario=request.user
    )
    return render(request, 'core/detalhe_despesa.html', {'despesa': despesa})

@login_required
def editar_despesa(request, id):
    get_object_or_404(
        Despesa,
        id=id,
        usuario=request.user
    )

    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)

        if form.is_valid():
            form.save()
            return redirect('lista_despesas')

    else:
        form = DespesaForm(instance=despesa)

    return render(request, 'core/form_despesa.html', {'form': form})