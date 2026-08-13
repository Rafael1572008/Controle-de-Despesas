from django.db import models

class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    valor = models.IntegerField()
    categoria = models.CharField(max_length=100)
    data_da_despesa = models.IntegerField()
    

def __str__(self):
    return self.nome
# Create your models here.
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
