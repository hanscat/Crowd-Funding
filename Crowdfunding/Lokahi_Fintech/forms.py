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
    
class Profile_Form(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "company", 'class': 'form-control'}))
    types = ["company","investor","not declared"]
    role = forms.ChoiceField(choices=types, required=True, initial='--SELECT USER TYPE--')
    
    class Meta:
        model = Profile
        fields = ['role', 'company']