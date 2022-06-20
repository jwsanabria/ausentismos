from django_tables2 import SingleTableView
from django.shortcuts import render, HttpResponse
from .models import Persona
from .tables import PersonaTable

# Create your views here.
class PersonaListView(SingleTableView):
    model = Persona
    table_class = PersonaTable
    template_name = 'personas/'


def home(request):
    return render(request, "index.html")

def ausentismos(request):
    return render(request, "ausentismos/index.html")

def informes(request):
    return render(request, "informes/index.html")

def accidentes(request):
    return render(request, "accidentes/index.html")

def personal(request):
    personas = PersonaTable(Persona.objects.all())
    personas.paginate(page=request.GET.get("page", 1), per_page=25)
    context = {
        "personas": personas
    }

    return render(request, 'personal/index.html', context)
