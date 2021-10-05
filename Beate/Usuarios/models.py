from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Usuario(models.Model):
    user = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    isAdmin = models.BooleanField(default=False)
    isActivo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user


class Perfil(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fotoPerfil = models.ImageField()
    aboutMe = models.TextField()

    def __str__(self) -> str:
        return self.user



class Seguidores(models.Model):
    seguidores = models.ManyToManyField(Usuario)
    
    @property
    def numSeguidores(self):
        return len(self.seguidores)




class UsuarioSeguidor(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    seguidores = models.ForeignKey(Seguidores, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user


class Comentario(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField(max_length=280)

    def __str__(self) -> str:
        return self.user


class Post(models.Model):
    user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=280)
    comentarios = models.ManyToManyField(Comentario)

   

class Like(models.Model):
    usuariosLike = models.ManyToManyField(Usuario)
    numLikes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)

    def like(self):
        self.numLikes += 1
        self.save()

    def disLike(self):
        self.numLikes -= 1
        self.save()
