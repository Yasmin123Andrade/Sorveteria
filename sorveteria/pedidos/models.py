from django.db import models


class Pedidos(models.Model):
    fk_pessoa = models.ForeignKey(
        'pessoa.Pessoa', 
        on_delete=models.CASCADE, 
        related_name='pedidos'
    )
    status = models.CharField(max_length=50)
    data_pedido = models.DateField()


    def __str__(self):
        return f"Pedido {self.id} - Status: {self.status}"


class Pedido_Produto(models.Model):
    fk_pedido = models.ForeignKey(
        Pedidos, 
        on_delete=models.CASCADE, 
        related_name='itens_pedido'
    )
  
    fk_produto = models.ForeignKey(
        'produtos.Produto', 
        on_delete=models.CASCADE, 
        related_name='itens_pedido'
    )
    quantidade = models.IntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('fk_pedido', 'fk_produto')

    def __str__(self):
        return f"Pedido {self.fk_pedido_id} - Produto {self.fk_produto_id}"