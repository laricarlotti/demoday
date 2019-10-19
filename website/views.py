from django.shortcuts import render, redirect
from website.models import *

def cadastro(request):
    if request.method == 'POST':
        user = User()
        user.nome = request.POST['nome']
        user.email = request.POST['email']

        # Aqui cria o algoritmo de criptografia 
        user.senha = request.POST['senha']
        user.save()

        args = {
            'sucesso': 'Você conseguiu campeão! Grite: Alucinação!'
        }

        return render(request, 'cadastro.html', args)

    return render(request, 'cadastro.html') 

def index(request):
    if request.method == 'POST':
        formulario_email = request.POST['email']
        formulario_senha = request.POST['senha']

        user_logado = User.objects.filter(email = formulario_email,
                                          senha = formulario_senha).first()

        if user_logado is not None:
            args = {
                'dados': user_logado
            }
            #return render(request, 'produtos.html', args)
            return render(request, 'index.html', args)
        else:
            args = {
                'msg': 'credenciais invalidas'
            }
            return render(request, 'index.html', args)

    return render(request, 'index.html')

    
def produtos(request):
    return render(request, 'produtos.html')

def menu(request):
    return render(request, 'menu.html')


