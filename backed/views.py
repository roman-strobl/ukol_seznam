from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Movie, Features

def index(request):
    movies = Movie.objects.all()
    return render(request, 'list/main_view.html', {"movies": movies})