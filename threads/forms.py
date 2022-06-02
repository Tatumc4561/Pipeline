from django import forms
from .models import *
from django.forms import ModelForm


class NewThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ["title", "text", "image"]
