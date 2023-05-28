from django.shortcuts import render
from locadora.models import Locacao, Filme

# Create your views here.

def index(request):
    context = {
        'sistema': 'Locadora',
        'aluno': 'João Pedro'
    }
    return render(request, 'main/index.html', context)

def lista_locacao(request):
    # Lógica para obter todas as locações do banco de dados
    locacoes = Locacao.objects.all()
    context = {
        'locacoes': locacoes
    }
    return render(request, 'main/locacao.html', context)

def lista_filmes(request):
    # Lógica para obter todos os filmes do banco de dados
    filmes = Filme.objects.all()
    context = {
        'filmes': filmes
    }
    return render(request, 'main/filmes.html', context)
