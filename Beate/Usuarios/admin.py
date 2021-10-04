from django.contrib import admin

from Usuarios.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Seguidores)
admin.site.register(Post)
admin.site.register(Comentario)

