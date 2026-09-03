from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta

from .models import Usuario, Despesa, Top
from .forms import DespesaForm, TopForm, UsuarioForm



@login_required
def preencher_despesas_massa(request):
    tops_nomes = [
        ("Alimentação", "Mercado, refeições e delivery", True),
        ("Moradia", "Aluguel, condomínio e contas da casa", True),
        ("Transporte", "Combustível, transporte e manutenção", True),
        ("Lazer", "Passeios, assinaturas e entretenimento", True),
        ("Saúde", "Consultas, exames e farmácia", True),
    ]

    tops = {}

    for nome, descricao, eh_debito in tops_nomes:
        top, _ = Top.objects.get_or_create(
            usuario=request.user,
            nome=nome,
            defaults={
                "descricao": descricao,
                "eh_debito": eh_debito,
            }
        )
        tops[nome] = top

    dados = [
        ("Supermercado", "Compras do mês", "Alimentação", 486.90, -25),
        ("Restaurante", "Almoço", "Alimentação", 68.50, -18),
        ("Delivery", "Jantar", "Alimentação", 52.90, -7),
        # ...
    ]

    hoje = timezone.localdate()

    despesas = [
        Despesa(
            nome=f"{nome} {i + 1}",
            descricao=descricao,
            valor=Decimal(str(valor)),
            data_da_despesa=hoje + timedelta(days=dias),
            usuario=request.user,
            top=tops[top_nome],
        )
        for i, (nome, descricao, top_nome, valor, dias)
        in enumerate(dados)
    ]

    Despesa.objects.bulk_create(despesas)

    return redirect("lista_despesas")


@login_required
def dashboard(request):
    despesas = Despesa.objects.filter(usuario=request.user).select_related('top')
    hoje = timezone.localdate()

    total_geral = sum((d.valor for d in despesas), 0)
    baixadas = [d for d in despesas if d.data_da_despesa <= hoje]
    agendadas = [d for d in despesas if d.data_da_despesa > hoje]
    total_baixado = sum((d.valor for d in baixadas), 0)
    total_agendado = sum((d.valor for d in agendadas), 0)

    por_top = {}
    for despesa in despesas:
        nome = despesa.top.nome
        if nome not in por_top:
            por_top[nome] = {'nome': nome, 'total': 0, 'baixado': 0, 'agendado': 0}
        por_top[nome]['total'] += despesa.valor
        if despesa.data_da_despesa <= hoje:
            por_top[nome]['baixado'] += despesa.valor
        else:
            por_top[nome]['agendado'] += despesa.valor

    top_resumo = sorted(por_top.values(), key=lambda item: item['total'], reverse=True)

    return render(request, 'core/dashboard.html', {
        'total_geral': total_geral,
        'total_baixado': total_baixado,
        'total_agendado': total_agendado,
        'chart_status': [float(total_baixado), float(total_agendado)],
        'top_labels': [item['nome'] for item in top_resumo],
        'top_values': [float(item['total']) for item in top_resumo],
        'top_resumo': top_resumo,
    })

@login_required
def lista_despesas(request):
    despesas = Despesa.objects.filter(usuario=request.user).select_related('top')
    tops = Top.objects.filter(usuario=request.user).order_by('nome')
    return render(
        request,
        'core/lista_despesas.html',
        {'despesas': despesas, 'tops': tops}
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