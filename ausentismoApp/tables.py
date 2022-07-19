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
    salario = CurrencyColumn(accessor='empleado.salario')
    area = tables.Column(accessor='empleado.area')
    seccion = tables.Column(accessor='empleado.seccion')
    cargo = tables.Column(accessor='empleado.cargo')
    costo = tables.Column(verbose_name='Costo', empty_values=())

    def render_costo(self, record):
        return '${:,.2f}'.format(record.empleado.salario/240 * Decimal(record.tiempo_ausentismo.hour + record.tiempo_ausentismo.minute/60))

    class Meta:
        model = Ausentismo
        row_attrs = {
            "data-id": lambda record: record.id
        }
        attrs = {'id': 'history_table', 'class': 'table table-striped table-hover'}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "empleado", "motivo", "fecha_ausentismo", "hora_inicial", "hora_final", "tiempo_ausentismo" )
        sequence = ('id', 'empleado', 'area', 'seccion', 'cargo', 'salario', 'fecha_ausentismo', 'tiempo_ausentismo', 'hora_inicial', 'hora_final', 'motivo', 'costo')


class AccidenteTable(tables.Table):
    template = '''<a href="{{record.get_documentar_url}}" class="btn btn-outline-info  btn-sm">Documentar</a><a href="{{record.get_lucro_url}}" class="btn btn-outline-info  btn-sm">Lucro</a><a href="{{record.get_documentar_url}}"   class="btn btn-outline-info btn-sm">Adaptación al cambio</a><a href="{{record.get_nomina_url}}" class="btn btn-secondary  btn-sm">Apropiaciones Nómina</a><a href="{{record.get_documentar_url}}" class="btn btn-primary  btn-sm">Balance</a>'''
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

