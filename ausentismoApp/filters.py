import django_filters
from django_filters import DateFromToRangeFilter
from .models import Ausentismo, Accidente

class AusentismoFilter(django_filters.FilterSet):
    fecha_ausentismo = DateFromToRangeFilter()
    class Meta:
        model = Ausentismo
        fields = ['empleado', 'motivo', 'sede', 'area', 'seccion', 'cargo', 'fecha_ausentismo']

    def __init__(self, *args, **kwargs):
        super(AusentismoFilter, self).__init__(*args, **kwargs)
        self.filters['empleado'].extra.update({'empty_label': 'Todos los empleados'})
        self.filters['motivo'].extra.update({'empty_label': 'Todos los motivos'})




class AccidenteFilter(django_filters.FilterSet):
    fecha_accidente = DateFromToRangeFilter()
    class Meta:
        model = Accidente
        fields = ['empleado', 'fecha_accidente']

    def __init__(self, *args, **kwargs):
        super(AccidenteFilter, self).__init__(*args, **kwargs)
        self.filters['empleado'].extra.update({'empty_label': 'Todos los empleados'})



