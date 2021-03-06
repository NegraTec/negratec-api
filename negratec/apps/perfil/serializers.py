from negratec.apps.perfil.models import Perfil
from rest_framework import serializers


import base64

from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super(Base64ImageField, self).to_internal_value(data)


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil

    imagem = Base64ImageField(
        max_length=None, use_url=True,
    )
