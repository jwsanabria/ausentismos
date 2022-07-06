from django_tables2 import SingleTableView, LazyPaginator
from django_tables2.export import ExportMixin
from django_tables2.config import RequestConfig
from django.shortcuts import render, HttpResponse
from .models import Persona, Ausentismo
from .forms import AusentismoForm
from .tables import PersonaTable, AusentismoTable
from django.views.generic.base import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import AusentismoFilter
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt


class BuscarPersonaView(View):
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']

            if action == 'autocomplete':
                data = []
                for i in Persona.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.personaToDictionary()
                    item['text'] = i.__str__()
                    item['id'] = i.id
                    data.append(item)
        except Exception as e:
            data['error']: str(e)

        return JsonResponse(data, safe=False)


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


class FilteredAusentismoListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = AusentismoTable
    model = Ausentismo
    template_name = "ausentismos/index2.html"
    paginate_by = 5
    filterset_class = AusentismoFilter

    def get_context_data(self, **kwargs):
        context = super(FilteredAusentismoListView, self).get_context_data(**kwargs)
        if('fecha' in self.kwargs):
            print('FECHA ' + self.kwargs['fecha'])
            query = Ausentismo.objects.all().select_related('empleado')
        else:
            query = Ausentismo.objects.all().select_related('empleado')

        f = AusentismoFilter(self.request.GET, queryset=query)

        t = AusentismoTable(data=f.qs)
        t.paginate(page=self.request.GET.get("page", 1), per_page=5)

        RequestConfig(self.request, paginate=False).configure(t)

        context['filter'] = f
        context['table'] = t
        
        export_format = self.request.GET.get("_export", None)
        '''
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, query)
            return exporter.response("query.{}".format(export_format))
        '''
        return context


class PersonaView(View):
    def get(self, request, pk):
        context_data = {"persona": Persona.objects.get(id=pk)}
        return render(request, 'personal/infoPersonal.html', context_data)


def home(request):
    return render(request, "index.html")


def ausentismos(request):
    #context_data = {"ausentismos": Ausentismo.objects.all()}
    #return render(request, "ausentismos/index.html", context_data)
    table = AusentismoTable(Ausentismo.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=5)
    return render(request, "ausentismos/index.html", {"ausentismos": table})


def informes(request):
    return render(request, "informes/index.html")


def accidentes(request):
    return render(request, "accidentes/index.html")


def personal(request):
    personas = PersonaTable(Persona.objects.all())
    personas.paginate(page=request.GET.get("page", 1), per_page=5)
    context = {
        "personas": personas
    }

    return render(request, 'personal/index.html', context)
