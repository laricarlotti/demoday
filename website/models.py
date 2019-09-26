from django.db import models
from django.utils import timezone

class User(models.Model):
    nome_completo = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.CharField(max_length=100, verbose_name='Email')
    senha = models.CharField(default= "", max_length=100, verbose_name='Senha')

    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_completo

    
    

