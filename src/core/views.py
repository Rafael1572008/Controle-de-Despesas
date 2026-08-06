from django.shortcuts import render 
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Despesa
from .forms import DespesaForm
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'core/inicio.html')  

def sobre(request):
    return HttpResponse("Esta página foi criada para apresentar o sistema.")

def lista_despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'core/lista_despesas.html', {'despesas': despesas})

@login_required   
def criar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_despesas')

    else:
        form = DespesaForm()

    return render(request, 'core/form_despesa.html', {'form': form})
# Create your views here.

@login_required
def detalhe_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    return render(request, 'core/detalhe_despesa.html', {'despesa': despesa})

@login_required
def editar_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)

    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)

        if form.is_valid():
            form.save()
            return redirect('lista_despesas')

    else:
        form = DespesaForm(instance=despesa)

    return render(request, 'core/form_despesa.html', {'form': form})