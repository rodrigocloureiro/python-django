from django.shortcuts import render
from usuarios import forms

# Create your views here.


def login(request):
  form = forms.LoginForms()
  return render(request, 'usuarios/login.html', {'form' : form})


def cadastro(request):
  return render(request, 'usuarios/cadastro.html')
