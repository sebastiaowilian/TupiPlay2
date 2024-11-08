from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from email.policy import default
from django.utils import timezone

# Create your models here.
class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True, default=0, verbose_name='ID idioma')
    nm_idioma = models.CharField(max_length=30,unique=True, verbose_name='Nome idioma')
    ds_idioma = models.CharField(max_length=150, null=True, verbose_name='Descrição idioma')
    nm_arquivo_imagem = models.CharField(max_length=50, null=True, verbose_name='Nome arquivo imagem')
    nm_arquivo_estilo_css = models.CharField(max_length=50, null=True, verbose_name='Nome arquivo estilo CSS')
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inlusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.nm_idioma


class Escolaridade(models.Model):
    id_escolaridade = models.AutoField(primary_key=True, default=0)
    nm_escolaridade = models.CharField(max_length=30, unique=True)
    ds_escolaridade = models.CharField(max_length=200, null=True)
    vl_escolaridade = models.IntegerField(default=0, null=True)
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inlusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.nm_escolaridade
    

class Tipo_Genero(models.Model):
    tp_genero = models.CharField(max_length=1, primary_key=True, verbose_name='Sigla Gênero')
    nm_genero = models.CharField(max_length=30, verbose_name='Gênero')
    
    def __str__(self) -> str:
        return self.nm_genero


class Jogador(models.Model):    
    id_jogador = models.AutoField(primary_key=True, verbose_name='Id jogador(a)')
    id_escolaridade = models.ForeignKey(Escolaridade, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Escolaridade')
    id_idioma = models.ForeignKey(Idioma, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Idioma')
    tp_genero = models.ForeignKey(Tipo_Genero, on_delete=models.SET_DEFAULT, default=0, null=True, verbose_name='Tipo gênero') 

    nm_jogador = models.CharField(max_length=80, verbose_name='Nome Jogador(a)')
    nm_avatar = models.CharField(max_length=20,unique=True, verbose_name='Nome Avatar')
    nm_arquivo_imagem = models.CharField(max_length=50, verbose_name='Nome Arquivo Imagem', null=True)
    dt_nascimento = models.DateField(null=True, verbose_name='Data Nascimento')    
    cd_cep = models.CharField(max_length=8, null=True, verbose_name='CEP')
    nm_email= models.EmailField(max_length=50,unique=True, verbose_name='E-mail')
    _nm_senha= models.CharField(max_length=20,db_column='nm_senha', null=True,verbose_name='Senha')
    
    dt_inclusao = models.DateTimeField(auto_now_add=True, verbose_name='Data inlusão')
    id_usuario_inclusao = models.IntegerField(default=0, verbose_name='Usuário inclusao')
    dt_alteracao = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Data alteração') #Pode receber None
    id_usuario_alteracao = models.IntegerField(default=0, null=True, verbose_name='Usuário alteração')
    dt_exclusao = models.DateTimeField(blank=True, null=True, verbose_name='Data exclusão') #Pode receber None
    id_usuario_exclusao = models.IntegerField(default=0, null=True, verbose_name='Usuário exclusão')

    def __str__(self) -> str:
        return self.nm_avatar

    @property
    def nm_senha(self):            
            return self._nm_senha

    @nm_senha.setter
    def nm_senha(self, value):
            #TODO: verificar se é um insert ou não
            print (value)
            if len(value) > 12:
                self._nm_senha = make_password(password=value, salt=None, hasher='pbkdf2_sha256')
            else:
                self._nm_senha = self._nm_senha 

    #TODO:Como salvar a senha encriptada sem reencriptar 2 X
    '''def identifica_jogador(email, senha_informada):   
        #TODO: Buscar jogador no banco de dados             
        jogador = Jogador # nm_email=email; nm_seha = CSenha
        if jogador:
            corresponde = check_password(password=senha_informada, encoded=jogador.nm_senha)
            if corresponde:
                return True
            else:
                return False
        else:
            return False   


    def save(self, *args, **kwargs):
        if not self.protocole:
            self.protocole = datetime.now().strftime("%d/%m/%Y-%H:%M:%S-") + token_hex(16)

        if not self.identificador:
            self.identificador = token_urlsafe(16)

        super(Jogador, self).save(*args, **kwargs)'''

