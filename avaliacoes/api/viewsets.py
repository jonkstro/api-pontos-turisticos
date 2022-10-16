from rest_framework.viewsets import ModelViewSet
from avaliacoes.api.serializers import AvaliacoesSerializer

from avaliacoes.models import Avaliacao


class AvaliacoesViewSet(ModelViewSet):
    serializer_class = AvaliacoesSerializer
    def get_queryset(self):
        return Avaliacao.objects.all()