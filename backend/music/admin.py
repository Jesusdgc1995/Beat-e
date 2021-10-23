from django.contrib import admin
from .models import Album, Track, Genre, Playlist


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist')


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'genre')


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', )


admin.site.register(Genre)
