from django.shortcuts import render

# Feed page.
def feed_page(request):
    """
    Muestra las vista con post de la comunidad
    """
    return render(request, 'app/feed/feed.html', {})


