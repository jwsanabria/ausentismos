from django import forms
from django.forms import ModelForm, Select, DateField, TextInput
from .models import Persona, Ausentismo, Accidente, CostosAccInsumosMedicos
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
    empleado = forms.ModelChoiceField(queryset=Persona.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    fallecido = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control', 'onclick': 'accidenteMortal()'}))
    invalidez = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    incapacidad = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    fecha_accidente = DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format='%d-%m-%Y'))


    class Meta:
        model = Accidente
        fields = ('empleado', 'fecha_accidente', 'hora_accidente', 'tipo_jornada', 'inicio_jornada', 'final_jornada',
                  'fallecido', 'incapacidad', 'invalidez', 'dias_incapacidad', 'grado_invalidez', 'descripcion_accidente',
                  'codigo_cie10', 'factor_personal', 'factor_laboral', 'acto_subestandar', 'cond_ambientales_subestandar')
        widgets = {
            'hora_accidente': TimePickerInput(),
            'inicio_jornada': TimePickerInput(),
            'final_jornada': TimePickerInput(),
            'tipo_jornada': Select(attrs={'class': 'form-control',  'placeholder': 'Seleccione jornada'}),
            'dias_incapacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'grado_invalidez': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'codigo_cie10': Select(attrs={'class': 'form-control'}),
            'factor_personal': Select(attrs={'class': 'form-control'}),
            'factor_laboral': Select(attrs={'class': 'form-control'}),
            'acto_subestandar': Select(attrs={'class': 'form-control'}),
            'cond_ambientales_subestandar': Select(attrs={'class': 'form-control'}),

        }



class CostosAccInsumosMedicosForm(ModelForm):

    class Meta:
        model = CostosAccInsumosMedicos
        exclude = ('accidente',)
        fields = ('insumo', 'valor', 'cantidad')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'insumo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'})
        }