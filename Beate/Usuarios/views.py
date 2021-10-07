# APIS CRUD
from django.shortcuts import render
from Usuarios.serializers import *
from rest_framework import viewsets, authentication, permissions
from Usuarios.models import *
from Usuarios.permissions import AccesoPersonal

# API para manupulación de usuario (login, registro de usuario, logout)
from rest_framework import views
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
class RegistrarAPI(views.APIView):
    def post(self, request):
        user = UsuarioSerial(data=request.data)
        if user.is_valid():
            user.save()
            return Response({"Bienvenido":True})
        return Response(usuario.errors, HTTP_400_BAD_REQUEST)
    pass

class LogIn(views.APIView):
    def post(self, request):
        user = authenticate(request, username=request.data["username"], password=request.data["password"])
        
        if not user is None:
            login(request, user)
            return Response({"Login Exitoso":True})
        return Response({"Login Exitoso":False})
            
class LogOut(views.APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPersonal)
    
    def get(self, request):
        user = request.user.username
        logout(request)
        return Response (f"{user} ha cerrado sesión.")


class UsuarioAPI(viewsets.ModelViewSet):
    serializer_class = UsuarioSerial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPersonal)
    queryset = get_user_model().objects.all()
    

class PerfilAPI(viewsets.ModelViewSet):
    serializer_class = PerfilSerial
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated, AccesoPersonal)
    queryset = Perfil.objects.all()
    
class SeguidoresAPI(viewsets.ModelViewSet):
    serializer_class = SeguidoresSerial
    queryset = Seguidores.objects.all()
    
class UsuarioSeguidorAPI(viewsets.ModelViewSet):
    serializer_class = UsuarioseguidorSerial
    queryset = UsuarioSeguidor.objects.all()

class ComentarioAPI(viewsets.ModelViewSet):
    serializer_class = ComentarioSerial
    queryset = Comentario.objects.all()

class PostAPI(viewsets.ModelViewSet):
    serializer_class = PostSerial
    queryset = Post.objects.all()
    
class LikeAPI(viewsets.ModelViewSet):
    serializer_class = LikeSerial
    queryset = Like.objects.all()