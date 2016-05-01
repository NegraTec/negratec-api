from factory import DictFactory
from factory.django import DjangoModelFactory
from negratec.apps.perfil.models import Perfil


class PerfilFactoryResource(DictFactory):
    nome = 'Roselma'
    cargo = 'Desenvolvedora'
    descricao = ''
    twitter = 'roselmamendes'
    github = 'roselmamendes'
    linkedin = 'roselmamendes'
    outras_redes = 'http://roselmamendes.github.io'
    lutas = 'feminismo negro'
    stacks = 'java, python'
    eventos = 'PyLadies'
    imagem = None
    usuaria = None


class PerfilFactory(DjangoModelFactory):
    class Meta:
        model = Perfil

    nome = 'Roselma'
    cargo = 'Desenvolvedora'
