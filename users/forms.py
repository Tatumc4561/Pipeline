from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

# create form

# ModelForm would work, but does not automatically hash passwords
class NewRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class NewLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput, label="password", max_length=10
    )


class NewLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput, label="password", max_length=10
    )


class FollowForm(ModelForm):
    class Meta:
        model = MyFollowings
        fields = "__all__"
