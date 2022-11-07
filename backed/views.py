from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse
from .models import Movie, Features
from .forms import FeatureForm

def index(request):
    movies = None
    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            features_api = form.cleaned_data.get('Features')
            print(f"Selected: {features_api}")
            # Vytvoření filtru s funkcí AND

            if features_api == []:
                movies = Movie.objects.all()
            else:
                movies = Movie.objects.filter(features__id = features_api[0])
                for x in range(1,len(features_api)):
                    movies = movies.filter(features__id = features_api[x]) 
                    if not movies:
                        break
    else:
        form = FeatureForm
        movies = Movie.objects.all()

    
    return render(request, 'list/main_view.html', {'form': form, "movies": movies})