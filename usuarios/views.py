from django.shortcuts import render, redirect
from usuarios import forms
from django.contrib.auth.models import User
from django.contrib import auth, messages

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
        messages.success(request, f'{nome} logado com sucesso!')
        return redirect(to='index')
      else:
        messages.error(request, 'Erro ao efetuar login.')
        return redirect(to='login')

  return render(request, 'usuarios/login.html', {'form' : form})


def cadastro(request):
  form = forms.CadastroForms()
  pass_fields = ['password_1', 'password_2']

  if request.method == 'POST':
    form = forms.CadastroForms(request.POST)
    
    if form.is_valid():
      if form['password_1'].value() != form['password_2'].value():
        messages.error(request, 'Senhas não são iguais.')
        return redirect(to='cadastro')
      
      nome = form['nome_cadastro'].value()
      email = form['email'].value()
      senha = form['password_1'].value()

      if User.objects.filter(username=nome).exists() or User.objects.filter(email=email).exists():
        messages.error(request, 'Usuário com email ou nome já cadastrado.')
        return redirect(to='cadastro')
      
      usuario = User.objects.create_user(
        username=nome,
        email=email,
        password=senha,
      )
      usuario.save()
      messages.success(request, 'Cadastro realizado com sucesso!')
      return redirect(to='login')

  return render(request, 'usuarios/cadastro.html', {'form': form, 'pass_fields': pass_fields})


def logout(request):
  auth.logout(request)
  messages.success(request, 'Logout efetuado com sucesso!')
  return redirect(to='login')
