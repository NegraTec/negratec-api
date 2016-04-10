from django.conf.urls import url
from negratec.perfil.views import PerfilView

urlpatterns = [
    url(r'v1/perfil/?$', PerfilView.as_view()),
]
