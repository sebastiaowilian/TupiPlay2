from django.forms import ModelForm
from django import forms
from .models import Jogador

class FormJogador(ModelForm):
    class Meta:
        model = Jogador        
        exclude = ['dt_inclusao', 'id_usuario_inclusao','dt_alteracao', 'id_usuario_alteracao','dt_exclusao', 'id_usuario_exclusao']
        widgets = {
            'dt_nascimento': forms.DateInput(), '_nm_senha':forms.PasswordInput(),
        }

class FormIdentificaJogador(forms.Form):
    nm_email = forms.EmailField(label='E-mail')       
    _nm_senha = forms.CharField(widget=forms.PasswordInput(), label='Senha')