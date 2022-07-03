import django_tables2 as tables
from .models import Persona, Ausentismo
import itertools

class CurrencyColumn(tables.Column):
    def render(self, value):
        return '${:,.2f}'.format(value)



class PersonaTable(tables.Table):
    template = '''<a href="{{record.get_absolute_url}}" ">detalle</a>'''
    persona_detalle = tables.TemplateColumn(
        template,
        verbose_name=u'Ver detalle',
        orderable=False,
    )
    salario = CurrencyColumn()
    fecha_ingreso = tables.DateColumn(format='d-m-Y')
    class Meta:
        model = Persona
        attrs = {'id': 'history_table'}
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("id", "tipo_documento", "documento", "nombre", "area", "seccion", "cargo", "estado", "fecha_ingreso" )
        sequence = ('id', 'tipo_documento', 'documento', 'nombre', 'fecha_ingreso', 'area', 'seccion', 'cargo', 'salario', 'estado', 'persona_detalle')


class AusentismoTable(tables.Table):
    salario = tables.Column(accessor='empleado.salario')
    class Meta:
        model = Ausentismo
        row_attrs = {
            "data-id": lambda record: record.id
        }
        attrs = {'id': 'history_table', 'class': 'table table-striped table-hover'}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "empleado", "motivo", "fecha_solicitud", "fecha_ausentismo", "hora_inicial", "hora_final", "tiempo_ausentismo" )
        sequence = ('id', 'empleado', 'motivo', 'fecha_solicitud', 'fecha_ausentismo', 'hora_inicial', 'hora_final', 'tiempo_ausentismo', 'salario')

