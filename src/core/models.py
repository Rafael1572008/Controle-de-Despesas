from django.contrib.auth.models import AbstractUser # Herança da tabela de user padão
from django.db import models


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Top(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    eh_debito = models.BooleanField(default=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="tops"
    )

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_da_despesa = models.DateField()

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="despesas"
    )

    top = models.ForeignKey(
        Top,
        on_delete=models.PROTECT,
        related_name="despesas"
    )

    def __str__(self):
        return self.nome