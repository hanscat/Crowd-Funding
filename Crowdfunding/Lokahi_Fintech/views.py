from django.shortcuts import render
from . forms import UserForm
from . models import User
from django.http import HttpResponse
from django.template import loader
import urllib.request, json

# Create your views here.
def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':  # if the form has been filled

        form = UserForm(request.POST)

        if form.is_valid():  # All the data is valid
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        # creating an user object containing all the data
        user_obj = User(username=username, email=email, password=password)
        # saving all the data in the current object into the database
        user_obj.save()

        return render(request, 'signup.html', {'user_obj': user_obj,'is_registered':True }) # Redirect after POST

    else:
        form = UserForm()  # an unboundform

        return render(request, 'signup.html', {'form': form})
    
#the function executes with the showdata url to display the list of registered users
def showUsers(request):
    all_users = User.objects.all()
    return render(request, 'userdetail.html', {'all_users': all_users, })

def logout(request):
    return (request, 'logout.html')