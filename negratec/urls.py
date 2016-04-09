from django.conf.urls import patterns, include, url
from django.contrib import admin
from negratec.perfil.views import PerfilView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'v1/perfil/?$', PerfilView.as_view()),
]