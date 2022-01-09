from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Rulz
from django.forms import ModelForm

class RulzCreateForm(ModelForm):
    class Meta:
        model = Rulz
        fields= ('title', 'content', 'country', 'city','player_num','complexity','author')
