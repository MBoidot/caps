from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#from django_superform import FormField, SuperForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput) 
    password2 = forms.CharField(label=("Confirm password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': ('Capser name'),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'birth_date')

