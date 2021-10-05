
from Usuarios.models import *

from rest_framework import serializers

class UsuarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["user", "nombre", "email"]


class PerfilSerial(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'


class SeguidoresSerial(serializers.ModelSerializer):
    class Meta:
        model = Seguidores
        fields = '__all__'

class UsuarioseguidorSerial(serializers.ModelSerializer):
    class Meta:
        model = UsuarioSeguidor
        fields = '__all__'


class ComentarioSerial(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class PostSerial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 

class LikeSerial(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'







