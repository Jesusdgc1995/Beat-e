from django.shortcuts import render

## ^LANDING MODULE
# Start page.
def landing_page(request):
    return render(request, 'landing/landing.html', {})
    
# Terminos y condiciones.
def terms_page(request):
    return render(request, 'terms/terminos.html', {})

# Politicas.
def politicas_page(request):
    return render(request, 'terms/politicas.html', {})

## ^ACOUNT MODULE
# Register page.
def signup_page(request):
    return render(request, 'account/signup.html', {})

# Login modal.
def login_page(request):
    return render(request, 'account/login.html', {})

## ^APP MODULE
# Profile page.
def profile_page(request):    
    """
    Muestra las vista con el perfil del usuario
    """
    return render(request, 'app/profile/profile.html', {})

# Feed page.
def feed_page(request):
    """
    Muestra las vista con post de la comunidad
    """
    return render(request, 'app/feed/feed.html', {})

# playlist page.
def playlist_page(request):
    """
    Muestra las vista con las listas de reproducción de un usuario
    """
    return render(request, 'app/playlist/playlist.html', {})

# albums page.
def albums_page(request):
    """
    Muestra las vista con los albumnes de un artista
    """
    return render(request, 'app/albums/albums.html', {})

# tracks page.
def tracks_page(request):
    """
    Muestra las vista con las pistas de un album o una playlist
    """
    return render(request, 'app/tracks/tracks.html', {})
