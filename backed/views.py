from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .task import main

def index(request):
    main()
    return HttpResponse("Hello, world. You're at the polls index.")