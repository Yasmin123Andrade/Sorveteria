from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pessoa')
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)
    
    # Endereço incorporado na Pessoa (conforme o diagrama)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"