from django.contrib import admin
from .models import Pessoa # e os outros modelos do app pessoa

@admin.register(Pessoa)
class PessoasAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'telefone', 'rua', 'bairro', 'numero', 'cep', 'cidade', 'estado')
