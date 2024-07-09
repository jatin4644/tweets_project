from django import forms   #(5) forms are inbuilt in django
from .models import Tweet   # (6) all models are to be included in forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class tweetform(forms.ModelForm):
    #(7) we always have to  make a meta class ,,,, its a part of syntax
    class Meta:
        #(8) we nees to specify the moddel to be used and fields to be included
        model=Tweet
        fields=['text' , 'photo']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        #we need to mention fields in meta class
        model=User
        fields=('username' , 'email' , 'password1' , 'password2')