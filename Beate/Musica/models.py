from django.db import models
from django.db.models.base import Model
from Usuarios.models import *

# Create your models here.

class Artista(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    artisticName = models.CharField(max_length=100)

class FormatoGeneral(models.Model):
    name = models.CharField(max_length=100)
    numLikes = models.IntegerField(default=0)
    numReproductions = models.IntegerField(default=0)

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

    def newReproduction(self):
        self.nuevaReproduccion +=1
        self.save()


class Album(FormatoGeneral):
    artist = models.ForeignKey(Artista, on_delete=models.CASCADE)
    cover = models.ImageField()
    releaseDate = models.DateField()


class Pista(FormatoGeneral):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    soundFile = models.FileField()

    def like(self):
        super().like()

        self.album.like()

    def newReproduction(self):
        super().newReproduction()

        self.album.newReproduction()


class ListaReproduccion(models.Model):
    usuarioCreador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Pista)

    def newReproduction(self):
        super().newReproduction()

    def like(self):
        super.like()

class SeguidorLista(models.Model):
    playList = models.ForeignKey(ListaReproduccion, on_delete= models.CASCADE)
    followers = models.ManyToManyField(Perfil)

    

    