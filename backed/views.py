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
            filters = Q()
            features = form.cleaned_data.get('Features')
            print(f"Selected: {features}")
            for feature in features:
                filters &= Q(features__in=feature)
            
            if features == []:
                movies = Movie.objects.all()
            else:           
                movies = Movie.objects.filter(filters)
            

    else:
        form = FeatureForm
        movies = Movie.objects.all()

    #return render_to_response('render_country.html', {'form': form},
    #                          context_instance=RequestContext(request))

    
    return render(request, 'list/main_view.html', {'form': form, "movies": movies})