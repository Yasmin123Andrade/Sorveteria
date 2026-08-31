from django import forms
from .models import Pedidos

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['fk_pessoa', 'status', 'data_pedido']
        widgets = {
            'data_pedido': forms.DateInput(attrs={'type': 'date'}),
        }