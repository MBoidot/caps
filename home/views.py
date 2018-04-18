from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,ProfileForm
from .models import Profile

def HomeView(request):
    template_name = "home/home_template.html"
    return render(request,template_name)

class UserFormView(View):
    Userform_class = SignUpForm
    Profileform_class = ProfileForm
    template_name = 'home/registration_form.html'

    #display a blank form
    def get(self, request):
        userform = self.Userform_class(None)
        profileform=self.Profileform_class(None)

        return render (request, self.template_name, {'userform': userform, 'profileform': profileform})

    #process form data
    def post(self, request):
        userform = self.Userform_class(request.POST)
        profileform = self.Profileform_class(request.POST)

        if userform.is_valid() and profileform.is_valid():
            user = userform.save(commit=False)
            #user.refresh_from_db()  # load the profile instance created by the signal
            password = userform.cleaned_data['password1']
            user.set_password(password)
            username = userform.cleaned_data['username']
            first_name=userform.cleaned_data['first_name']
            last_name=userform.cleaned_data['last_name']
            email = userform.cleaned_data['email']
            user.save()

            new_profile = user_profile.objects.get(user = request.user)
            new_profile.objects.create(
                user=user,
                location=profileform.cleaned_data.get('location'),
                birth_date=profileform.cleaned_data.get('birth_date'))
            new_profile.save()

            #return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')

        return render (request, self.template_name, {'userform': userform, 'profileform':profileform})
