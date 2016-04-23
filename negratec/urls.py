from django.conf.urls import url
from negratec.apps.perfil.views import PerfilView

urlpatterns = [
    url(r'v1/perfil/?$', PerfilView.as_view()),
]
