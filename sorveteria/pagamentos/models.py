from django.db import models
from pessoa.models import Pessoa


class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor:.2f}"


class Pedido(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='pedidos')
    status = models.CharField(max_length=50)
    data_pedido = models.DateField(auto_now_add=True)

    produtos = models.ManyToManyField(
        Produto, 
        through='PedidoProduto', 
        related_name='pedidos'
    )

    def __str__(self):
        return f"Pedido #{self.id} - {self.pessoa.nome}"


class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='pedidos_item')
    quantidade = models.IntegerField(default=1)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.descricao} (Pedido #{self.pedido.id})"


class Pagamento(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pagamentos')
    forma_pagamento = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pagamento R$ {self.valor_total} ({self.forma_pagamento}) - Pedido #{self.pedido.id}"