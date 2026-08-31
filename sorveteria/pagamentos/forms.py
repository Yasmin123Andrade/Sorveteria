from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['fk_Pedido', 'forma_pagamento', 'valor_total']