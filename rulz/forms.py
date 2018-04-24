from .models import Rulz
from django.forms import ModelForm


class RulzCreateForm(ModelForm):

    class Meta:
        model = Rulz
        fields = '__all__'


