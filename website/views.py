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
            'sucesso': 'Cadastro efetuado com sucesso.'
        }

        return render(request, 'cadastro.html')

    return render(request, 'cadastro.html') 

def login(request):
    if request.method == 'POST':
        formulario_email = request.POST['email']
        formulario_senha = request.POST['senha']

        user_logado = User.objects.filter(email = formulario_email,
                                          senha = formulario_senha).first()

        if user_logado is not None:
            args = {
                'dados': user_logado
            }
            return render(request, 'index.html', args)
        else:
            args = {
                'msg': 'Credenciais inválidas. Tente novamente.'
            }
            return render(request, 'login.html', args)

    return render(request, 'login.html')

    
def produtos(request):
    return render(request, 'produtos.html')

def menu(request):
    return render(request, 'menu.html')

def index(request):
    return render(request, 'index.html')


