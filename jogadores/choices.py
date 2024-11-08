from django.db.models import TextChoices
from django.utils.translation import gettext as _

class Choices_Tipo_Genero(TextChoices):
    MASCULINO = "M", "Masculino"
    FEMININO = "F", "Feminino"
    NAOINFORMADO = "N", "Não informado"

class Choices_Tipo_Motivacao(TextChoices):
    ACERTO = "A", "Após Acerto"
    ERRO = "E", "Após Erro"

class Choices_Tipo_Recurso(TextChoices):
    ESCRITA = "E", "Escrita"
    IMAGEM = "I", "Imagem"
    SOM = "S", "Som"    