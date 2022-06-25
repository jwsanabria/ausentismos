from django_tables2 import SingleTableView
from django.shortcuts import render, HttpResponse
from .models import Persona, Ausentismo
from .forms import AusentismoForm
from .tables import PersonaTable
from django.views.generic.base import View
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegistrarAusentismoView(CreateView):
    model = Ausentismo
    form_class = AusentismoForm
    template_name = "ausentismos/add.html"
    success_url = reverse_lazy("ausentismo")

# Create your views here.
class PersonaListView(SingleTableView):
    model = Persona
    table_class = PersonaTable
    template_name = 'personas/infoPersonal.html'


class PersonaView(View):
    def get(self, request, pk):
        context_data = {"persona": Persona.objects.get(id=pk)}
        return render(request, 'personal/infoPersonal.html', context_data)


def home(request):
    return render(request, "index.html")

def ausentismos(request):
    context_data = {"ausentismos": Ausentismo.objects.all()}
    return render(request, "ausentismos/index.html", context_data)

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
