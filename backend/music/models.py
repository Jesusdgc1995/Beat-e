from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class FormatoGeneral(models.Model):
    name = models.CharField(max_length=100)
    numLikes = models.IntegerField(default=0)
    numReproductions = models.IntegerField(default=0)
    tags = TaggableManager(blank=True)
    objects = models.Manager()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

    def like(self):
        self.numLikes +=1
        self.save()

    def disLike(self):
        self.numLikes -=1
        self.save()

    def newReproduction(self):
        self.numReproductions +=1
        self.save()


class Album(FormatoGeneral):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField()
    releaseDate = models.DateField()


class Track(FormatoGeneral):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    soundFile = models.FileField()
    releaseDate = models.DateField()

    def like(self):
        super().like()
        self.album.like()

    def newReproduction(self):
        super().newReproduction()
        self.album.newReproduction()
    class Meta:
        ordering = ('id',)


class Playlist(FormatoGeneral):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track)

    def newReproduction(self):
        super().newReproduction()

    def like(self):
        super.like()
