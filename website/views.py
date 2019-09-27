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

        return render(request, 'index.html', args)

    return render(request, 'index.html') 

def index(request):
    return render(request, 'index.html')
    

    # login_email = User.email.filter(id=id).first()
    # login_senha = User.senha.filter(id=id).first()
    # if login_email and login_senha is not None:
    #     login_email.ativo and login_senha.ativo = False
    #     login_email.save() and login_senha.save()
    #     return redirect('login.html' + login_email.id and login_senha.id)
    # return render(request, 'index.html')
    

    # login.email = User.objects.get(User.objects.filter(email=''))
    # login.senha = User.objects.get(User.objects.filter(senha=''))

    # if (login.email = True and login.senha = True) 
    #  return render(request, 'login.html')

    #  else return render(request, 'cadastro.html')

    



