from django import forms
from django.core import validators

class UserForm(forms.Form):
    #to take the input of username
    username = forms.CharField(max_length=100, required=True)
    # to take the input of email
    email = forms.EmailField(help_text='A valid email address, please.')
    # to take the input of password
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    retype_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    
class loginFrom(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    
    
    