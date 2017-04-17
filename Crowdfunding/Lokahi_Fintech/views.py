from django.shortcuts import render
from . forms import UserForm
from . models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.template import loader
import urllib.request, json
import operator
from django.db.models import Q


# Create your views here.
def index(request):
    all_users = User.objects.all()
    return render(request, 'home.html', )

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
    #return (request, 'logout.html')
    if not request.user.is_authenticated:
        return render(request, 'home.html')
    all_users = User.objects.all()
    return render(request, 'home.html', )


def login_page(request):
    return render(request, 'login.html')

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'home.html')
    else:
        # Return an 'invalid login' error message.
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
            return render(request, 'signup.html', {'user_obj': user_obj, 'is_registered': True})  # Redirect after POST
    else:
        form = UserForm()  # an unboundform

        return render(request, 'signup.html', {'form': form})


# the function executes with the showdata url to display the list of registered users
def showUsers(request):
    all_users = User.objects.all()
    return render(request, 'userdetail.html', {'all_users': all_users, })


@login_required
def logout(request):
    # do something to log out
    logout(request)
    return (request, 'logout.html')