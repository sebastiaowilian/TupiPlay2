from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponse

#import os
# Importação de código criados por nós
from .models import Jogador
from .forms import FormJogador, FormIdentificaJogador

#diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
#caminho_template = os.path.join(diretorio_raiz, 'templates', 'home.html')
# Definição das CBVs: Class Based Views
class JogadorCreateView(CreateView):
    model = Jogador
    fields = ["nm_jogador","nm_avatar","nm_arquivo_imagem","dt_nascimento","cd_cep","nm_email","nm_senha","dt_inclusao","id_escolaridade_id","tp_genero","id_idioma_id"]
    sucess_url = reverse_lazy("identifica_jogador")


# Create your views here.
def home(request):
    # Acessa informações da sessão
    id = request.session.get('id_jogador', 'None') #'1' #request.session['id_jogador']
    avatar = request.session.get('nm_avatar','None')
    nome = request.session.get('nm_jogador', 'None')
    genero = request.session.get('tp_genero', 'N')
    #print('From Jogadores' + context.get('nm_avatar','None'))

    #print('CONTEXT: ID = ' + str(context.get('id_jogador')) + ', Nome = ' + context.get('nm_jogador'))
    #print('CONTEXT: ID = ' + str(context['id_jogador']) + ', Nome = ' + context['nm_jogador'] + ', Avatar = ' + context['nm_avatar'] + ', Gênero = ' + context['tp_genero'])

    # Passa os valores para o contexto
    context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome, 'tp_genero' : genero}
    return render(request, 'home.html', context)

def identifica_jogador(request):
    if request.method == "GET":
        form = FormIdentificaJogador()
        return render(request, "identifica_jogador.html",{'form':form})
    elif request.method == "POST":
        form = FormIdentificaJogador(request.POST)
        if form.is_valid():  
            email = form.cleaned_data['nm_email']
            senha = form.cleaned_data['_nm_senha']    
            jogador = Jogador.objects.filter(nm_email=email,_nm_senha=senha).first()
            request.session.clear()
            if jogador:                
                request.session['id_jogador'] = jogador.id_jogador
                request.session['nm_avatar'] = jogador.nm_avatar
                request.session['nm_jogador'] = jogador.nm_jogador
                request.session['tp_genero'] = jogador.tp_genero
                context = {'id_jogador': str(jogador.id_jogador), 'nm_avatar': jogador.nm_avatar, 'nm_jogador': jogador.nm_jogador, 'tp_genero': jogador.tp_genero}
                return redirect(reverse('home'), context)
            else:
                form.add_error(None, 'Email ou senha inválidos')
                return render(request, 'identifica_jogador.html', {'form': form})
        else:
            return render(request, 'identifica_jogador.html', {'form': form})    
    

def inclui_jogador(request):
    if request.method == "GET":
        form = FormJogador()
        return render(request, 'inclui_jogador.html', {'form':form})
    elif request.method== "POST":
        form = FormJogador(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'identifica_jogador.html', {'form': form})
            return redirect(reverse('identifica_jogador'), {'form': form})
        else:
            return render(request, 'inclui_jogador.html', {'form': form})
            #return redirect(reverse('inclui_jogador'), {'form': form})
        