from django import forms
from .models import Despesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = [
            'nome',
            'descricao',
            'valor',
            'categoria',
            'data_da_despesa'
        ]