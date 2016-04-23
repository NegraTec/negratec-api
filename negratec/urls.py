from django.conf.urls import url, include
from negratec.apps.perfil.views import PerfilView

urlpatterns = [
    url(r'v1/perfil/?$', PerfilView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
