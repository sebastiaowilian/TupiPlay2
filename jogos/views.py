
import random
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Frase
from jogadores.models import Jogador as tabJogador
# Create your views here.

def home(request):
    # Acessa informações da sessão

    id = request.session.get('id_jogador', 'None') #'1' #request.session['id_jogador']
    avatar =  request.session.get('nm_avatar','None')
    nome =  request.session.get('nm_jogador', 'None')
    genero = request.session.get('tp_genero', 'None')

    #print(context['id_jogador'])
    #print('ejejejeje' + context.get('id_jogador'))

    # Passa os valores para o contexto
    context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome, 'tp_genero':genero}
    return render(request, 'home.html', context)


def pega_dados_partida_quiz():
    #Pego frases
    frases_full = Frase.objects.all()
    #frases_pergunta = frases_full.order_by(Random())[:5]
    frases_pergunta = frases_full.order_by('?')[:5]
    #ids_pergunta = list(frases_pergunta.values_list('id_frase', flat=True))
    arrids_pergunta = []
    lstfrases_pergunta = []
    for item in frases_pergunta:
        arrids_pergunta.append(item.id_frase)
        dict = {'id_frase':item.id_frase, 'ds_frase_idioma_1': item.ds_frase_idioma_1, 'ds_frase_idioma_2': item.ds_frase_idioma_2}
        lstfrases_pergunta.append(dict)
    #frases_resposta = frases_full.exclude(id__in=ids_pergunta).order_by(Random())[:20]
    #frases_resposta = frases_full.exclude(id_frase__in=ids_pergunta).order_by('?')[:20]
    
    #frases_resposta = frases_full.exclude(id_frase__in=ids_pergunta).order_by('?')[:20].values('id_frase', 'ds_frase_idioma_1')
    lstfrases_resposta = []
    frases_resposta = frases_full.exclude(id_frase__in=arrids_pergunta).order_by('?')[:20].values('id_frase', 'ds_frase_idioma_2')
    for item in frases_resposta:
        dict = {'id_frase':item['id_frase'], 'ds_frase_idioma_2':item['ds_frase_idioma_2']}
        lstfrases_resposta.append(dict)      

    arrPosicaoRandomica = [random.randint(0, 4), random.randint(5, 9), random.randint(10, 14), random.randint(15, 19), random.randint(20, 24)] 
    
    #print('SEBAH')
    #print(lstfrases_resposta)
    #print (arrPosicaoRandomica)
    #print (lstfrases_pergunta)
    #print('-------------------------------')

    lstrespostas_full = []
    qtRespostas = 0
    posRespostaPergunta = 0
    posRandomica = -1

    #Complemento coleção Resposta
    for frase in frases_resposta:
        #print('Estou na posição: '+ str(qtRespostas))           
        if qtRespostas % 5 == 0 or qtRespostas == 0:
            posRandomica += 1
            posRespostaPergunta = arrPosicaoRandomica[posRandomica]
            #print('A posição da inclusão da pergunta será: ' + str(posRespostaPergunta))
        
        if qtRespostas == posRespostaPergunta:
            #print('Inclui resposta da pergunta ' + str(lstfrases_pergunta[posRandomica]['id_frase']) + ' e resposta aleatória ' + str(frase['id_frase']))
            lstrespostas_full.append(lstfrases_pergunta[posRandomica])
            lstrespostas_full.append(frase)
            qtRespostas += 2
        else:
            #print('Inclui resposta aleatória ' + str(frase['id_frase']))
            lstrespostas_full.append(frase)
            qtRespostas += 1
        
    '''
    print('Total em lstfrases_pergunta: ' + str(len(lstfrases_pergunta)))
    print('Total em lstfrases_resposta: ' + str(len(lstfrases_resposta)))
    print('Total em lstrespostas_full: ' + str(len(lstrespostas_full)))
    
    counter = 0
    for frase in lstrespostas_full:
        print('Posição ' + str(counter) + ' : ')
        print(frase)
        counter = counter + 1'''
        
    # Combino perguntas e respostas em uma coleção 
    lstPerguntasRespostas = [(lstfrases_pergunta, lstrespostas_full[i:i+5]) for i, lstfrases_pergunta in enumerate(lstfrases_pergunta)]
    return(lstPerguntasRespostas)


