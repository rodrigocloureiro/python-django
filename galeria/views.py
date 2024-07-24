from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  # return HttpResponse('<h1>Alura Space</h1><p>Bem-vindo ao espaço Alura!</p>')
  return render(request, 'galeria/index.html')


def imagem(request):
  return render(request, 'galeria/imagem.html')
