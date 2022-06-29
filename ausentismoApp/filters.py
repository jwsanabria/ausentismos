import django_filters
from .models import Ausentismo

class AusentismoFilter(django_filters.FilterSet):
    class Meta:
        model = Ausentismo
        fields = ['empleado', 'motivo']