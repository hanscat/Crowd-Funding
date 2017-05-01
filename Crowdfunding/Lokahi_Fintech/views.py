from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login, get_user
from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DeleteView
from django.views.generic import ListView
from Crypto.PublicKey import RSA
from Crypto import Random
from ast import literal_eval as make_tuple

from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.db.models import Q


# helper functions for encryption & decryptions
def secret_string(msg, public_key):
    """takes in a string and a public key, encrypts the string with said
key, then returns the resulting string"""
    cipher_text = public_key.encrypt(msg.encode('utf-8'), 8)
    return cipher_text


def plain_string(msg, key):
    """takes in a string and a public key, decrypts the string with said
key, then returns the plain string"""
    plain_text = key.decrypt(msg, 32)
    return plain_text


def generate_RSA():
    """Generate an RSA keypair"""
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    return key


# Create your views here.
@csrf_exempt
def index(request):
    print("==================="+str(request.session.get('logged_user')))

    if not request.user.is_authenticated or request.session.get('logged_user') == None:
        return render(request, 'home.html', {'logedin': False})
    else:
        # all_users = User.objects.all()
        # the_report = Report.objects.get(get_user(request))
        # reports_to_show = {"file list": Document.objects.filter(report = the_report)}
        # reports_to_show = {"logedin" : True}
        # print(request.user.profile)
        return render(request, 'home.html', {"logedin": True, 'user': request.user})


# def login_page(request):
#     form = UserForm(request.POST or None)
#     return render(request, 'login.html', {"form":form})

def my_login(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['logged_user'] = username
                request.session['loged_in'] = True
                if next == 'home.html':
                    return render(request, "home.html", {"user": user, "logedin": True})
                else:
                    return render(request, "validate.html", {"user": user, "logedin": True})

            # Redirect to a success page.
            return render(request, 'login.html', {"message": "Disabled account!", "form": form})
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {"message": "invalid token!", "form": form})
    else:
        return render(request, "login.html", {"form": form})


def signup(request):
    # if request.method == 'POST':  # if the form has been filled

    form = UserForm(request.POST or None)
    profile = Profile_Form(request.POST or None)
    print(form.errors)
    messages = []
    messages.append(form.errors)
    if form.is_valid() and not profile.is_valid():  # All the data is valid
        user = form.save()
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        # user.set_email(email)
        password = request.POST.get('password', '')
        user.set_password(password)
        # profile = profile.save(commit=False)
        type = request.POST.get('type', '')
        if (str(type) == 'True'):
            # print("assigning type ", type)
            user.profile.is_investor = True
        else:
            # print("assigning type", type)
            user.profile.is_investor = False

        company = request.POST.get('company', '')
        if (company):
            user.profile.company = company
        # print(user.profile.company, user.profile.is_investor)    

        user.profile.save()
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if (not user.profile.is_investor) and user.profile.company == None:
                    messages.append("Registration failed! Please fill in the company field for a company user!")
                    print('here!')
                    # return redirect('/Lokahi/signup', {'messages':messages})
                    return render(request, "signup.html",
                                  {"form": form, "profileForm": profile, 'is_registered': False, 'messages': messages})
                else:
                    login(request, user)
                    request.session['logged_user'] = username
                    request.session['loged_in'] = True
                    return redirect("/Lokahi")

    return render(request, "signup.html",
                  {"form": form, "profileForm": profile, 'is_registered': False, 'messages': messages})
    # return render(request, 'signup.html', {'user_obj': user_obj, 'is_registered': True})  # Redirect after POST
    # else:
    #     form = UserForm()  # an unboundform
    #     return render(request, 'signup.html', {'form': form})


@login_required
def message_detail(request, message_id):
    message = Message.objects.filter(id=message_id)[0]
    # print("user " + message.receiver.username + "'s unread num is " + str(message.receiver.profile.unread_messages))
    # print("receiver id " + str(message.receiver.id))
    # print("user id " +str(request.user.id))

    # get the receiver's id and decrement receiver's unread message number
    if(message.unread):
        if (message.receiver.profile.unread_messages > 0):
            message.receiver.profile.unread_messages -= 1
        else:
            message.receiver.profile.unread_messages = 0
            print("unread message number for user " + message.receiver.username + " corrupted!")
    else:
        print("The message is already read.")
    # print("user " + message.receiver.username + "'s unread num after dec is " + str(
    #     message.receiver.profile.unread_messages))

    # print(message.content)
    # save the new number into user profile
    message.receiver.profile.save()
    message.unread = False
    message.save()
    return render(request, 'messagedetail.html', {"logedin": True, "message": message})


