from django.shortcuts import render, redirect
from django.views import generic

def HomeView(request):
    template_name = "home/home_template.html"
    return render(request,template_name)