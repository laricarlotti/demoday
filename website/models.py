from django.db import models
from django.utils import timezone

class User(models.Model):
    nome = models.CharField(default='', max_length=100, verbose_name='Nome')
    email = models.CharField(max_length=100, verbose_name='Email', unique=True)
    senha = models.CharField(default= '', max_length=100, verbose_name='Senha')

    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

    
    

