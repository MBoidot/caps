from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rulz.models import Rulz, RulzComment
from .forms import RulzCreateForm, RulzCommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count


    
def rules_home(request):
    template_name = "rulz/rulz_home_template.html"
    return render(request,template_name)

class rules_index(generic.ListView):
    template_name = 'rulz/rulz_index_template.html'
    context_object_name = 'all_rulz'

    def get_queryset(self):
        return Rulz.objects.select_related().annotate(comment_count=Count('rcomments'))

    def get_context_data(self, **kwargs):
        context = super(rules_index, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context



class rules_detail(DetailView):
    model = Rulz
    template_name = 'rulz/rulz_detail_template.html'
    def get_context_data(self):
        return self.RulzComment.all()

'''   def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['comment_list'] = RulzComment.objects.all()
        return context'''





#login required decorator placed in the urls.py file
class rules_create(CreateView):
    model = Rulz
    Rulzform_class = RulzCreateForm
    fields=['title','content','country','city','player_num','complexity']

    #process form data
    def post(self, request):
        rulzform = self.Rulzform_class(request.POST)

        if rulzform.is_valid():
            rulz = rulzform.save(commit=False)
            rulz.author = request.user
            rulz.save()

        return redirect('home:home')


'''class add_comment_to_rule(CreateView):
    model = RulzComment
    RulzCommentform_class = RulzCommentForm
    fields=['text']

    def post(self, request):
        rulzcommentform = self.RulzCommentform_class(request.POST)

        if rulzcommentform.is_valid():
            rcomment = rulzcommentform.save(commit=False)
            rcomment.rule = request.rule
            rcomment.author = request.user

        return redirect('rulz:rulz_detail', pk=Rulz.pk)'''
        

def add_comment_to_rule(request, pk):
    rule = get_object_or_404(Rulz, pk=pk)
    if request.method == "POST":
        form = RulzCommentForm(request.POST)
        if form.is_valid():
            rcomment = form.save(commit=False)
            rcomment.rule = rule
            rcomment.save()
            return redirect('rulz_detail', pk=rule.pk)
    else:
        form = RulzCommentForm()
    return render(request, 'rulz/add_comment_to_rule.html', {'form': form})
