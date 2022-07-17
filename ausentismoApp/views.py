from django_tables2 import SingleTableView, LazyPaginator
from django_tables2.export import ExportMixin
from django_tables2.config import RequestConfig
from django.shortcuts import render, HttpResponse
from .models import Persona, Ausentismo, Accidente, CostosAccInsumosMedicos, CostosAccTransporte, CostosAccOtros, CostosAccRepuestos, CostosAccManoObra, CostosAccMaquinaria
from .forms import AusentismoForm, AccidenteForm, CostosAccInsumosMedicosForm, CostosAccTransporteForm, CostosAccOtrosForm, CostosAccManoObraForm, CostosAccRepuestoForm, CostosAccMaquinariaForm, DanoMaterialForm
from .tables import PersonaTable, AusentismoTable, AccidenteTable
from django.views.generic.base import View
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import AusentismoFilter, AccidenteFilter
from django.shortcuts import get_object_or_404
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt


class BuscarPersonaView(View):
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']

            if action == 'autocomplete':
                data = {}
                for i in Persona.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.personaToDictionary()
                    item['text'] = i.__str__()
                    item['id'] = i.id
                    data = {'data': item}
        except Exception as e:
            data['error']: str(e)

        return JsonResponse(data, safe=False)


class LiquidacionView(View):
    def get(self, request):
        data = {}
        try:
            fecha_liquidacion = request.GET['fecha_liquidacion']

            data = []
            fecha_liquidacion = datetime.strptime(fecha_liquidacion, "%d-%m-%Y")
            item = {}
            item['ipc_final'] = 8.79
            item['ipc_inicial'] = 7.3
            data.append(item)
        except Exception as e:
            data['error']: str(e)

        return JsonResponse(data, safe=False)

class RegistrarAusentismoView(CreateView):
    model = Ausentismo
    form_class = AusentismoForm
    template_name = "ausentismos/add.html"
    success_url = reverse_lazy("ausentismo")

class RegistrarAccidenteView(CreateView):
    model = Accidente
    form_class = AccidenteForm
    template_name = "accidentes/add.html"
    success_message = "Accdiente creado exitosamente"
    success_url = reverse_lazy("accidentes")



# Create your views here.
class PersonaListView(SingleTableView):
    model = Persona
    table_class = PersonaTable
    template_name = 'personas/infoPersonal.html'


class FilteredAccidenteListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = AccidenteTable
    model = Accidente
    template_name = "accidentes/index.html"
    paginate_by = 20
    filterset_class = AccidenteFilter

class FilteredAusentismoListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = AusentismoTable
    model = Ausentismo
    template_name = "ausentismos/index2.html"
    paginate_by = 20
    filterset_class = AusentismoFilter

'''
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
        
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, query)
            return exporter.response("query.{}".format(export_format))
        
        return context
'''

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


