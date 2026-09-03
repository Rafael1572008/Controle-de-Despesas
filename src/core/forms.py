from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Despesa, Top, Usuario

class DespesaForm(forms.ModelForm):

    class Meta:
        model = Despesa 
        fields = [
            'nome',
            'descricao',
            'valor',
            'data_da_despesa',
            'top',
        ]
        widgets = {
            'data_da_despesa': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['top'].queryset = Top.objects.filter(
            usuario=usuario
        )

class TopForm(forms.ModelForm):

    class Meta:
        model = Top
        fields = [
            'nome',
            'descricao',
            'eh_debito',
        ]


class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = [
            'username',
            'nome',
            'email',
        ]