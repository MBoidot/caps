from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


def HomeView(request):
    template_name = "home/home_template.html"
    return render(request,template_name)


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'home/registration_form.html', {'form': f})



class UserFormView(View):
    form_class = SignUpForm
    template_name = 'home/registration_form.html'
    
    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render (request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.refresh_from_db()  # load the profile instance created by the signal
            password = form.cleaned_data['password1']
            user.set_password(password)
            username = form.cleaned_data['username']
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.location = form.cleaned_data.get('location')    
            user.save()

            #return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')

        return render (request, self.template_name, {'form': form})

'''def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('rulz/rules_home')
    else:
        form = SignUpForm()
    return render(request, 'home/registration_form.html', {'form': form})'''