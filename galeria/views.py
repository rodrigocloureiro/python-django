from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Fotografia

# Create your views here.

def index(request):
  # return HttpResponse('<h1>Alura Space</h1><p>Bem-vindo ao espaço Alura!</p>')
  fotografias = Fotografia.objects.all()
  return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request):
  return render(request, 'galeria/imagem.html')
