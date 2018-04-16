from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm

def HomeView(request):
    template_name = "home/home_template.html"
    return render(request,template_name)


class UserFormView(View):
    form_class = UserForm
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

            #cleaned and normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')

        return render (request, self.template_name, {'form': form})

