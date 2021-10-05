from django.db.models import fields
from rest_framework import serializers

from Musica.models import *

class ArtistaSerial(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerial(serializers.ModelSerializer):
    class Meta:
        model: Album
        fields = '__all__'

class PistaSerial(serializers.ModelSerializer):
    class Meta:
        model= Pista
        fields = '__all__'

class ListaReproduccionSerial(serializers.ModelSerializer):
    class Meta:
        model = ListaReproduccion
        fields = '__all__'

class SeguidoresListaSerial(serializers.ModelSerializer):
    class Meta:
        model = SeguidorLista
        fields = '__all__'


