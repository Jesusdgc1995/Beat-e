from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Musica.views import *

router = DefaultRouter()
router.register("artistas", ArtistaAPI)
router.register("albumes", AlbumAPI)
router.register("pistas", PistaAPI)
router.register("listas", ListaReproduccionAPI)
router.register("seguidores", SeguidorListaAPI)

urlpatterns = [
    path("crud/", include(router.urls))
]
