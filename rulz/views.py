from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rulz.models import Rulz
from .forms import RulzCreateForm
from django.contrib.auth.decorators import login_required

    
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



#login required decorator placed in the urls.py file
class rules_create(CreateView):
    model = Rulz
    Rulzform_class = RulzCreateForm

    #process form data
    def post(self, request):
        rulzform = self.Rulzform_class(request.POST)

        if rulzform.is_valid():
            rulz = rulzform.save(commit=False)
            rulz.author = request.user
            rulz.save()

        return redirect('home:home')


