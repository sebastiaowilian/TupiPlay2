from django.db import models
from django.utils import timezone
from jogadores import models as appJogadores
#from jogadores.choices import Choices_Tipo_Motivacao, Choices_Tipo_Recurso


class Tipo_Motivacao(models.Model):
    tp_motivacao = models.CharField(max_length=1, primary_key=True, verbose_name='Sigla Motivação')
    nm_motivacao = models.CharField(max_length=50, verbose_name='Motivação')
    
    def __str__(self) -> str:
        return self.nm_motivacao
    

class Tipo_Recurso(models.Model):
    tp_recurso = models.CharField(max_length=1, primary_key=True, verbose_name='Sigla Recurso')
    nm_recurso = models.CharField(max_length=30, verbose_name='Motivação')
    
    def __str__(self) -> str:
        return self.recurso
    

class Nivel_Jogador(models.Model):
    id_nivel_jogador = models.AutoField(primary_key=True, default=0, verbose_name='Id nível jogador')
    nm_nivel_jogador = models.CharField(max_length=30, unique=True, verbose_name='Nome nível jogador')
    ds_nivel_jogador = models.CharField(max_length=100, null=True, verbose_name='Descrição nível jogador')
    vl_nivel_jogador = models.IntegerField(default=0, null=True, verbose_name='Valor nível jogador')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.nm_nivel_jogador


class Nivel_Dificuldade(models.Model):
    id_nivel_dificuldade = models.AutoField(primary_key=True, default=0, verbose_name='Id nível dificuldade')
    nm_nivel_dificuldade = models.CharField(max_length=30, unique=True, verbose_name='Nome nível dificuldade')
    ds_nivel_dificuldade = models.CharField(max_length=100, null=True, verbose_name='Descrição dificuldade')
    vl_nivel_dificuldade = models.IntegerField(default=0, null=True, verbose_name='Valor nível dificuldade')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.nm_nivel_dificuldade


