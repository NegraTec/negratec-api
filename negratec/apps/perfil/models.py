from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=20, blank=True)
    github = models.CharField(max_length=20, blank=True)
    linkedin = models.CharField(max_length=20, blank=True)
    outras_redes = models.CharField(max_length=100, blank=True)
    lutas = models.CharField(max_length=100, blank=True)
    stacks = models.CharField(max_length=100, blank=True)
    eventos = models.CharField(max_length=100, blank=True)
    imagem = models.ImageField(upload_to='negratec/media', default='negratec/media', null=True)
    usuaria = models.ForeignKey(User)
