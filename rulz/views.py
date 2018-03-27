from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import indexV, DetailView, FormView
    

def rules_index(request):
    template_name = "rulz/home_template.html"
    return render(request,template_name)