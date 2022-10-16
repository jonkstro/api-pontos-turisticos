from rest_framework.viewsets import ModelViewSet
from .serializers import AtracaoSerializer

from atracoes.models import Atracao


class AtracoesViewSet (ModelViewSet):
    serializer_class = AtracaoSerializer
    def get_queryset(self):
        return Atracao.objects.all()