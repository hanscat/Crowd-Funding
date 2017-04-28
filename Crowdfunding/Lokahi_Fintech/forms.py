from django import forms
from django.core import validators
from .models import *

class UserForm(forms.ModelForm):
    #to take the input of username
    username = forms.CharField(max_length=100, required=True)
    # to take the input of email
    email = forms.EmailField(help_text='A valid email address, please.')
    # to take the input of password
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    retype_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    company = forms.CharField(max_length=100, required=True)
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password","email"]
    
class loginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    
class sendMessageForm(forms.ModelForm):
    content = forms.CharField(max_length=500, widget=forms.Textarea)
    receiver = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="--Select a Receiver--")
    to_encrypt = forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )
    class Meta:
        model = Message
        # fields = ['receiver', 'content', 'sender', 'time']
        exclude = ['sender', 'time']
    
class Profile_Form(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "company", 'class': 'form-control'}))
    types = ["company","investor","not declared"]
    role = forms.ChoiceField(choices=types, required=True, initial='--SELECT USER TYPE--')
    
    class Meta:
        model = Profile
        fields = ['role', 'company']

class UploadForm(forms.Form):
    files = forms.FileField(label="Upload a file here",
                              widget=forms.FileInput(attrs={'multiple': True, 'type': 'file', 'class': 'button'}),
                              required=False)
    class Meta:
        model = Report
        fields = ("files",)

class ReportForm(forms.ModelForm):
    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'),)
    title = forms.CharField(required=True, label="Enter Report Title")
    company = forms.CharField(required=True, label="Enter Company Name")
    owner = forms.CharField(required=True, label="Enter Owner Name")
    phone = forms.CharField(required=True, label="Enter Company Phone Number")
    location = forms.CharField(required=True, label="Enter Company Location")
    country = forms.CharField(required=True, label="Enter Company Country")
    industry = forms.CharField(required=True, label="Enter Industry")
    sector = forms.CharField(required=True, label="Enter Company Sector")
    projects = forms.CharField(required=True, label="Enter Project Name")
    is_private = forms.BooleanField(label="Is This Private?", required=False)
    is_encrypted = forms.BooleanField(label="Is The File Encrypted?", required =False)
    files = forms.FileField(label="Upload a file here",
                              widget=forms.FileInput(attrs={'multiple': True, 'type': 'file', 'class' : 'button'}), required=False) #'onchange':'getName'
    class Meta:
        model= Report;
        fields = ['title','company','owner','phone','location','country','industry','sector', 'projects', 'created_at', 'is_private', 'is_encrypted', 'files']



