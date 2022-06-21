from django import forms
from .models import Investimento


class InvestimentoForm(forms.ModelForm):
    class Meta:
        model = Investimento

        fields = [
            "nome",
            "valor",
            "data_entrada",
            "data_saida",
            "proprietario_id"
        ]
