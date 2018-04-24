from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rulz.models import Rulz
from .forms import RulzCreateForm

    
def rules_home(request):
    template_name = "rulz/rulz_home_template.html"
    return render(request,template_name)

class rules_index(generic.ListView):
    template_name = 'rulz/rulz_index_template.html'
    context_object_name = 'all_rulz'

    def get_queryset(self):
        return Rulz.objects.all()

class rules_detail(DetailView):
    model = Rulz
    template_name = 'rulz/rulz_detail_template.html'

class rules_create(CreateView):
    model=Rulz
    form_class = RulzCreateForm
    fields=['title', 'content','country','city' , 'player_num', 'complexity']
    template_name="rulz/rulz_create_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render (request, self.template_name, {'form': form})