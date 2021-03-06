from django_tables2 import SingleTableView, LazyPaginator
from django_tables2.export import ExportMixin
from django.db.models import Count, Sum
from django_tables2.config import RequestConfig
from django.http import HttpResponseRedirect
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
from django.db.models import F
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required


interes_tecnico = 0.004867


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def postAdicionales (request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccAdicionalesForm(request.POST)
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


def postCapacitador(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    capacitador = get_object_or_404(Persona, id=request.POST["capacitador"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CapacitacionAccForm(request.POST)
        form.instance.accidente = accidente
        form.instance.salario = capacitador.salario
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


def postReemplazo(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs['pk'])
    reemplazo = get_object_or_404(Persona, id=request.POST["reemplazo"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = ReemplazosAccForm(request.POST)
        form.instance.accidente = accidente
        form.instance.salario = reemplazo.salario
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
                data = []
                for i in Persona.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.personaToDictionary()
                    item['text'] = i.__str__()
                    item['id'] = i.id
                    data.append(item)
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

            accidente.fecha_liquidacion = fecha_liquidacion
            accidente.lucro_consolidado = lucro_cesante_consolidado
            accidente.lucro_futuro = lucro_cesante_futuro
            accidente.ipc_inicial = factor_ipc_inicial
            accidente.ipc_final = factor_ipc_final
            accidente.num_mes_lcc = num_meses_liq
            accidente.save()

            item = {}
            item['ipc_final'] = factor_ipc_final
            item['ipc_inicial'] = factor_ipc_inicial
            item['lcc']= num_meses_liq
            item['lucro_cesante_consolidado']= lucro_cesante_consolidado
            item['lucro_cesante_futuro']= lucro_cesante_futuro
            item['fecha_liq']=fecha_liquidacion

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

@login_required()
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
        f_tiempos_acompanamiento = TiemposAccAcompanamientoForm()
        accidente = get_object_or_404(Accidente, id= pk)

        matrix = []

        result = TiemposAccAcompanamiento.objects.filter(accidente=pk).values('tipo_acompanamiento').order_by('tipo_acompanamiento').annotate(dTotal=Sum('total'))
        tipos_acompanamiento = TipoAcompanamiento.objects.all().order_by('id')
        factor_parafiscales = FactorAccParafiscales.objects.all().order_by('id')
        for parafiscal in factor_parafiscales:
            fila = []
            fila.append(parafiscal.descripcion)
            for tipo in tipos_acompanamiento:
                valor = 0;
                for r in result.iterator():
                    if tipo.id == r['tipo_acompanamiento']:
                        valor = parafiscal.factor*r['dTotal']
                fila.append(valor)
            matrix.append(fila)




        context_data = {"accidente": accidente,
                        'f_tiempos_acompanamiento': f_tiempos_acompanamiento,
                        'list_acompanamientos': TiemposAccAcompanamiento.objects.filter(accidente=pk),
                        'matrix': matrix, 'factor_parafiscal': factor_parafiscales, 'tipos_acompanamiento': tipos_acompanamiento}

        return render(request, 'accidentes/apropiaciones.html', context_data)

    def post(selft, request, *args, **kwargs):
        accidente = get_object_or_404(Accidente, id=kwargs['pk'])
        form = TiemposAccAcompanamientoForm(request.POST)
        acompanante = get_object_or_404(Persona, id=request.POST["empleado"])
        factor = get_object_or_404(FactorTiemposAcompanamiento, id=request.POST["factor"])
        form.instance.salario = acompanante.salario
        form.instance.valor_diario = acompanante.salario / 30
        form.instance.valor_factor = factor.factor
        form.instance.total = ((acompanante.salario / 30) * factor.factor) * 1

        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect(reverse('apropiaciones_nomina', kwargs={'pk':instance.accidente.id}) )

        # some error occured
        return HttpResponseRedirect(reverse('apropiaciones_nomina', kwargs={'pk':kwargs['pk']}))


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


class AdaptacionCambioView(View):
    def get(self, request, pk):
        accidente = get_object_or_404(Accidente, id=pk)
        f_reemplazo = ReemplazosAccForm()
        f_capacitador = CapacitacionAccForm()
        f_costos_adicionales = CostosAccAdicionalesForm()

        context_data = {"accidente": accidente,
                    'f_reemplazo': f_reemplazo,
                    'f_capacitador': f_capacitador,
                    'f_costos_adicionales': f_costos_adicionales,
                    'list_reemplazos': ReemplazoAccidente.objects.filter(accidente=pk),
                    'list_capacitadores': CapacitadorAccidente.objects.filter(accidente=pk),
                    'list_costos': CostosAccAdicionales.objects.filter(accidente=pk), }

        return render(request, 'accidentes/adaptacion_cambio.html', context_data)


class BalanceView(View):
    def get(self, request, pk):
        accidente = get_object_or_404(Accidente, id=pk)

        valor_1 = 0;
        valor_2 = 0;
        valor_3 = 0;
        valor_4 = 0;
        valor_5 = 0;
        valor_6 = 0;
        valor_7 = 0;
        valor_8 = 0;
        valor_9 = 0;
        valor_10 = 0;
        valor_11 = 0;
        valor_12 = 0;
        valor_13 = 0;
        valor_14 = 0;
        valor_15 = 0;
        valor_16 = 0;

        result = TiemposAccAcompanamiento.objects.filter(accidente=accidente.id).values('tipo_acompanamiento').order_by('tipo_acompanamiento').annotate(dTotal=Sum('total'))

        for r in result.iterator():
            if 1 == r['tipo_acompanamiento']:
                valor_2 = r['dTotal']
            elif 2 == r['tipo_acompanamiento']:
                valor_9 = r['dTotal']
            elif 3 == r['tipo_acompanamiento']:
                valor_10 = r['dTotal']
            elif 4 == r['tipo_acompanamiento']:
                valor_11 = r['dTotal']
            elif 5 == r['tipo_acompanamiento']:
                valor_12 = r['dTotal']

        tiempo_dic = {}
        result = TiemposAccAcompanamiento.objects.filter(accidente=accidente.id).order_by('tipo_acompanamiento')

        for r in result:
            if tiempo_dic.get(r.tipo_acompanamiento.id) is None:
                tiempo_dic[r.tipo_acompanamiento.id]= r.tiempo.hour * 60 + r.tiempo.minute
            else:
                tiempo_dic[r.tipo_acompanamiento.id] = tiempo_dic[r.tipo_acompanamiento.id] + (r.tiempo.hour * 60 + r.tiempo.minute)

        valor_1 = calcular_tiempo(tiempo_dic, 1)
        valor_5 = calcular_tiempo(tiempo_dic, 2)
        valor_6 = calcular_tiempo(tiempo_dic, 3)
        valor_7 = calcular_tiempo(tiempo_dic, 4)
        valor_8 = calcular_tiempo(tiempo_dic, 5)


        result = CostosAccInsumosMedicos.objects.filter(accidente= accidente.id).aggregate(total = Sum(F('valor')*F('cantidad')))['total']
        if result is not None: valor_3 = valor_3 + result
        result = CostosAccTransporte.objects.filter(accidente= accidente.id).aggregate(total=Sum(F('valor')))['total']
        if result is not None: valor_3 = valor_3 +  result
        result = CostosAccOtros.objects.filter(accidente=accidente.id).aggregate(total=Sum(F('valor')))['total']
        if result is not None: valor_3 = valor_3 + result

        result = CostosAccDanoEmergente.objects.filter(accidente= accidente.id).aggregate(total=Sum(F('valor')))['total']
        if result is not None: valor_4 = valor_4 + result

        result = CostosAccMaquinaria.objects.filter(accidente= accidente.id).aggregate(total = Sum(F('valor')*F('cantidad')))['total']
        if result is not None: valor_14 = valor_14 + result

        result = CostosAccRepuestos.objects.filter(accidente=accidente.id).aggregate(total=Sum(F('valor') * F('cantidad')))['total']
        if result is not None: valor_15 = valor_15 + result

        result = CostosAccManoObra.objects.filter(accidente=accidente.id).aggregate(total=Sum(F('valor') * F('cantidad')))['total']
        if result is not None: valor_16 = valor_16 + result

        context_data = {"accidente": accidente,
                        'valor_1': valor_1,
                        'valor_2': valor_2,
                        'valor_3': valor_3,
                        'valor_4': valor_4,
                        'valor_5': valor_5,
                        'valor_6': valor_6,
                        'valor_7': valor_7,
                        'valor_8': valor_8,
                        'valor_9': valor_9,
                        'valor_10': valor_10,
                        'valor_11': valor_11,
                        'valor_12': valor_12,
                        'valor_13': valor_13,
                        'valor_14': valor_14,
                        'valor_15': valor_15,
                        'valor_16': valor_16,
                     }

        return render(request, 'accidentes/balance.html', context_data)



def calcular_tiempo(dic, indice):
    if dic.get(indice) is None:
        return "00:00"
    else:
        return str(int(dic.get(indice) / 60)) + ":" + str(int(dic.get(indice) % 60))