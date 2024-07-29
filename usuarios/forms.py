from django import forms

class LoginForms(forms.Form):
  nome_login = forms.CharField(
    label='Nome de Login',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Ex.: João Silva',
      }
    )
  )
  password = forms.CharField(
    label='Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha',
      }
    ),
  )


class CadastroForms(forms.Form):
  nome_cadastro = forms.CharField(
    label='Nome de Cadastro',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Ex.: João Silva',
      }
    ),
  )
  email = forms.EmailField(
    label='E-mail',
    required=True,
    max_length=100,
    widget=forms.EmailInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'joaosilva@xpto.com',
      }
    ),
  )
  password_1 = forms.CharField(
    label='Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha',
      }
    ),
  )
  password_2 = forms.CharField(
    label='Confirme sua senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha novamente',
      }
    ),
  )

  def clean_nome_cadastro(self):
    nome = self.cleaned_data.get('nome_cadastro')

    if nome:
      nome = nome.strip()
      if ' ' in nome:
        raise forms.ValidationError('Espaços não são permitidos no campo Nome de Cadastro.')
      else:
        return nome
      
  def clean_password_2(self):
    password_1 = self.cleaned_data.get('password_1')
    password_2 = self.cleaned_data.get('password_2')

    if password_1 and password_2:
      if password_1 != password_2:
        raise forms.ValidationError('As senhas não são iguais')
      else:
        return password_2
