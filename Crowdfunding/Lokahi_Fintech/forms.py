from django import forms

class UserForm(forms.Form):
    #to take the input of username
    username = forms.CharField(max_length=100, required=True)
    # to take the input of email
    email = forms.CharField(max_length=100, required=True)
    # to take the input of password
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    retype_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())
    
class Login(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())