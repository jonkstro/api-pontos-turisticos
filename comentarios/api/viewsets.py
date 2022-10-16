from rest_framework.viewsets import ModelViewSet
from comentarios.api.serializers import ComentariosSerializer

from comentarios.models import Comentario


class ComentariosViewSet(ModelViewSet):
    serializer_class = ComentariosSerializer
    def get_queryset(self):
        return Comentario.objects.all()