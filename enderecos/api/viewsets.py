from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecosSerializer

from enderecos.models import Endereco

class EnderecosViewSet(ModelViewSet):
    serializer_class = EnderecosSerializer
    def get_queryset(self):
        return Endereco.objects.all()