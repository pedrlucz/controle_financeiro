from django.shortcuts import render, redirect
from .models import Transacao, Categoria
from .forms import TransacaoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def adicionar_transacao(request):
    if request.method == 'POST':
        # se o formulário for enviado processa os dados
        form = TransacaoForm(request.POST)

        if form.is_valid():
            # salva a transação, associando ao usuário logado
            transacao = form.save(commit = False)
            transacao.usuario = request.user
            transacao.save()

            # tem que ter o nome lista_transacoes lá na urls.pys
            return redirect('lista_transacoes') # redireciona para lista de transações
        
    else:
        # se não foi enviado, exibe o formulário em branco
        form = TransacaoForm()

    # renderiza o template com o formulário
    return render(request, 'adicionar_transacao.html', {'form': form})

"""se configurar o decorador @login_required na view, o Django vai redirecionar o usuário para a página de login se ele não estiver autenticado, e depois de fazer login, ele será redirecionado para a página que estava tentando acessar (ou para uma página padrão)."""

@login_required # garante que o usuário esteja autenticado
def lista_transacoes(request):
    """Busca todas as transações do usuário e as envia para o template"""

    transacoes = Transacao.objects.filter(usuario = request.user) # filtra apenas as transações do usuário logado

    return render(request, 'controle/lista_transacoes.html', {'transacoes': transacoes})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login') #redireciona para a pagina de login após o cadastro
        
        else:
            messages.error(request, 'Erro ao criar a conta. Tente novamente.')
    
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

