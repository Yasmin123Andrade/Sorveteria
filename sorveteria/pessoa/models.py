from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    # Relacionamento 1:1 com o User do Django (herança/associação com django.contrib.auth)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pessoa')
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def _str_(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Endereco(models.Model):
    # Relacionamento 1:1 com Pessoa
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='endereco', primary_key=True)
    cidade = models.CharField(max_length=100)
    numero = models.IntegerField()
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"


class Pedido(models.Model):
    # Relacionamento 1:N com Pessoa (Uma Pessoa faz vários Pedidos)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='pedidos')
    data_pedido = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    forma_pagamento = models.CharField(max_length=50)

    # Relacionamento N:N com Produto através da tabela intermediária PedidoProduto
    produtos = models.ManyToManyField('Produto', through='PedidoProduto', related_name='pedidos')

    def _str_(self):
        return f"Pedido #{self.id} - {self.pessoa.nome}"


class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.descricao} - R$ {self.valor:.2f}"


class PedidoProduto(models.Model):
    """
    Tabela Intermediária (N:N) entre Pedido e Produto com atributos adicionais.
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='pedidos_item')
    quantidade_produto = models.IntegerField(default=1)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.quantidade_produto}x {self.produto.descricao} (Pedido #{self.pedido.id})"