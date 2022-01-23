from enum import unique
from django.db import models
from datetime import datetime

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True, error_messages={"unique": "Email já cadastrado"})
    senha = models.CharField(max_length=16)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=16, unique=True, error_messages={"unique":"Telefone já cadastrado"})
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)
    pais = models.CharField(max_length=150)
    CEP = models.CharField(max_length=9)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    A_CONFIRMAR = 'AC'
    CONFIRMARDO = 'C'
    FINALIZADO = 'F'
    STATUS_AGENDAMENTO_CHOICES = [
        (A_CONFIRMAR, 'A confirmar'),
        (CONFIRMARDO, 'Confirmado'),
        (FINALIZADO, 'Finalizado')
    ]
    status_agendamento = models.CharField(max_length=2, choices=STATUS_AGENDAMENTO_CHOICES, default=A_CONFIRMAR)
    data = models.DateTimeField(default=datetime.now, blank=True)
    descricao = models.TextField()
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
