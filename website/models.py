from django.db import models
from django.utils import timezone

class Login(models.Model):
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=100, verbose_name='Email')
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome')
    usuario = models.CharField(max_length=100, verbose_name='Nome de Usuário')

    def __str__(self):
        return self.nome

    
    

