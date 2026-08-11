from django.contrib import admin
from .models import Pedido_Produto, Pedidos



class PedidoProdutoInline(admin.TabularInline):
    model = Pedido_Produto
    extra = 1


@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_pessoa', 'status', 'data_pedido')
    list_filter = ('status', 'data_pedido')
    inlines = [PedidoProdutoInline] 

@admin.register(Pedido_Produto)
class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_pedido', 'fk_produto', 'quantidade', 'preco_total')