class Motivacional(models.Model):
    id_motivacao = models.AutoField(primary_key=True, default=0, verbose_name='Id Idioma')
    id_idioma = models.ForeignKey(appJogadores.Idioma, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Idioma')    
    msg_motivacional = models.CharField(max_length=30, unique=True, verbose_name='Mensagem motivacional')
    tp_motivacional = models.ForeignKey(Tipo_Motivacao, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Tipo motivação')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.msg_motivacional


class Jogo(models.Model):
    id_jogo = models.AutoField(primary_key=True, default=0, verbose_name='ID jogo')
    nm_jogo = models.CharField(max_length=30, unique=True, verbose_name='Nome jogo')
    ds_jogo = models.CharField(max_length=100, null=True, verbose_name='Descrição jogo')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.nm_jogo


class Frase(models.Model):
    id_frase = models.AutoField(primary_key=True, default=0, verbose_name='Id frase')
    id_idioma_1 = models.ForeignKey(appJogadores.Idioma, related_name='frases_idioma_1', on_delete=models.SET_DEFAULT, default=1, null=True, verbose_name='Idioma nativo')    
    id_idioma_2 = models.ForeignKey(appJogadores.Idioma, related_name='frases_idioma_2', on_delete=models.SET_DEFAULT, default=2, null=True, verbose_name='Idioma aprendizado')    
    ds_frase_idioma_1 = models.CharField(max_length=250, unique=True, verbose_name='Frase idioma nativo')
    ds_frase_idioma_2 = models.CharField(max_length=250, verbose_name='Frase idioma aprendizado' )
    ds_frase_idioma_2_observacao = models.CharField(max_length=100, null=True, verbose_name='Observações' )
    nm_arquivo_imagem = models.CharField(max_length=100, null=True, verbose_name='Nome arquivo de imagem')
    nm_arquivo_som = models.CharField(max_length=50, null=True, verbose_name='Nome arquivo de som')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.ds_frase_idioma_1
    

class Verbete(models.Model):
    id_verbete = models.AutoField(primary_key=True, default=0, verbose_name='Id verbete')
    id_idioma_1 = models.ForeignKey(appJogadores.Idioma, related_name='verbete_idioma_1', on_delete=models.SET_DEFAULT, default=1, null=True, verbose_name='Idioma nativo')    
    id_idioma_2 = models.ForeignKey(appJogadores.Idioma, related_name='verbete_idioma_2', on_delete=models.SET_DEFAULT, default=2, null=True, verbose_name='Idioma aprendizado')    
    nm_verbete_idioma_2 = models.CharField(max_length=100, unique=True, verbose_name='Verbete idioma aprendizado')
    ds_verbete_idioma_1 = models.CharField(max_length=250, verbose_name='Definição verbete idioma nativo' )
    ds_verbete_idioma_1_observacao = models.CharField(max_length=100, null=True, verbose_name='Observações' )
    nm_arquivo_imagem = models.CharField(max_length=50, null=True, verbose_name='Nome arquivo de imagem')
    nm_arquivo_som = models.CharField(max_length=50, null=True, verbose_name='Nome arquivo de som')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.nm_verbete_idioma_2


class Partida(models.Model):
    id_partida = models.AutoField(primary_key=True, default=0, verbose_name='Id partida')
    id_idioma_1 = models.ForeignKey(appJogadores.Idioma, related_name='partida_idioma_1', on_delete=models.SET_DEFAULT, default=1, null=True, verbose_name='Idioma nativo')    
    id_idioma_2 = models.ForeignKey(appJogadores.Idioma, related_name='partida_idioma_2', on_delete=models.SET_DEFAULT, default=2, null=True, verbose_name='Idioma aprendizado')    
    id_jogo = models.ForeignKey(Jogo, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Jogo escolhido')    
    id_jogador = models.ForeignKey(appJogadores.Jogador, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Jogador(a)')
    tp_recurso = models.ForeignKey(Tipo_Recurso, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Tipo recurso')
    qt_pontos = models.IntegerField(default=0, verbose_name='Pontuação')
    qt_acerto = models.IntegerField(default=0, verbose_name='Acertos')
    qt_erro = models.IntegerField(default=0, verbose_name='Erros')
    qt_continuar = models.IntegerField(default=0, verbose_name='Continuações')
    dt_inicio_partida = models.DateTimeField(blank=True, null=True, verbose_name='Início') #Pode receber None= models.IntegerField(default=0, verbose_name='')
    qt_duracao_minutos = models.IntegerField(default=0, verbose_name='Duração')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.id_partida + ' ' + self.id_idioma_2 + ' ' + self.id_jogo  


class Partidas_Resumo(models.Model):
    id_partida_resumo = models.AutoField(primary_key=True, default=0, verbose_name='Id partidas resumo')
    id_idioma_1 = models.ForeignKey(appJogadores.Idioma, related_name='partidas_resumo_idioma_1', on_delete=models.SET_DEFAULT, default=1, null=True, verbose_name='Idioma nativo')    
    id_idioma_2 = models.ForeignKey(appJogadores.Idioma, related_name='partidas_idioma_2', on_delete=models.SET_DEFAULT, default=2, null=True, verbose_name='Idioma aprendizado')    
    id_jogo = models.ForeignKey(Jogo, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Jogo escolhido')    
    id_jogador = models.ForeignKey(appJogadores.Jogador, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Jogador(a)')
    qt_pontos = models.IntegerField(default=0, verbose_name='Pontuação')
    qt_acerto = models.IntegerField(default=0, verbose_name='Acertos')
    qt_erro = models.IntegerField(default=0, verbose_name='Erros')
    qt_continuar = models.IntegerField(default=0, verbose_name='Continuações')    
    qt_duracao_minutos = models.IntegerField(default=0, verbose_name='Duração')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inclusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.id_partida + ' ' + self.id_idioma_2 + ' ' + self.id_jogo  
