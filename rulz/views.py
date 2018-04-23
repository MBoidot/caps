from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView
from rulz.models import Rulz
    
def rules_home(request):
    template_name = "rulz/rulz_home_template.html"
    return render(request,template_name)
