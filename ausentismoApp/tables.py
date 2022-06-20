import django_tables2 as tables
from .models import Persona
import itertools

class PersonaTable(tables.Table):
    class Meta:
        model = Persona
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("tipo_documento", "documento", "nombre", "area", "seccion", "cargo", "salario", "estado" )
