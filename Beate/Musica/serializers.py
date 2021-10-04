from django.db.models import fields
from rest_framework import serializers

from Musica.models import *

class ArtistaSerial(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerial(serializers.ModelSerializer):
    class Meta:
        models: Album
        fields = '__all__'

class PistaSerial(serializers.ModelSerializer):
    class Meta:
        models= Pista
        fields = '__all__'

class ListaReproduccionSerial(serializers.ModelSerializer):
    class Meta:
        models = ListaReproduccion
        fields = '__all__'

