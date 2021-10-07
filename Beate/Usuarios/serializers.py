
from Usuarios.models import *
from rest_framework import serializers

class UsuarioSerial(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]
        extra_kwargs = {
            "password":{"write_only":True, "style":{"input_type":"password"}},
            "email":{"write_only":True}
        }

class PerfilSerial(serializers.HyperlinkedModelSerializer):
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







