from django.contrib import admin

from Usuarios.models import *

# Register your models here.
admin.site.register(Seguidores)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(UsuarioSeguidor)
admin.site.register(Like)

