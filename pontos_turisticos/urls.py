
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from avaliacoes.api.viewsets import AvaliacoesViewSet
from comentarios.api.viewsets import ComentariosViewSet

from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecosViewSet
router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracoesViewSet, basename='Atracoes')
router.register(r'enderecos', EnderecosViewSet, basename='Enderecos')
router.register(r'avaliacoes', AvaliacoesViewSet, basename='Avaliacoes')
router.register(r'comentarios', ComentariosViewSet, basename='Comentarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