class CostosView(View):
    def get(self, request, pk):
        accidente = get_object_or_404(Accidente, id= pk)
        f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})
        f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})
        f_otros = CostosAccOtrosForm(initial={"accidente": accidente})
        f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})
        f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})
        f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

        context_data = {"accidente": accidente,
                        'f_insumos': f_insumos,
                        'f_transporte': f_transporte,
                        'f_otros': f_otros,
                        'f_maquinaria': f_maquinaria,
                        'f_manoObra': f_manoObra,
                        'f_repuesto': f_repuesto,
                        "listInsumosMed": CostosAccInsumosMedicos.objects.filter(accidente=pk),
                        "listTransporte": CostosAccTransporte.objects.filter(accidente=pk),
                        "listOtros": CostosAccOtros.objects.filter(accidente=pk),
                        "listMaquinaria": CostosAccMaquinaria.objects.filter(accidente=pk),
                        "listRepuestos": CostosAccRepuestos.objects.filter(accidente=pk),
                        "listManoObra": CostosAccManoObra.objects.filter(accidente=pk)}
        return render(request, 'accidentes/documentar.html', context_data)

    def post(self, request, *args, **kwargs):
        accidente = get_object_or_404(Accidente, id=kwargs['pk'])
        if 'nuevo_insumo' in request.POST:
            f_insumos = CostosAccInsumosMedicosForm(request.POST)
            f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})
            f_otros = CostosAccOtrosForm(initial={"accidente": accidente})
            f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})
            f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})
            f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

            f_insumos.instance.accidente = accidente
            if f_insumos.is_valid():
                f_insumos.save()
                f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})

        if 'nuevo_transporte' in request.POST:
            f_transporte = CostosAccTransporteForm(request.POST)
            f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})
            f_otros = CostosAccOtrosForm(initial={"accidente": accidente})
            f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})
            f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})
            f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

            f_transporte.instance.accidente = accidente
            if f_transporte.is_valid():
                f_transporte.save()
                f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})


        if 'nuevo_otros' in request.POST:
            f_otros = CostosAccOtrosForm(request.POST)
            f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})
            f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})
            f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})
            f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})
            f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

            f_otros.instance.accidente = accidente
            if f_otros.is_valid():
                f_otros.save()
                f_otros = CostosAccOtrosForm(initial={"accidente": accidente})


        if 'nuevo_maquinaria' in request.POST:
            f_maquinaria = CostosAccMaquinariaForm(request.POST)
            f_otros = CostosAccOtrosForm(initial={"accidente": accidente})
            f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})
            f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})
            f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})
            f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

            f_maquinaria.instance.accidente = accidente
            if f_otros.is_valid():
                f_otros.save()
                f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})

        if 'nuevo_repuesto' in request.POST:
            f_repuesto = CostosAccRepuestoForm(request.POST)
            f_otros = CostosAccOtrosForm(initial={"accidente": accidente})
            f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})
            f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})
            f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})
            f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

            f_repuesto.instance.accidente = accidente
            if f_otros.is_valid():
                f_otros.save()
                f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})

        if 'nuevo_manoObra' in request.POST:
            f_manoObra = CostosAccManoObraForm(request.POST)
            f_otros = CostosAccOtrosForm(initial={"accidente": accidente})
            f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})
            f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})
            f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})
            f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})

            f_manoObra.instance.accidente = accidente
            if f_otros.is_valid():
                f_otros.save()
                f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

        context_data = {"accidente": accidente,
                        'f_insumos': f_insumos,
                        'f_transporte': f_transporte,
                        'f_otros': f_otros,
                        'f_maquinaria': f_maquinaria,
                        'f_manoObra': f_manoObra,
                        'f_repuesto': f_repuesto,
                        "listInsumosMed": CostosAccInsumosMedicos.objects.filter(accidente=accidente.id),
                        "listTransporte": CostosAccTransporte.objects.filter(accidente=accidente.id),
                        "listOtros": CostosAccOtros.objects.filter(accidente=accidente.id),
                        "listMaquinaria": CostosAccMaquinaria.objects.filter(accidente=accidente.id),
                        "listRepuestos": CostosAccRepuestos.objects.filter(accidente=accidente.id),
                        "listManoObra": CostosAccManoObra.objects.filter(accidente=accidente.id)}

        return render(request, 'accidentes/documentar.html', context_data)


class LucroView(View):
    def get(self, request, pk):
        accidente = get_object_or_404(Accidente, id= pk)
        salario = accidente.empleado.salario
        edad = relativedelta(datetime.now(), accidente.empleado.fecha_nacimiento)
        estado = "LESIONADO"
        if accidente.fallecido :
            estado = "FALLECIDO"

        context_data = {"accidente": accidente,
                        'salario': salario,
                        'edad': edad,
                        'estado': estado,
                        'f_danomaterial': DanoMaterialForm()}


        return render(request, 'accidentes/lucro.html', context_data)



class CostosNuevosView(CreateView):
    model = CostosAccInsumosMedicos
    template_name = "accidentes/costo_insumos_med.html"
    form_class = CostosAccInsumosMedicosForm

    def get_context_data(self, **kwargs):
        context = super(CostosNuevosView, self).get_context_data(**kwargs)
        context['acc'] = self.kwargs['acc']
        return context

    def form_valid(self, form):
        form.instance.accidente = Accidente.objects.get(pk=self.kwargs['acc'])
        context = {'acc': self.kwargs['acc']}
        self.success_url = reverse_lazy("costos_list", kwargs={'pk': self.kwargs['acc']})
        return super(CostosNuevosView, self).form_valid(form)


class CostosEditView(UpdateView):
    model = CostosAccInsumosMedicos
    template_name = "catalogos/subcategoria_form.html"
    context_object_name = 'obj'
    form_class = CostosAccInsumosMedicosForm
    success_url = reverse_lazy("ausentismo:costos_list")