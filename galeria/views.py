from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

dados = {
  1: {'nome': 'Nebulosa de Carina', 'legenda': 'webbtelescope.org / NASA / James Webb'},
  2: {'nome': 'Galáxia NGC 1079', 'legenda': 'nasa.org / NASA / Hubble'},
}

def index(request):
  # return HttpResponse('<h1>Alura Space</h1><p>Bem-vindo ao espaço Alura!</p>')
  return render(request, 'galeria/index.html', {'cards': dados})


def imagem(request):
  return render(request, 'galeria/imagem.html')
