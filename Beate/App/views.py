from django.shortcuts import render
from django.views import View

class LandingPage(View):
    templates = ['index.html']
    def get(self, request):
        return render(request, self.templates[0], {})
    
class RegisterPage(View):
    templates = ['signup.html']
    def get(self, request):
        return render(request, self.templates[0], {})