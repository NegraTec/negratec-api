from django.conf.urls import url, include
from negratec.apps.perfil.views import PerfilView, PerfilDestroyView

urlpatterns = [
    url(r'v1/perfil/?$', PerfilView.as_view()),
    url(r'v1/perfil/(?P<pk>[0-9]+)/$', PerfilDestroyView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
