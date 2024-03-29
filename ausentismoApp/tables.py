import django_tables2 as tables
from .models import Persona, Ausentismo, Accidente
from decimal import Decimal
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
    #salario = CurrencyColumn(accessor='empleado.salario')
    #costo = tables.Column(verbose_name='Costo', empty_values=())
    fecha_ausentismo = tables.DateColumn(format='d-m-Y')

    def render_valor_ausentismo(self, record):
        return '${:,.2f}'.format(record.valor_ausentismo).replace(",", "@").replace(".", ",").replace("@", ".")

    def render_salario_ausentismo(self, record):
        return '${:,.2f}'.format(record.salario_ausentismo).replace(",", "@").replace(".", ",").replace("@", ".")

    class Meta:
        model = Ausentismo
        row_attrs = {
            "data-id": lambda record: record.id
        }
        attrs = {'id': 'history_table', 'class': 'table table-striped table-hover'}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "empleado", "motivo", "fecha_ausentismo", "horas_ausentismo", "salario_ausentismo", "valor_ausentismo", "area", "seccion", "cargo", "sede" )
        sequence = ('id', 'empleado', 'sede', 'area', 'seccion', 'cargo', 'salario_ausentismo', 'fecha_ausentismo', 'horas_ausentismo',  'motivo', 'valor_ausentismo')


class AccidenteTable(tables.Table):
    template = '''<a href="{{record.get_detalle_url}}" class="btn btn-outline-info  btn-sm">Ver Detalle</a><a href="{{record.get_balance_url}}" class="btn btn-primary  btn-sm">Balance</a>'''
    botones_action = tables.TemplateColumn(
        template,
        verbose_name=u'Acciones',
        orderable=False,
    )

    class Meta:
        model = Accidente
        row_attrs = {
            "data-id": lambda record: record.id
        }
        attrs = {'id': 'history_table', 'class': 'table table-striped table-hover'}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "empleado", "fecha_accidente", "fallecido", 'botones_action' )
        sequence = ('id', 'empleado', 'fecha_accidente', 'fallecido', 'botones_action')

