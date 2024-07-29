from django.shortcuts import render, redirect
from usuarios import forms
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def login(request):
  form = forms.LoginForms()

  if request.method == 'POST':
    form = forms.LoginForms(request.POST)

    if form.is_valid():
      nome = form['nome_login'].value()
      senha = form['password'].value()

      usuario = auth.authenticate(
        request,
        username=nome,
        password=senha,
      )

      if usuario is not None:
        auth.login(request, usuario)
        return redirect(to='index')
      else:
        return redirect(to='login')

  return render(request, 'usuarios/login.html', {'form' : form})


def cadastro(request):
  form = forms.CadastroForms()
  pass_fields = ['password_1', 'password_2']

  if request.method == 'POST':
    form = forms.CadastroForms(request.POST)
    
    if form.is_valid():
      if form['password_1'].value() != form['password_2'].value():
        return redirect(to='cadastro')
      
      nome = form['nome_cadastro'].value()
      email = form['email'].value()
      senha = form['password_1'].value()

      if User.objects.filter(username=nome).exists() or User.objects.filter(email=email).exists():
        return redirect(to='cadastro')
      
      usuario = User.objects.create_user(
        username=nome,
        email=email,
        password=senha,
      )
      usuario.save()
      return redirect(to='login')

  return render(request, 'usuarios/cadastro.html', {'form': form, 'pass_fields': pass_fields})
