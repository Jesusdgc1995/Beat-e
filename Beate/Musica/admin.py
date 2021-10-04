from django.contrib import admin

from Musica.models import Album, Artista, ListaReproduccion, Pista

# Register your models here.
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Pista)
admin.site.register(ListaReproduccion)
