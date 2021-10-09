from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Artista)
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('cover','name', 'artist')
@admin.register(Pista)
class PistaAdmin(admin.ModelAdmin):
    list_display = ('id','name','album','gender','soundFile')
admin.site.register(ListaReproduccion)
admin.site.register(SeguidorLista)
admin.site.register(Genero)
