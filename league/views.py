from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import League


class league_index(generic.ListView):
    template_name = 'league/league_index_template.html'
    context_object_name = 'all_leagues'

    def get_queryset(self):
        return League.objects.all()

