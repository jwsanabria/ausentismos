from django import forms
from django.forms import ModelForm
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

from .models import Ausentismo

class AusentismoForm(ModelForm):
    class Meta:
        model = Ausentismo
        fields = '__all__'
        widgets = {
            'fecha_solicitud': DatePickerInput(),
            'fecha_ausentismo': DatePickerInput(),
            'hora_inicial': TimePickerInput(),
            'hora_final': TimePickerInput(),
            'tiempo_ausentismo': TimePickerInput(),
        }