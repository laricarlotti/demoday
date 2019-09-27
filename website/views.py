from django.shortcuts import render
from website.models import *

def index(request):
    index = User.objects.filter(ativo=True).all()
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        user = User()
        user.nome_completo = request.POST['nome_completo']
        user.email = request.POST['email']
        user.senha = request.POST['senha']
        user.save()

        args = {
            'sucesso': 'Você conseguiu campeão! Grite: Alucinação!'
        }

        return render(request, 'cadastro.html', args)

    return render(request, 'cadastro.html') 

    



