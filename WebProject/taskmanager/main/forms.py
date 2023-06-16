from django import forms
from .models import *

class AddPostForm(forms.Form):
    subject = forms.CharField(max_length=100)