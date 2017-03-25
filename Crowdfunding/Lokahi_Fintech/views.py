from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import urllib.request, json

# Create your views here.
def index(request):
    return render(request, 'static/templates/home.html')
