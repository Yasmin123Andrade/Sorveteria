from django import forms
from .models import Pedidos

class PedidosForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user and not user.has_perm('pedidos.change_pedidos'):
            self.fields.pop('fk_pessoa')

    class Meta:
        model = Pedidos
        fields = ['fk_pessoa', 'status', 'data_pedido']
        widgets = {
            'data_pedido': forms.DateInput(attrs={'type': 'date'}),
        }