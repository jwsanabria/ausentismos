from django import forms
from django.forms import ModelForm, Select, DateField, TextInput
from .models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django.conf import settings
from .validators import validador_fecha_futura, validador_valor_positivo


class AusentismoForm(ModelForm):
    empleado = forms.ModelChoiceField(
        queryset=Persona.objects.all(), widget=Select(attrs={"class": "form-control"})
    )
    fecha_solicitud = DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=DatePickerInput(format="%d-%m-%Y"),
    )
    fecha_ausentismo = DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=DatePickerInput(format="%d-%m-%Y"),
    )
    tiempo_ausentismo = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super(AusentismoForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )

    class Meta:
        model = Ausentismo
        fields = (
            "empleado",
            "motivo",
            "fecha_solicitud",
            "fecha_ausentismo",
            "tiempo_ausentismo",
            "periodo_ausentismo",
        )


class AccidenteForm(ModelForm):
    empleado = forms.ModelChoiceField(
        queryset=Persona.objects.all(), widget=Select(attrs={"class": "form-control"})
    )
    fecha_accidente = DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=DatePickerInput(format="%d-%m-%Y"),
        validators=[validador_fecha_futura],
    )

    class Meta:
        model = Accidente
        fields = (
            "empleado",
            "fecha_accidente",
            "hora_accidente",
            "tipo_jornada",
            "inicio_jornada",
            "final_jornada",
            "fallecido",
            "incapacidad",
            "invalidez",
            "dias_incapacidad",
            "grado_invalidez",
            "descripcion_accidente",
            "codigo_cie10",
            "factor_personal",
            "factor_laboral",
            "acto_subestandar",
            "cond_ambientales_subestandar",
        )
        widgets = {
            "hora_accidente": TimePickerInput(),
            "inicio_jornada": TimePickerInput(),
            "final_jornada": TimePickerInput(),
            "tipo_jornada": Select(
                attrs={"class": "form-control", "placeholder": "Seleccione jornada"}
            ),
            "dias_incapacidad": forms.NumberInput(attrs={"class": "form-control"}),
            "grado_invalidez": forms.NumberInput(
                attrs={"class": "form-control", "min": 0, "max": 100}
            ),
            "codigo_cie10": Select(attrs={"class": "form-control"}),
            "factor_personal": Select(attrs={"class": "form-control"}),
            "factor_laboral": Select(attrs={"class": "form-control"}),
            "acto_subestandar": Select(attrs={"class": "form-control"}),
            "cond_ambientales_subestandar": Select(attrs={"class": "form-control"}),
            "descripcion_accidente": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "5",
                    "cols": "50",
                    "value": "Cuando, Quién",
                }
            ),
            "invalidez": forms.CheckboxInput(),
            "incapacidad": forms.CheckboxInput(),
            "fallecido": forms.CheckboxInput(attrs={"onclick": "accidenteMortal()"}),
        }

    def __init__(self, *args, **kargs):
        super(AccidenteForm, self).__init__(*args, **kargs)
        self.initial[
            "descripcion_accidente"
        ] = "Cuando, Quién, Donde, Se encontraba, Sucede que, Actividad ordenada por, Se encontraba con"


class CostosAccInsumosMedicosForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_insumo = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CostosAccInsumosMedicos

        fields = ("insumo", "valor", "cantidad")
        widgets = {
            "valor": forms.NumberInput(attrs={"class": "form-control"}),
            "insumo": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control"}),
        }


class CostosAccTransporteForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_transporte = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CostosAccTransporte

        fields = ("elemento", "valor")
        widgets = {
            "valor": forms.NumberInput(attrs={"class": "form-control"}),
            "elemento": forms.TextInput(attrs={"class": "form-control"}),
        }


class CostosAccOtrosForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_otros = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CostosAccOtros

        fields = ("elemento", "valor")
        widgets = {
            "valor": forms.NumberInput(
                attrs={
                    "class": "form-control mb-2 mr-sm-2",
                    "placeholder": "Valor Unitario",
                }
            ),
            "elemento": forms.TextInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Elemento"}
            ),
        }


class CostosAccMaquinariaForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_maquinaria = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CostosAccMaquinaria

        fields = ("elemento", "valor", "cantidad")
        widgets = {
            "valor": forms.NumberInput(
                attrs={
                    "class": "form-control mb-2 mr-sm-2",
                    "placeholder": "Valor hora",
                }
            ),
            "elemento": forms.TextInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Elemento"}
            ),
            "cantidad": forms.NumberInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Cantidad"}
            ),
        }


class CostosAccRepuestoForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_repuesto = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CostosAccRepuestos

        fields = ("elemento", "valor", "cantidad")
        widgets = {
            "valor": forms.NumberInput(
                attrs={
                    "class": "form-control mb-2 mr-sm-2",
                    "placeholder": "Valor hora",
                }
            ),
            "elemento": forms.TextInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Elemento"}
            ),
            "cantidad": forms.NumberInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Cantidad"}
            ),
        }


class CostosAccManoObraForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])
    nuevo_manoObra = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = CostosAccManoObra

        fields = ("descripcion", "valor", "cantidad")
        widgets = {
            "valor": forms.NumberInput(
                attrs={
                    "class": "form-control mb-2 mr-sm-2",
                    "placeholder": "Valor hora",
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "class": "form-control mb-2 mr-sm-2",
                    "placeholder": "Descripción",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Cantidad"}
            ),
        }


class DanoMaterialForm(forms.Form):
    fecha_liquidacion = DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=DatePickerInput(format="%d-%m-%Y"),
    )


class DanoMoralForm(forms.Form):
    NIVEL = (
        ("N1", "Nivel 1"),
        ("N2", "Nivel 2"),
        ("N3", "Nivel 3"),
        ("N4", "Nivel 4"),
        ("N5", "Nivel 5"),
    )
    nivel = forms.CharField(widget=forms.Select(choices=NIVEL))
    cantidad = forms.DecimalField(validators=[validador_valor_positivo])

    def __init__(self, *args, **kwargs):
        super(DanoMoralForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )


class BalanceAsegurableForm(ModelForm):
    TIPO = (
        ("AD", "ASEGURABLE - DIRECTO"),
        ("AI", "ASEGURABLE - INDIRECTO"),
        ("ND", "NO ASEGURABLE - DIRECTO"),
        ("NI", "NO ASEGURABLE - INDIRECTO"),
    )

    tipo1 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo2 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo3 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo4 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo5 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo6 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo7 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo8 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo9 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo10 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo11 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo12 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo13 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo14 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo15 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo16 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo17 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo18 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo19 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo20 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo21 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo22 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo23 = forms.CharField(widget=forms.Select(choices=TIPO))
    tipo24 = forms.CharField(widget=forms.Select(choices=TIPO))

    def __init__(self, *args, **kwargs):
        super(BalanceAsegurableForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )

    class Meta:
        model = BalanceAccidente
        fields = (
            "tipo1",
            "tipo2",
            "tipo3",
            "tipo4",
            "tipo5",
            "tipo6",
            "tipo7",
            "tipo8",
            "tipo9",
            "tipo10",
            "tipo11",
            "tipo12",
            "tipo13",
            "tipo14",
            "tipo15",
            "tipo16",
            "tipo17",
            "tipo18",
            "tipo19",
            "tipo20",
            "tipo21",
            "tipo22",
            "tipo23",
            "tipo24",
        )


class CostosAccDanoEmergenteForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])

    class Meta:
        model = CostosAccDanoEmergente

        fields = ("descripcion", "valor")
        widgets = {
            "valor": forms.NumberInput(
                attrs={
                    "class": "form-control mb-2 mr-sm-2",
                    "placeholder": "Valor hora",
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "class": "form-control mb-2 mr-sm-2",
                    "placeholder": "Descripción",
                }
            ),
        }


class TiemposAccAcompanamientoForm(ModelForm):
    empleado = forms.ModelChoiceField(
        queryset=Persona.objects.all(), widget=Select(attrs={"class": "form-control"})
    )

    def __init__(self, *args, **kwargs):
        super(TiemposAccAcompanamientoForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )

    class Meta:
        model = TiemposAccAcompanamiento
        exclude = ("salario", "valor_diario", "valor_factor", "total")
        fields = ("empleado", "tipo_acompanamiento", "tiempo", "factor")
        widgets = {"tiempo": TimePickerInput()}


class ReemplazosAccForm(ModelForm):
    reemplazo = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        widget=Select(attrs={"class": "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ReemplazosAccForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )
            if name == "reemplazo":
                self.fields[name].widget.attrs.update(
                    {
                        "disabled": True,
                    }
                )

    class Meta:
        model = ReemplazoAccidente
        exclude = ("valor_salarial_real",)
        fields = ("tipo_reemplazo", "dias", "reemplazo", "salario", "nombre_reemplazo")
        widgets = {
            "dias": forms.NumberInput(attrs={"class": "form-control"}),
            "salario": forms.NumberInput(attrs={"disabled": True}),
            "nombre_reemplazo": forms.TextInput(attrs={"disabled": True}),
        }


class CapacitacionAccForm(ModelForm):
    capacitador = forms.ModelChoiceField(
        queryset=Persona.objects.all(), widget=Select(attrs={"class": "form-control"})
    )

    def __init__(self, *args, **kwargs):
        super(CapacitacionAccForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control",
                }
            )

    class Meta:
        model = CapacitadorAccidente
        exclude = ("salario",)
        fields = ("capacitador", "dias")
        widgets = {
            "dias": forms.NumberInput(attrs={"class": "form-control"}),
        }


class CostosAccAdicionalesForm(ModelForm):
    valor = forms.DecimalField(validators=[validador_valor_positivo])

    class Meta:
        model = CostosAccAdicionales

        fields = ("actividad", "valor")
        widgets = {
            "valor": forms.NumberInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Valor"}
            ),
            "actividad": forms.TextInput(
                attrs={"class": "form-control mb-2 mr-sm-2", "placeholder": "Actividad"}
            ),
        }
