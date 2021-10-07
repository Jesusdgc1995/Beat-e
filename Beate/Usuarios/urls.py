from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from Usuarios.views import *

router = DefaultRouter()
router.register("usuarios", UsuarioAPI)
router.register("perfiles", PerfilAPI)
router.register("seguidores", SeguidoresAPI)
router.register("usuarios_seguidores", UsuarioSeguidorAPI)
router.register("comentarios", ComentarioAPI)
router.register("posts", PostAPI)
router.register("likes", LikeAPI)


urlpatterns = [
    path("crud/", include(router.urls)),
    path("register", RegistrarAPI.as_view()),
    path("logout", LogOut.as_view()),
    path("login", LogIn.as_view()),
]