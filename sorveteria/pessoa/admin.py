from django.contrib import admin
from .models import Pessoa, Endereco, Pedido, Produto, PedidoProduto


class EnderecoInline(admin.StackedInline):
    model = Endereco
    can_delete = False


class PedidoProdutoInline(admin.TabularInline):
    model = PedidoProduto
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email', 'telefone')
    search_fields = ('nome', 'cpf', 'email')
    inlines = [EnderecoInline]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'categoria', 'valor')
    list_filter = ('categoria',)
    search_fields = ('descricao',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'data_pedido', 'valor_total', 'forma_pagamento')
    list_filter = ('data_pedido', 'forma_pagamento')
    inlines = [PedidoProdutoInline]


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'cidade', 'estado', 'cep')


@admin.register(PedidoProduto)
class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade_produto', 'preco_total')