@login_required
def message_detail_decrypted(request, message_id):
    message = Message.objects.filter(id=message_id)[0]
    reader = request.session.get('logged_user')

    # initialize the plain text as an default error message string
    plain = "Decryption failed"
    receiver = message.receiver
    content = message.content

    # key factor for decryption. Since the database converted the tuple into string when storing, so we have to convert it back
    content = make_tuple(content)
    # print("content is ", content)
    # print("type of content", type(content))

    raw_key = message.key.encode('utf-8')
    # print("raw key", raw_key)
    # print("type of raw key", type(raw_key))

    # get the key from the message object
    parsed_key = RSA.importKey(message.key)
    # print("parsed key", parsed_key)

    # for debugging use, change the content within b'' with the correct exported RSA key
    # text_key = (
    # b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQC0Y04oecrWP1rcEHfRHvh/+SOchB/iX48FNPDMn6+XLSQdQfKT\nOKaLsJi8iGQWUG+mhg0at0Zd9NUEIjFWLpWFCW/bks2qC1oJieGi0QXLAKmN6K3Y\n3GVBUcc5I/06rbI4deQ/Falft9VIiy61FBXnhvb84XXZR0S2hmCSIXCLWwIDAQAB\nAoGBAK9i/lMMV9MHtmfQ+y4wVpzWt3EuZXHMR1pgpt/NQwRRt5Na02eg5Q1cnqRw\nWB/6BRR7sbIQEDK6IYLrW9zXXjdhkCq8n77aaDzX8tLnAe63p4xEDyy9BCAkU93F\nBR8WUnq3jy54k3q9e1KpXsWgOPLh7Y88bLaCS4m5r6qwO7hBAkEA058jB+Vye1XL\nWH/7dRjwMIL6CcJU91cOxcrJ9gQjccKbkXGt+Q4ssQNuBeb0+8e7VFvuvYb6yF4P\nBPl9L/wGvQJBANo3ZJJzPk2ul1mnrTvD4nTIKjXIQPYN62r2KJAmpk9wZWjTvF+9\neuOiMEDAL28fdblOI1he5kcYvtGORpnQZ/cCQGcYyEA4kCV2DrL25tKNa7a2mInY\nmvxE9XV27h1ktr/dR1z8PP1w4mT6fsdxVTi0fZcDkrPS5qpm6HpL8alG5yECQQCw\n7bLEr133vDSJA9QInjVxfI4E114cYoLbUcTnw/6acEY47VxRwB7wjCNVjL2o+rgH\nzBwKXb+WK7Ej1ZjWw8xXAkBQJ1iTkGF0apa89vV+wNOojW15ZL40Ffqyhycn7f5l\n6HIj8lSueBw49qNMfUqNrd0Q0KLauM/ih5APKLPB12yN\n-----END RSA PRIVATE KEY-----')
    # print("type of text key", type(text_key))
    # VERIFY IF IT IS THE RECEIVER TRYING TO DECRYPT
    if (str(reader) == str(receiver) and message.to_encrypt == True):
        print("pass the decrption check!!!")
        # plain_text = plain_string(message.content, key)
        # decrypt the content
        plain = RSA.importKey(raw_key).decrypt(content)

    # print("decrypt when read:", plain)
    return render(request, 'messagedetail.html',
                  {"logedin": True, "message": message, 'plaintext': plain, "dec": True})


