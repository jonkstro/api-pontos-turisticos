from rest_framework import serializers

from avaliacoes.models import Avaliacao


class AvaliacoesSerializer(serializers.ModelSerializer):
    # data = serializers.DateTimeField(format = f"%d/%m/%Y %H:%M:%S")
    class Meta:
        model = Avaliacao
        fields = ('__all__')