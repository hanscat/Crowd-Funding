from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, authenticate, login, get_user
from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from Crypto.PublicKey import RSA
from Crypto import Random

# helper functions for encryption & decryptions
def secret_string(msg, public_key):
    """takes in a string and a public key, encrypts the string with said
key, then returns the resulting string"""
    cipher_text = public_key.encrypt(msg.encode('utf-8'), 8)
    return cipher_text


def plain_string(msg, key):
    """takes in a string and a public key, decrypts the string with said
key, then returns the plain string"""
    plain_text = key.decrypt(msg,32)
    return plain_text


def generate_RSA():
    """Generate an RSA keypair"""
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    return key


# Create your views here.
@csrf_exempt
def index(request):
    # print("==================="+request.session.get('loged_user'))
    if not request.user.is_authenticated:
        return render(request, 'home.html', {'logedin': False})
    else:
        # all_users = User.objects.all()
        # the_report = Report.objects.get(get_user(request))
        # reports_to_show = {"file list": Document.objects.filter(report = the_report)}
        # reports_to_show = {"logedin" : True}
        return render(request, 'home.html', {"logedin": True})


# def login_page(request):
#     form = UserForm(request.POST or None)
#     return render(request, 'login.html', {"form":form})

def my_login(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['logged_user'] = username
                request.session['loged_in'] = True
                return render(request, "home.html", {"user": user, "logedin": True})
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

    if form.is_valid() and not profile.is_valid():  # All the data is valid
        user = form.save()

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
                request.session['logged_user'] = username
                request.session['loged_in'] = True
                return redirect("/Lokahi")

    return render(request, "signup.html", {"form": form, "profileForm": profile, 'is_registered': False})
    # return render(request, 'signup.html', {'user_obj': user_obj, 'is_registered': True})  # Redirect after POST
    # else:
    #     form = UserForm()  # an unboundform
    #     return render(request, 'signup.html', {'form': form})


@login_required
def sendMessage(request):
    form = sendMessageForm(request.POST or None)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            content = request.POST.get('content', '')
            print("content is ", content)
            receiver_pk = request.POST.get('receiver', '')
            print("recerver is ", receiver_pk)
            to_encrypt = request.POST.get('to_encrypt', '')
            print("To encrypt:", to_encrypt)

            sender_name = request.session.get('logged_user')
            print(sender_name)
            sender = User.objects.get(username=sender_name)
            print("sender is", sender)
            time = datetime.now()
            print("time is", time)


            message = form.save()
            message.receiver = User.objects.get(pk=receiver_pk)
            key = generate_RSA()

            if (to_encrypt == 'True'):
                content = secret_string(content, key.publickey())
                plain = RSA.importKey(message.key).decrypt(message.content)
                print(plain)
                message.to_encrypt = True
            else:
                message.to_encrypt = False
                
            message.content = content
            message.sender = sender
            message.time = time

            text_key = key.exportKey()
            message.key = text_key
            message.save()

            # print("key is", key)
            # print("text key ", text_key)

            if message is not None:
                print(message)
                receiver_name = User.objects.get(pk=receiver_pk).username
                success_message = "Message successfully sent to: " + receiver_name + "!"
                # return redirect("/Lokahi", {"message":success_message})
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


@login_required
def message_detail(request, message_id):
    message = Message.objects.filter(id=message_id)[0]
    print(message.content)
    return render(request, 'messagedetail.html', {"logedin": True, "message": message})


@login_required
def message_detail_decrypted(request, message_id):
    message = Message.objects.filter(id=message_id)[0]
    # print(message.content)
    reader = request.session.get('logged_user')
    receiver = message.receiver
    # VERIFY IF IT IS THE RECEIVER TRYING TO DECRYPT
    plain = ""
    # print("text key", message.key.encode('ascii'))
    key = RSA.importKey(message.key)
    if (reader == receiver and message.to_encrypt == True):
        plain_text = plain_string(message.content, key)
        plain = RSA.importKey(message.key).decrypt(message.content)
    print("key is ", key)
    print("plain text is: ",plain)
    return render(request, 'messagedetail.html',
                  {"logedin": True, "message": message, 'plaintext': plain, "dec":True})


@login_required
def delete_message(request, message_id):
    to_delete_message = Message.objects.filter(id=message_id)
    # print(to_delete_message)
    to_delete_message.delete()
    # Message.objects.all().delete()
    return render(request, 'home.html', {"logedin": True, 'message': 'Message successfully deleted!'})


class MakeGroup(CreateView):
    model = Group
    fields = ["title", "owner", "participants"]
    success_url = '/Lokahi/GroupList/'
    template_name = "addgroup.html"


class GroupList(ListView):
    model = Group
    template_name = "grouplist.html"


class addMember(UpdateView):
    model = Group
    fields = ["participants"]
    template_name = "addgroup.html"
