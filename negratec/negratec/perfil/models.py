from django.db import models


class Perfil(models.Model):

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    twitter = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=20)
    outras_redes = models.CharField(max_length=100)
    lutas = models.CharField(max_length=100)
    stacks = models.CharField(max_length=100)
    eventos = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='/media', default='/media', null=True)
