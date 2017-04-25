from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login, get_user
from django.shortcuts import render_to_response
from django.http import HttpRequest
from django.template import RequestContext

from django.views.generic.edit import CreateView

from django.views.generic import UpdateView

from django.views.generic import ListView
import django
django.setup()




# Create your views here.
def index(request):
    return render(request, 'home.html')

def login_page(request):
    form = UserForm(request.POST or None)
    return render(request, 'login.html', {"form":form})

def my_login(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html', {"user":user, "logedin" : True})
            # Redirect to a success page.
            return render(request, 'login.html', {"message":"Disabled account!", "form":form})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {"message":"invalid token!", "form":form})
    else:
        return render(request, "login.html", {"form":form})

def signup(request):
    # if request.method == 'POST':  # if the form has been filled

    form = UserForm(request.POST or None)
    profile = Profile_Form(request.POST or None)

    if form.is_valid() and not profile.is_valid():  # All the data is valid
        user = form.save(), 'signup.html', {'user_obj': user_obj, 'is_registered': True})  # Redirect after POST
    # else:
    #     form = UserForm()  # an u
        
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        # user.set_email(email)
        password = request.POST.get('password', '')
        user.set_password(password)
        # profile = profile.save(commit=False)
        
        # # creating an user object containing all the data
        # user_obj = User(username=username, email=email, password=password)
        # # saving all the data in the current object into the database
        # user_obj.save()
        
        # profile.user = user
        # profile.save()
        user.save()
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/Lokahi")
            
    return render(request,"signup.html", {"form":form, "profileForm": profile,'is_registered': False})
            # return render(requesnboundform
    #     return render(request, 'signup.html', {'form': form})


@login_required
def my_logout(request):
    # do something to log out
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'login.html', {"form": form})


# the testing function executes with the showdata url to display the list of registered users
def showUsers(request):
    all_users = User.objects.all()
    return render(request, 'userdetail.html', {'all_users': all_users})

def showReports(request):
    all_reports = Report.objects.all()
    return render(request, 'showreports.html', {'all_reports': all_reports})

def showGroups(request):
    all_groups = Group.objects.all()
    return render(request, 'showgroups.html', {'all_groups': all_groups})

class MakeGroup(CreateView):
    model = Group
    fields = ["title", "owner", "participants"]
    success_url =  '/Lokahi/GroupList/'
    template_name = "addgroup.html"

class GroupList(ListView):
    model = Group
    template_name = "grouplist.html"

class addMember(UpdateView):
    model = Group
    fields = ["participants"]
    template_name = "addgroup.html"

def suspendUser(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = User.objects.get(username=search_id)
            user.is_active=False
            user.save()
            return render(request, 'home.html')
        except User.DoesNotExist:
            return HttpResponse("no user by that username")
    else:
        return render(request, 'home.html')

def activateUser(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = User.objects.get(username=search_id)
            user.is_active=True
            user.save()
            return render(request, 'home.html')
        except User.DoesNotExist:
            return HttpResponse("no user by that username")
    else:
        return render(request, 'home.html')

def deleteFromGroup(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            g = User.groups.filter(username=search_id)
            return render(request, 'home.html')
        except User.DoesNotExist:
            return HttpResponse("no user by that username")
    else:
        return render(request, 'home.html')

def makeManager(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = User.objects.get(username=search_id)
            user.is_superuser = True
            user.save()
            return render(request, 'home.html')
        except User.DoesNotExist:
            return HttpResponse("no user by that username")
    else:
        return render(request, 'home.html')