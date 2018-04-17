from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField()
    location = forms.CharField()
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput) 
    password2 = forms.CharField(label=("Confirm password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'location','email', 'birth_date')
        widgets = {
            'birth_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        labels = {
            'username': ('Capser name'),
        }
        help_texts = {
            'username' : None,
            'birth_date': None,
        }



#class ProfileForm(forms.ModelForm):
#    class Meta:
#       model = Profile
#        fields = ('location', 'birth_date')

