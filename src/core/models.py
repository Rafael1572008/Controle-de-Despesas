from django.db import models

class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    valor = models.IntegerField()
    categoria = models.CharField(max_length=100)
    data_da_despesa = models.IntegerField()
    

def __str__(self):
    return self.nome