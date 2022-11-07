from django import forms

from .models import Features

class FeatureForm(forms.Form):
    
    Features_db = Features.objects.all()

    OPTIONS = list()

    for feature in Features_db:
        #vytvoření listu pro Formulář (<ID>, jméno)
        _, name = feature.name.split("_",1)
        OPTIONS.append((feature.id,name))

    print(OPTIONS)

    Features = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS,required=False)
