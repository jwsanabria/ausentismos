from django import forms
from django.forms import ModelForm, Select, DateField, TextInput
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.conf import settings
from .validators import validador_fecha_futura, validador_valor_positivo


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
    fecha_accidente = DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format='%d-%m-%Y'), validators=[validador_fecha_futura])


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
            'descripcion_accidente': forms.Textarea(attrs={'class': 'form-control', 'rows':"5", 'cols':"50"}),
            'invalidez': forms.CheckboxInput(),
            'incapacidad': forms.CheckboxInput(),
            'fallecido': forms.CheckboxInput(attrs={ 'onclick': 'accidenteMortal()'})

        }



class CostosAccInsumosMedicosForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_insumo = forms.BooleanField(widget=forms.HiddenInput, initial=True)


    class Meta:
        model = CostosAccInsumosMedicos

        fields = ('insumo', 'valor', 'cantidad')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'insumo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'})
        }

class CostosAccTransporteForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_transporte = forms.BooleanField(widget=forms.HiddenInput, initial=True)


    class Meta:
        model = CostosAccTransporte

        fields = ('elemento', 'valor')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'elemento': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CostosAccOtrosForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_otros = forms.BooleanField(widget=forms.HiddenInput, initial=True)


    class Meta:
        model = CostosAccOtros

        fields = ('elemento', 'valor')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Valor Unitario'}),
            'elemento': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Elemento'}),
        }

class CostosAccMaquinariaForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_maquinaria = forms.BooleanField(widget=forms.HiddenInput, initial=True)


    class Meta:
        model = CostosAccMaquinaria

        fields = ('elemento', 'valor', 'cantidad')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Valor hora'}),
            'elemento': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Elemento'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Cantidad'}),
        }



class CostosAccRepuestoForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_repuesto = forms.BooleanField(widget=forms.HiddenInput, initial=True)


    class Meta:
        model = CostosAccRepuestos

        fields = ('elemento', 'valor', 'cantidad')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Valor hora'}),
            'elemento': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Elemento'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Cantidad'}),
        }



class CostosAccManoObraForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_manoObra = forms.BooleanField(widget=forms.HiddenInput, initial=True)


    class Meta:
        model = CostosAccManoObra

        fields = ('descripcion', 'valor', 'cantidad')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Valor hora'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Descripción'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Cantidad'}),
        }


class DanoMaterialForm(forms.Form):
    fecha_liquidacion = DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format='%d-%m-%Y'))


class DanoMoralForm(forms.Form):
    NIVEL = (
        ('N1', 'Nivel 1'),
        ('N2', 'Nivel 2'),
        ('N3', 'Nivel 3'),
        ('N4', 'Nivel 4'),
        ('N5', 'Nivel 5'),
    )
    nivel = forms.CharField(widget=forms.Select(choices=NIVEL))
    cantidad = forms.DecimalField(validators=[validador_valor_positivo])

    def __init__(self, *args, **kwargs):
        super(DanoMoralForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })



class CostosAccDanoEmergenteForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])

    class Meta:
        model = CostosAccDanoEmergente

        fields = ('descripcion', 'valor')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Valor hora'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Descripción'}),
        }


class TiemposAccAcompanamientoForm(ModelForm):
    empleado = forms.ModelChoiceField(queryset=Persona.objects.all(), widget=Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(TiemposAccAcompanamientoForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = TiemposAccAcompanamiento
        exclude = ('salario', 'valor_diario', 'valor_factor', 'total')
        fields = ('empleado', 'tipo_acompanamiento', 'tiempo', 'factor')
        widgets = {
            'tiempo': TimePickerInput()
        }

class ReemplazosAccForm(ModelForm):
    reemplazo = forms.ModelChoiceField(queryset=Persona.objects.all(), widget=Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ReemplazosAccForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = ReemplazoAccidente
        exclude = ('salario',)
        fields = ('reemplazo', 'tipo_reemplazo', 'dias')
        widgets = {
            'dias': forms.NumberInput(attrs={'class': 'form-control'}),
        }



class CapacitacionAccForm(ModelForm):
    capacitador = forms.ModelChoiceField(queryset=Persona.objects.all(), widget=Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(CapacitacionAccForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = CapacitadorAccidente
        exclude = ('salario',)
        fields = ('capacitador', 'dias')
        widgets = {
            'dias': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CostosAccAdicionalesForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])

    class Meta:
        model = CostosAccAdicionales

        fields = ('actividad', 'valor')
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Valor'}),
            'actividad': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Actividad'}),
        }