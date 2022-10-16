from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=255)
    linha2 = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    pais = models.CharField(max_length=25)
    latitude = models.IntegerField(null=True, blank=True)
    lontitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1