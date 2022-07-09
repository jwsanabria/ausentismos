from django import forms
from django.forms import ModelForm, Select, DateField, TextInput
from .models import Persona, Ausentismo, Accidente
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.conf import settings


class AusentismoForm(ModelForm):
    empleado = forms.ModelChoiceField(queryset=Persona.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    fecha_solicitud = DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format='%d-%m-%Y'))
    fecha_ausentismo = DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format='%d-%m-%Y'))
    class Meta:
        model = Ausentismo
        fields = ('empleado', 'motivo', 'fecha_solicitud', 'fecha_ausentismo', 'hora_inicial', 'hora_final', 'tiempo_ausentismo')
        widgets = {
            'motivo': forms.Select(attrs={'class': 'form-control'}),
            'hora_inicial': TimePickerInput(),
            'hora_final': TimePickerInput(),
            'tiempo_ausentismo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo entre la hora final e inicial', 'onclick' : 'calculaTiempo()'}),
        }

class AccidenteForm(ModelForm):
    class Meta:
        model = Accidente
        fields = ('__all__')