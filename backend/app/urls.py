from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('playlist/', views.playlist_page, name='playlist'),
    path('playlist/<int:pk>', views.tracks_page, name='playlist-track'),
    path('albums/', views.albums_page, name='albums'),
    path('albums/<int:pk>', views.tracks_page, name='album-tracks'),
]