from django.shortcuts import render
from usuarios import forms

# Create your views here.


def login(request):
  form = forms.LoginForms()
  return render(request, 'usuarios/login.html', {'form' : form})


def cadastro(request):
  form = forms.CadastroForms()
  pass_fields = ['password_1', 'password_2']
  return render(request, 'usuarios/cadastro.html', {'form': form, 'pass_fields': pass_fields})
