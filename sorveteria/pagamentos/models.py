from django.db import models





class Pagamento(models.Model):
    pedido = models.ForeignKey('pedidos.Pedidos', on_delete=models.CASCADE, related_name='pagamentos')
    forma_pagamento = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pagamento R$ {self.valor_total} ({self.forma_pagamento}) - Pedido #{self.pedido.id}"