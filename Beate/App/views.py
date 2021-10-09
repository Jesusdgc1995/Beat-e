from Musica.models import Pista,Album
from django.shortcuts import render, get_object_or_404
from django.views import View

def track_list(request):
        album = Album.objects.get()
        pistas = Pista.objects.all()
        return render(request, 'pista/lista.html', {'album': album,'pistas': pistas})

class LandingPage(View):
    templates = ['index.html']
    def get(self, request):
        return render(request, self.templates[0], {})

class RegisterPage(View):
    templates = ['signup.html']
    def get(self, request):
        return render(request, self.templates[0], {})