def jogo_quiz(request):
    id = request.session.get('id_jogador', '0')
    avatar =  request.session.get('nm_avatar','Anônimo')
    nome =  request.session.get('nm_jogador', 'Anônimo')
    genero = request.session.get('tp_genero', 'N')
    if request.method == "GET":

        lstPerguntasRespostas = pega_dados_partida_quiz()

        # Iterando sobre frases_combinadas para obter os id_frase das perguntas
        id_frases_aleatorias_5 = []
        for item_aleatorio_5, _ in lstPerguntasRespostas:
            id_frases_aleatorias_5.append(item_aleatorio_5['id_frase'])
            #print ('Sebah ' + str(item_aleatorio_5['id_frase']) +' - ' + item_aleatorio_5['ds_frase_idioma_1'] +  ' - ' + item_aleatorio_5['ds_frase_idioma_2'])
        # Imprimindo a lista de id_frase de frases_aleatorias_5
        Partida = lstPerguntasRespostas[0]
        Pergunta = Partida[0]
        Questao = Pergunta['ds_frase_idioma_1'] # Levar
        Respostas = Partida[1]
        print(Questao)
        print(str(Pergunta['id_frase']) + ' - ' + Pergunta['ds_frase_idioma_2'])        
        print(Respostas)
        
        #print('Nome da sessão '+ SESSION_COOKIE_NAME )

        #Pego jogador
        if id!=0:
            jogador = tabJogador.objects.filter(id_jogador=id).first()
            if jogador!=None:
                genero = jogador.tp_genero
                

        #Monto Context
        #context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome, 'genero': genero, 'frases': frases_full}
        #context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome, 'tp_genero': genero, 'numPartida':0, 'numQuestao':0, 'qtPontos':0, 'qtTempo':0, 'qtAcertos':0, 'qtErros':0, 'qtReplays':0, 'lstPerguntasRespostas':lstPerguntasRespostas,'Pergunta':Pergunta,'Respostas':Respostas}
        context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome, 'tp_genero': genero, 'id_qt_partida':1, 'id_num_questao':0, 'id_qt_pontos':0, 'id_qt_tempo':"00:00:00", 'id_qt_acerto':0, 'id_qt_erro':0, 'qtReplays':0, 'lstPerguntasRespostas':lstPerguntasRespostas,'Pergunta':Pergunta,'Respostas':Respostas}
        return render(request, 'jogo_quiz.html', context = context)
    elif request.method == "POST":    
        lstPerguntasRespostas = pega_dados_partida_quiz()

        # Iterando sobre frases_combinadas para obter os id_frase das perguntas
        id_frases_aleatorias_5 = []
        for item_aleatorio_5, _ in lstPerguntasRespostas:
            id_frases_aleatorias_5.append(item_aleatorio_5['id_frase'])
            #print ('Sebah ' + str(item_aleatorio_5['id_frase']) +' - ' + item_aleatorio_5['ds_frase_idioma_1'] +  ' - ' + item_aleatorio_5['ds_frase_idioma_2'])
        # Imprimindo a lista de id_frase de frases_aleatorias_5
        Partida = lstPerguntasRespostas[0]
        Pergunta = Partida[0]
        Questao = Pergunta['ds_frase_idioma_1'] # Levar
        Respostas = Partida[1]
        print(Questao)
        print(str(Pergunta['id_frase']) + ' - ' + Pergunta['ds_frase_idioma_2'])        
        print(Respostas)
        
        #print('Nome da sessão '+ SESSION_COOKIE_NAME )

        #Pego jogador
        if id!=0:
            jogador = tabJogador.objects.filter(id_jogador=id).first()
            if jogador!=None:
                genero = jogador.tp_genero

        
        print(request.POST.get('id_num_questao'))
        id_num_questao = int(request.POST.get('id_num_questao',0))
        id_qt_pontos = int(request.POST.get('id_qt_pontos',0))
        id_qt_acerto = int(request.POST.get('id_qt_acerto',0))
        id_qt_erro = int(request.POST.get('id_qt_erro',0))

        '''print(id_num_questao)
        print(id_qt_pontos)
        print(id_qt_acerto)
        print(id_qt_erro)'''


        #Monto Context
        #context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome, 'genero': genero, 'frases': frases_full}
        context = {'id_jogador': id, 'nm_avatar': avatar, 'nm_jogador': nome, 'tp_genero': genero, 'id_qt_partida':1, 'id_num_questao':id_num_questao, 'id_qt_pontos':id_qt_pontos, 'id_qt_tempo':"00:00:00", 'id_qt_acerto':id_qt_acerto, 'id_qt_erro':id_qt_erro, 'qtReplays':0, 'lstPerguntasRespostas':lstPerguntasRespostas,'Pergunta':Pergunta,'Respostas':Respostas}
    
   
        return render(request, 'jogo_quiz.html', context = context)