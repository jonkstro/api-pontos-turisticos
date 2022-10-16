from rest_framework import serializers

from comentarios.models import Comentario


class ComentariosSerializer(serializers.ModelSerializer):
    # data = serializers.DateTimeField(format = f"%d/%m/%Y %H:%M:%S")
    class Meta:
        model = Comentario
        fields = ('__all__')