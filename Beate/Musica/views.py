# Creación de las APIS CRUD
from django.shortcuts import render
from Musica.serializers import *
from rest_framework import viewsets, authentication, permissions
from Musica.models import *

class ArtistaAPI(viewsets.ModelViewSet):
    serializer_class = ArtistaSerial
    queryset = Artista.objects.all()   

class AlbumAPI(viewsets.ModelViewSet):
    serializer_class = AlbumSerial
    queryset = Album.objects.all()
    
class PistaAPI(viewsets.ModelViewSet):
    serializer_class = PistaSerial
    queryset = Pista.objects.all()

class ListaReproduccionAPI(viewsets.ModelViewSet):
    serializer_class = ListaReproduccionSerial
    queryset = ListaReproduccion.objects.all()

class SeguidorListaAPI(viewsets.ModelViewSet):
    serializer_class = SeguidorLista
    queryset = SeguidorLista.objects.all()