from django.forms import ModelForm

from .models import Ausentismo

class AusentismoForm(ModelForm):
    class Meta:
        model = Ausentismo
        fields = '__all__'