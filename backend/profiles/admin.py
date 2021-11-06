from django.contrib import admin

from .models import ArtistProfile, UserProfile

# Register your models here.
admin.site.register(ArtistProfile)
admin.site.register(UserProfile)