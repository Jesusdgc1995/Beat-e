from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Seguidores)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(UsuarioSeguidor)
admin.site.register(Like)
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user','profilePhoto','name', 'lastName', 'isActive')

