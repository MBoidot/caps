from django.forms import ModelForm
from . import models

class RulzCreateForm(ModelForm):
    class Meta:
        model=models.Rulz
        fields = ['title','content','country','city','player_num','complexity']


class RulzCommentForm(ModelForm):
    class Meta:
        model = models.RulzComment
        fields = ['author', 'text']