from django.forms import ModelForm
from . import models

class RulzCreateForm(ModelForm):
    class Meta:
        model=models.Rulz
        fields = '__all__'
