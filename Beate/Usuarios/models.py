from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model

# Create your models here.

class Perfil(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    # isAdmin = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    profilePhoto = models.ImageField(blank=True, null=True)
    aboutMe = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.email


class Seguidores(models.Model):
    followers = models.ManyToManyField(Perfil)
    
    @property
    def numFollowers(self):
        return len(self.followers)


class UsuarioSeguidor(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    followers = models.ForeignKey(Seguidores, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user


class Post(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=280)
    # comentarios = models.ManyToManyField(Comentario)
    # Hay un error en la lógica, lo correcto es que un comentario pertenezca a un post, así varios comentarios pueden pertenecer a uno pero no se especifica como ManyToMany
    
    def __str__(self) -> str:
        return f"{self.user.user} - {self.date}"


class Comentario(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)

    def __str__(self) -> str:
        return self.user


class Like(models.Model):
    userersLike = models.ManyToManyField(Perfil)
    numLikes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)

    def like(self):
        self.numLikes += 1
        self.save()

    def disLike(self):
        self.numLikes -= 1
        self.save()
