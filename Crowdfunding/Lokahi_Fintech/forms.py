from django import forms
from django.core import validators
from .models import *


class UserForm(forms.ModelForm):
    # to take the input of username
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # to take the input of email
    email = forms.EmailField(help_text='A valid email address, please.',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    # to take the input of password
    password = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    retype_password = forms.CharField(max_length=100, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    company = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=((True, 'Investor'), (False, 'Company')),
        widget=forms.RadioSelect(attrs={'class': 'optionsRadios'})
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "email"]


class loginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput())


class sendMessageForm(forms.ModelForm):
    content = forms.CharField(max_length=500, widget=forms.Textarea)
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="--Select a Receiver--")
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
    types = ["company", "investor", "not declared"]
    role = forms.ChoiceField(choices=types, required=True, initial='--SELECT USER TYPE--')

    class Meta:
        model = Profile
        fields = ['role', 'company']

class ReportForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required = True)
    body = forms.CharField(required=True)