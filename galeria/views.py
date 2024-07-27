from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia

# Create your views here.

def index(request):
  # return HttpResponse('<h1>Alura Space</h1><p>Bem-vindo ao espaço Alura!</p>')
  # fotografias = Fotografia.objects.all()
  fotografias = Fotografia.objects.filter(publicada=True)
  return render(request, 'galeria/index.html', {'cards': fotografias})


def imagem(request, foto_id):
  fotografia = get_object_or_404(Fotografia, pk=foto_id)
  return render(request, 'galeria/imagem.html', {'fotografia': fotografia})
