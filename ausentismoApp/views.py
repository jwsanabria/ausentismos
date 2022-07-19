from django_tables2 import SingleTableView, LazyPaginator
from django_tables2.export import ExportMixin
from django_tables2.config import RequestConfig
from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from .tables import *
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
from django.db.models import ObjectDoesNotExist
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt


interes_tecnico = 0.004867


def postInsumo (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccInsumosMedicosForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize('json', [instance,])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)



def postOtros (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccOtrosForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize('json', [instance,])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

def postTransporte (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccTransporteForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize('json', [instance,])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)



def postMaquinaria (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccMaquinariaForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize('json', [instance,])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postRepuesto (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccRepuestoForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize('json', [instance,])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

def postManoObra (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccManoObraForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize('json', [instance,])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postDanoEmergente (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccDanoEmergenteForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize('json', [instance,])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


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
            id_accidente = request.GET['id_accidente']
            num_meses_exp = request.GET['lcf']
            accidente = get_object_or_404(Accidente, id=id_accidente)

            data = []
            fecha_liquidacion = datetime.strptime(fecha_liquidacion, "%d-%m-%Y")
            factor_ipc_final = 0.0
            factor_ipc_inicial = 0.0
            diferencia = relativedelta(fecha_liquidacion, accidente.fecha_accidente)
            num_meses_liq = diferencia.years * 12 + diferencia.months

            if num_meses_liq == 0:
                num_meses_liq = 1.0

            try:
                f_ipc_final = FactorIPC.objects.filter(anio=fecha_liquidacion.year).filter(mes=fecha_liquidacion.month).get()
                factor_ipc_final = f_ipc_final.factor
                f_ipc_inicial = FactorIPC.objects.filter(anio=accidente.fecha_accidente.year).filter(mes=accidente.fecha_accidente.month).get()
                factor_ipc_inicial = f_ipc_inicial.factor
            except ObjectDoesNotExist:
                pass

            ingreso_base = accidente.empleado.salario + (accidente.empleado.salario * 25 / 100)
            valor_actualizado = ingreso_base - (ingreso_base * 25 / 100)
            valor_presente = 0
            renta_actualizada = 0
            lucro_cesante_consolidado = 0
            lucro_cesante_futuro = 0


            valor_presente = valor_actualizado * (factor_ipc_final / factor_ipc_inicial)

            if accidente.fallecido:
                renta_actualizada = valor_presente
            else:
                renta_actualizada = valor_presente * accidente.grado_invalidez


            lucro_cesante_consolidado = renta_actualizada * ((Decimal(1.0) + Decimal(interes_tecnico)) ** (Decimal(num_meses_liq) - Decimal(1.0)) / Decimal(interes_tecnico))

            lucro_cesante_futuro = renta_actualizada * ((Decimal(1.0) + Decimal(interes_tecnico)) ** Decimal(num_meses_exp) - Decimal(1.0)) / (Decimal(interes_tecnico) * (Decimal(1.0) + Decimal(interes_tecnico)) ** Decimal(num_meses_exp))

            item = {}
            item['ipc_final'] = factor_ipc_final
            item['ipc_inicial'] = factor_ipc_inicial
            item['lcc']= num_meses_liq
            item['lucro_cesante_consolidado']= lucro_cesante_consolidado
            item['lucro_cesante_futuro']= lucro_cesante_futuro

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



class LucroView(View):
    def get(self, request, pk):
        f_dano_emergente = CostosAccDanoEmergenteForm()
        accidente = get_object_or_404(Accidente, id= pk)

        salario = accidente.empleado.salario
        edad = relativedelta(datetime.now(), accidente.empleado.fecha_nacimiento)
        tiempo_expectativa = 0
        try:
            expectativa = ExpectativaVida.objects.filter(edad = edad.years).filter(tipo = accidente.empleado.sexo).get()
            tiempo_expectativa = expectativa.expectativa
        except ObjectDoesNotExist:
            pass

        estado = "LESIONADO"
        if accidente.fallecido :
            estado = "FALLECIDO"

        context_data = {"accidente": accidente,
                        'salario': salario,
                        'edad': edad,
                        'estado': estado,
                        'lcf': tiempo_expectativa * 12,
                        'interes_tecnico': interes_tecnico,
                        'expectativa': tiempo_expectativa + edad.years,
                        'f_dano_emergente': f_dano_emergente,
                        'f_danomaterial': DanoMaterialForm(),
                        'list_dano_emergente': CostosAccDanoEmergente.objects.filter(accidente=pk)}


        return render(request, 'accidentes/lucro.html', context_data)



class AprociacionesView(View):
    def get(self, request, pk):
        f_dano_emergente = CostosAccDanoEmergenteForm()
        accidente = get_object_or_404(Accidente, id= pk)

        salario = accidente.empleado.salario
        edad = relativedelta(datetime.now(), accidente.empleado.fecha_nacimiento)
        tiempo_expectativa = 0
        try:
            expectativa = ExpectativaVida.objects.filter(edad = edad.years).filter(tipo = accidente.empleado.sexo).get()
            tiempo_expectativa = expectativa.expectativa
        except ObjectDoesNotExist:
            pass

        estado = "LESIONADO"
        if accidente.fallecido :
            estado = "FALLECIDO"

        context_data = {"accidente": accidente,
                        'salario': salario,
                        'edad': edad,
                        'estado': estado,
                        'lcf': tiempo_expectativa * 12,
                        'interes_tecnico': interes_tecnico,
                        'expectativa': tiempo_expectativa + edad.years,
                        'f_dano_emergente': f_dano_emergente,
                        'f_danomaterial': DanoMaterialForm(),
                        'list_dano_emergente': CostosAccDanoEmergente.objects.filter(accidente=pk)}


        return render(request, 'accidentes/apropiaciones.html', context_data)


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