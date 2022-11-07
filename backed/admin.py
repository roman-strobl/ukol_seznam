from django.contrib import admin

# Register your models here.

from .models import Movie, Features

admin.site.register(Movie)

admin.site.register(Features)