@login_required
def sendMessage(request):
    form = sendMessageForm(request.POST or None)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            content = request.POST.get('content', '')
            # print("content is ", content)
            receiver_pk = request.POST.get('receiver', '')
            # print("recerver is ", receiver_pk)
            to_encrypt = request.POST.get('to_encrypt', '')
            # print("To encrypt:", to_encrypt)

            sender_name = request.session.get('logged_user')
            # print(sender_name)
            sender = User.objects.get(username=sender_name)
            # print("sender is", sender)
            time = datetime.now()
            # print("time is", time)

            message = form.save()
            message.receiver = User.objects.get(pk=receiver_pk)
            # increment the receiver's unread message amount
            message.receiver.profile.unread_messages += 1
            # print("user " + message.receiver.username + "'s unread message number is " + str(
            #     message.receiver.profile.unread_messages))
            # print("receiver id " + str(message.receiver.id))
            # print("sender id " + str(request.user.id))
            key = generate_RSA()

            if (to_encrypt == 'True'):
                content = secret_string(content, key.publickey())
                message.to_encrypt = True
            else:
                message.to_encrypt = False

            message.content = content
            message.sender = sender
            message.time = time

            text_key = key.exportKey()
            message.key = text_key
            message.unread = True
            message.save()
            message.receiver.profile.save()
            # plain = RSA.importKey(message.key).decrypt(message.content)
            # print("content is ", message.content)
            # print("type of content", type(content))
            # print("decrypt when send:", plain)
            # print("key is", key)
            # print("text key ", text_key)

            if message is not None:
                # print(message)
                receiver_name = User.objects.get(pk=receiver_pk).username
                success_message = "Message successfully sent to: " + receiver_name + "!"
                return render(request, "home.html", {"logedin": True, "message": success_message})

    return render(request, 'sendMessage.html', {"logedin": True, "form": form})


@login_required
def my_logout(request):
    # do something to log out
    logout(request)
    try:
        del request.session['user']
    except KeyError:
        pass
    try:
        del request.session['logged_in']
    except KeyError:
        pass

    form = UserForm(request.POST or None)
    # return render(request, 'logout.html', {"form": form})

    return redirect('login.html', {"form": form})


# the testing function executes with the showdata url to display the list of registered users

def showUsers(request):
    all_users = User.objects.all()
    # print(all_users)
    all_messages = Message.objects.all()
    # print(all_messages)
    return render(request, 'userdetail.html', {'all_users': all_users, "all_messages": all_messages})


@login_required
def inbox(request):
    # form = sendMessageForm(request.POST or None)
    all_messages = Message.objects.all()
    username = request.session.get('logged_user')
    # print("======",username,"======")
    # print("all messages: ",all_messages)
    return render(request, 'inbox.html', {"logedin": True, "messages": all_messages, "receiver_name": username})


# class MakeReport(CreateView):
#     model = Report
#     fields = ["owner", "date", "title", "company", "phone", "location", "country", "industry", "projects", "files", "private"]
#     success_url = '/Lokahi/ReportList/'
#     template_name = "addreport.html"



# class ReportList(ListView):
#     model = Report
#     template_name = "reportslist.html"

# def viewReports (request):
#     model = Report
#     template_name = "reportslist.html"
def ReportList(request):
    reports = Report.objects.all()
    return render(request, 'reportslist.html', {'reports': reports})


def report_list(request):
    reports = Report.objects.all()

    return render(request, 'reportslist.html', {'reports': reports})



def MakeReport(request):
    # Report.objects.get(pk=id)
    # Report.object.all()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            owner = request.POST.get('owner')
            company = request.POST.get('company')
            ceo = request.POST.get('ceo')
            phone = request.POST.get('phone')
            location = request.POST.get('location')
            country = request.POST.get('country')
            industry = request.POST.get('industry')
            sector = request.POST.get('sector')
            projects = request.POST.get('projects')
            encryptionKey = request.POST.get('encryptionKey')
            is_private = request.POST.get('is_private')
            is_encrypted = request.POST.get('is_encrypted')
            created_at = request.POST.get('created_at')
            report = Report.objects.create(title=title, ceo=ceo, owner=owner, company=company, phone=phone,
                                           location=location, country=country, industry=industry, sector=sector,
                                           encryptionKey=encryptionKey, projects=projects, is_private=is_private,
                                           is_encrypted=is_encrypted, created_at=created_at)

            report.save()

            for afile in request.FILES.getlist('files'):
                # url = afile
                # split = url.split("/").pop(0)
                # actualurl = split.join("/")
                actualurl="";
                encrypted = is_encrypted
                FileKey =  encryptionKey
                actualurl = "static/documents/" + str(afile);
                fileX = File.objects.create(file=afile, actualurl=actualurl, encrypted=encrypted, FileKey=FileKey)

                FILENAME = afile.name
                fileX.save()
                report.files.add(fileX)

            report.save()

            # if is_private == 'N':
            #     story = Story.objects.create(content=user.username+" created a report called "+report.projects)
            return HttpResponseRedirect('/Lokahi/ReportList')

        else:
            print(form.errors)
    else:
        form = ReportForm();
    return render(request, 'addReport.html', {'form': form})

