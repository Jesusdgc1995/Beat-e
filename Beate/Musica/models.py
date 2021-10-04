from django.db import models
from django.db.models.base import Model
from Usuarios.models import *

# Create your models here.


class Artista(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombreArtistico = models.CharField(max_length=100)

class FormatoGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    numLikes = models.IntegerField(default=0)
    numReproducciones = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.nombre

    def like(self):
        self.numLikes +=1
        self.save()

    def disLike(self):
        self.numLikes -=1
        self.save()

    def nuevaReproduccion(self):
        self.nuevaReproduccion +=1
        self.save()


class Album(FormatoGeneral):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    caratura = models.ImageField()
    fechaLanzamiento = models.DateField()


class Pista(FormatoGeneral):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    archivoSonido = models.FileField()

    def like(self):
        super().like()

        self.album.like()

    def nuevaReproduccion(self):
        super().nuevaReproduccion()

        self.album.nuevaReproduccion()





class ListaReproduccion(models.Model):
    usuarioCreador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pistas = models.ManyToManyField(Pista)

    