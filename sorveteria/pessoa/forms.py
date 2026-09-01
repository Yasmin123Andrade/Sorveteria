from django import forms
from django.contrib.auth.models import User
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    
    class Meta:
        model = Pessoa
        fields = ['cpf', 'nome', 'telefone', 'rua', 'bairro', 'numero', 'cep', 'cidade', 'estado']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso. Escolha outro.")
        return username