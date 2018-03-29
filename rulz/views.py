from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView
from rulz.models import Rulz
    
def rules_home(request):
    template_name = "rulz/home_template.html"
    return render(request,template_name)

class Rulz_IndexView(generic.ListView):
    template_name = "rulz/index_template.html"
    context_object_name = 'all_rulz'

    def get_queryset(self):
        return Rulz.objects.all()

class Rulz_DetailView(generic.DetailView):
    template_name = "rulz/detail_template.html"
    #have to pass stuff to the request like Id of the current rule etc..., Check also on the button that leads here on the template (index_tempalte in rules)


class RulzCreate(CreateView):
    model = Rulz
    fields = ['title','content','country','city','player_num','complexity']
