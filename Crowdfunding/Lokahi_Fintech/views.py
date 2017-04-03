from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import urllib.request, json
import operator
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'static/templates/home.html')

def search(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for