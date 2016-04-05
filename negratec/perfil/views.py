from negratec.perfil.models import Perfil
from negratec.perfil.serializers import PerfilSerializer
from rest_framework.generics import ListCreateAPIView


class PerfilView(ListCreateAPIView):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()
