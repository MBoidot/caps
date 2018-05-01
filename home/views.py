from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,ProfileForm
from .models import Profile
from rulz.models import Rulz, RulzComment
from django.db.models import Count
from rulz.views import rules_index
from django.contrib.auth.models import User


def HomeView(request):
    template_name = "home/home_template.html"
    total_comments = RulzComment.objects.count()
    mycomments = RulzComment.objects.filter(author=request.user).count()
    comments_percentage = mycomments/total_comments*100
    myrulz = Rulz.objects.filter(author=request.user).count()
    total_rulz = Rulz.objects.count()
    rulz_percentage = myrulz/total_rulz*100
    nb_users = User.objects.count()

    def get_context_data(self, **kwargs):
        context = super(rules_index, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    return render(request,template_name,
    context={
    'total_comments': total_comments,
    'mycomments':mycomments,
    'comments_percentage':comments_percentage,
    'myrulz':myrulz,
    'total_rulz':total_rulz,
    'rulz_percentage':rulz_percentage,
    'nb_users':nb_users
    })



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
            #new_profile = profileform.save(commit=False)

            new_profile = Profile.objects.create(
                user=user,
                location=profileform.cleaned_data.get('location'),
                birth_date=profileform.cleaned_data.get('birth_date')
            )

            #return user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:home')

        return render (request, self.template_name, {'userform': userform, 'profileform':profileform})