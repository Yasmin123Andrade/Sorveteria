from django.db import models
from django.contrib.auth.models import User


class Pessoa(User):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    
    
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"