def MakeFile (request, report_id):
    report = Report.objects.get(pk=report_id)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            encryptionKey = request.POST.get('FileKey')
            encrypted = request.POST.get('encrypted')


            report.save()

            for afile in request.FILES.getlist('files'):
                # url = afile
                # split = url.split("/").pop(0)
                # actualurl = split.join("/")
                actualurl="";
                encrypted = encrypted
                FileKey=encryptionKey
                actualurl = "static/documents/" + str(afile);
                fileX = File.objects.create(file=afile, actualurl=actualurl, report_id=report_id, encrypted=encrypted, FileKey=FileKey)
                FILENAME = afile.name
                fileX.save()
                report.files.add(fileX)

            report.save()

            # if is_private == 'N':
            #     story = Story.objects.create(content=user.username+" created a report called "+report.projects)
            return HttpResponseRedirect('/Lokahi/ReportList')

        else:
            print(form.errors)
    else:
       form = UploadForm();
    return render(request, 'makeFile.html', {'report': report,'form': form})

class addFile(CreateView):
    model = File
    fields = ["name", "reports", "encrypted", "encryptionKey", "filename"]
    template_name = "addfile.html"
    success_url = '/Lokahi/ReportList/'


class FileList(ListView):
    model = File
    template_name = "filelist.html"


class linkfile(UpdateView):
    model = Report
    fields = ["files"]
    template_name = "addFile.html"
    success_url = '/Lokahi/ReportList/'

class ReportUpdate(UpdateView):
    #instance =Report.objects.get(id=)
    model = Report
    # the fields mentioned below become the entyr rows in the update form
    fields = ['title', 'owner', 'company', 'ceo', 'phone', 'location', 'country','industry', 'sector', 'projects', 'is_private','is_encrypted']
    template_name = 'viewreport.html'
    success_url = '/Lokahi/ReportList/'
class deleteReport(DeleteView):
    model = Report
    success_url = '/Lokahi/ReportList/'
    template_name = 'deleteReport.html'


@login_required
def delete_message(request, message_id):
    to_delete_message = Message.objects.filter(id=message_id)[0]
    # print(to_delete_message)

    # also dec the unread amout if delete an unread msg
    if(to_delete_message.unread):
        request.user.profile.unread_messages -= 1
        request.user.profile.save()
    
    to_delete_message.delete()
    # Message.objects.all().delete()
    return render(request, 'home.html', {"logedin": True, 'message': 'Message successfully deleted!'})


class MakeGroup(CreateView):
    model = Group1
    fields = ["title", "owner", "participants"]
    success_url = '/Lokahi/GroupList/'
    template_name = "addgroup.html"


class GroupList(ListView):
    model = Group1
    template_name = "grouplist.html"


class addMember(UpdateView):
    model = Group1
    fields = ["participants"]
    template_name = "addgroup.html"
    success_url = '/Lokahi/GroupList/'


class deleteGroup(DeleteView):
    model = Group1
    success_url = '/Lokahi/GroupList/'
    template_name = 'deleteGroup.html'


def Validate(request):
    return render(request, 'validate.html')


def suspendUser(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = User.objects.get(username=search_id)
            user.is_active = False
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
            user.is_active = True
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
            u = User.objects.get(username=search_id)
            u.is_superuser = True
            u.save()
            return render(request, 'home.html')
        except User.DoesNotExist:
            return HttpResponse("no user by that username")
    else:
        return render(request, 'home.html')


def Validate(request):
    return render(request, 'validate.html')
