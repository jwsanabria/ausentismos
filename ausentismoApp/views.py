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
import json
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)

interes_tecnico = 0.004867


def page_not_found_view(request, exception):
    return render(request, "404.html", status=404)


def post_guardar_ausentismo(request, *args, **kwargs):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        form = AusentismoForm(request.POST)
        # get the form data
        try:
            empleado = get_object_or_404(Persona, id=request.POST["empleado"])
            tiempo = request.POST["tiempo_ausentismo"]
            periodo = request.POST["periodo_ausentismo"]
            form.instance.horas_ausentismo = 0

            if periodo == "D":
                form.instance.horas_ausentismo = int(tiempo) * 8
            else:
                form.instance.horas_ausentismo = int(tiempo)

            form.instance.valor_ausentismo = Decimal(
                empleado.salario / 240 * Decimal(form.instance.horas_ausentismo)
            ) * Decimal(1.5568)
            form.instance.salario_ausentismo = empleado.salario
            form.instance.cargo = empleado.cargo.descripcion
            form.instance.seccion = empleado.seccion.descripcion
            form.instance.area = empleado.area.descripcion
            form.instance.sede = empleado.sede.descripcion
            instance = form.save()
            instance.nombre_empleado = empleado.nombre

            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                    empleado,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)

        except Exception as e:
            # some form errors occured.
            return JsonResponse({"error": e.__str__()}, status=400)

    # some error occured
    return JsonResponse(
        {"error": "Se presento un error al calcular el valor del ausentismo"},
        status=400,
    )


def post_remove_row(request, *args, **kwargs):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        try:
            tipo = request.POST["tipo"]
            if tipo == "I":
                model = get_object_or_404(
                    CostosAccInsumosMedicos, id=request.POST["id"]
                )

            elif tipo == "T":
                model = get_object_or_404(CostosAccTransporte, id=request.POST["id"])

            elif tipo == "O":
                model = get_object_or_404(CostosAccOtros, id=request.POST["id"])

            elif tipo == "M":
                model = get_object_or_404(CostosAccMaquinaria, id=request.POST["id"])

            elif tipo == "R":
                model = get_object_or_404(CostosAccRepuestos, id=request.POST["id"])

            elif tipo == "B":
                model = get_object_or_404(CostosAccManoObra, id=request.POST["id"])

            elif tipo == "E":
                model = get_object_or_404(CostosAccDanoEmergente, id=request.POST["id"])

            elif tipo == "S":
                model = get_object_or_404(ReemplazoAccidente, id=request.POST["id"])

            elif tipo == "C":
                model = get_object_or_404(CapacitadorAccidente, id=request.POST["id"])

            elif tipo == "A":
                model = get_object_or_404(CostosAccAdicionales, id=request.POST["id"])

            elif tipo == "P":
                model = get_object_or_404(
                    TiemposAccAcompanamiento, id=request.POST["id"]
                )

            model.delete()
            # send to client side.
            ser_instance = serializers.serialize(
                "json",
                [
                    model,
                ],
            )
            return JsonResponse({"instance": ser_instance}, status=200)
        except:
            # some form errors occured.
            return JsonResponse(
                {"error": "Se presento un error al eliminar la fila"}, status=400
            )

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def post_remove_acompanamiento(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        try:
            model = get_object_or_404(TiemposAccAcompanamiento, id=request.POST["id"])

            model.delete()

            matrix = []

            result = (
                TiemposAccAcompanamiento.objects.filter(accidente=accidente.id)
                .values("tipo_acompanamiento")
                .order_by("tipo_acompanamiento")
                .annotate(dTotal=Sum("total"))
            )
            tipos_acompanamiento = TipoAcompanamiento.objects.all().order_by("id")
            factor_parafiscales = FactorAccParafiscales.objects.all().order_by("id")
            for parafiscal in factor_parafiscales:
                fila = []
                fila.append(parafiscal.descripcion)
                for tipo in tipos_acompanamiento:
                    valor = 0
                    for r in result.iterator():
                        if tipo.id == r["tipo_acompanamiento"]:
                            valor = parafiscal.factor * r["dTotal"]
                    fila.append(valor)
                matrix.append(fila)

            # send to client side.
            ser_instance = json.dumps(matrix, cls=DecimalEncoder)
            return JsonResponse({"instance": ser_instance}, status=200)
        except Exception:
            # some form errors occured.
            return JsonResponse(
                {"error": "Se presento un error al eliminar la fila"}, status=400
            )

    # some error occured
    return JsonResponse({"error": ""}, status=400)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


def post_dano_moral(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = DanoMoralForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            if request.POST["nivel"] == "N1":
                accidente.valor_moral_n1 = request.POST["cantidad"]
            elif request.POST["nivel"] == "N2":
                accidente.valor_moral_n2 = request.POST["cantidad"]
            elif request.POST["nivel"] == "N3":
                accidente.valor_moral_n3 = request.POST["cantidad"]
            elif request.POST["nivel"] == "N4":
                accidente.valor_moral_n4 = request.POST["cantidad"]
            elif request.POST["nivel"] == "N5":
                accidente.valor_moral_n5 = request.POST["cantidad"]

            valor_dano = Decimal(0.0)
            valor_dano = valor_dano + (
                Decimal(accidente.valor_moral_n1)
                * Decimal(accidente.salario_minimo)
                * Decimal(accidente.factor_moral_n1)
            )
            valor_dano = valor_dano + (
                Decimal(accidente.valor_moral_n2)
                * Decimal(accidente.salario_minimo)
                * Decimal(accidente.factor_moral_n2)
            )
            valor_dano = valor_dano + (
                Decimal(accidente.valor_moral_n3)
                * Decimal(accidente.salario_minimo)
                * Decimal(accidente.factor_moral_n3)
            )
            valor_dano = valor_dano + (
                Decimal(accidente.valor_moral_n4)
                * Decimal(accidente.salario_minimo)
                * Decimal(accidente.factor_moral_n4)
            )
            valor_dano = valor_dano + (
                Decimal(accidente.valor_moral_n5)
                * Decimal(accidente.salario_minimo)
                * Decimal(accidente.factor_moral_n5)
            )
            accidente.valor_dano_moral = valor_dano
            accidente.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    accidente,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def post_adicionales(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccAdicionalesForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def post_capacitador(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
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
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                    capacitador,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postReemplazo(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    reemplazo = Persona()
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = ReemplazosAccForm(request.POST)
        form.instance.accidente = accidente

        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save(commit=False)
            instance.nombre_reemplazo = form.instance.nombre_reemplazo
            instance.save()
            reemplazo.nombre = instance.nombre_reemplazo
            form.cleaned_data["reemplazo"]
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                    reemplazo,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            print(form.errors)
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def post_insumo(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccInsumosMedicosForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def post_otros(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccOtrosForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postTransporte(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccTransporteForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postMaquinaria(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccMaquinariaForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postRepuesto(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccRepuestoForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postManoObra(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccManoObraForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def postDanoEmergente(request, *args, **kwargs):
    accidente = get_object_or_404(Accidente, id=kwargs["pk"])
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CostosAccDanoEmergenteForm(request.POST)
        form.instance.accidente = accidente
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize an object in json
            ser_instance = serializers.serialize(
                "json",
                [
                    instance,
                ],
            )
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
            action = request.POST["action"]

            if action == "autocomplete":
                data = []
                for i in Persona.objects.filter(nombre__icontains=request.POST["term"]):
                    item = i.personaToDictionary()
                    item["text"] = i.__str__()
                    item["id"] = i.id
                    data.append(item)
        except Exception as e:
            data["error"]: str(e)

        return JsonResponse(data, safe=False)


class LiquidacionView(View):
    def get(self, request):
        data = []
        try:
            parametro = get_object_or_404(ParametrosApp, parametro="SMLV")
            smlv = float(parametro.valor)
            fecha_liquidacion = datetime.strptime(
                request.GET["fecha_liquidacion"], "%d-%m-%Y"
            )
            id_accidente = request.GET["id_accidente"]
            num_meses_exp = Decimal(request.GET["lcf"])
            accidente = get_object_or_404(Accidente, id=id_accidente)

            factor_ipc_final = 0.0
            factor_ipc_inicial = 0.0

            diferencia = fecha_liquidacion.date() - accidente.fecha_accidente
            logger.info(
                "MESES A LIQuIDAR: "
                + str(diferencia.days)
                + "|"
                + str(fecha_liquidacion)
                + "|"
                + str(accidente.fecha_accidente)
            )
            num_meses_liq = (diferencia.days + 1) / 30

            if num_meses_liq < 0:
                raise Exception(
                    "La fecha de liquidación es inferior a la fecha del accidente"
                )

            if num_meses_liq == 0:
                num_meses_liq = 1.0

            num_meses_exp -= Decimal(num_meses_liq)

            try:
                f_ipc_final = (
                    FactorIPC.objects.filter(anio=fecha_liquidacion.year)
                    .filter(mes=fecha_liquidacion.month)
                    .get()
                )
                factor_ipc_final = f_ipc_final.factor
                f_ipc_inicial = (
                    FactorIPC.objects.filter(anio=accidente.fecha_accidente.year)
                    .filter(mes=accidente.fecha_accidente.month)
                    .get()
                )
                factor_ipc_inicial = f_ipc_inicial.factor
            except ObjectDoesNotExist as e:
                logger.error(e)
                raise Exception(
                    "Falta información de IPC para las fechas seleccionadas"
                )

            try:
                ingreso_base = Decimal(accidente.salario_accidentado) * (
                    Decimal(factor_ipc_final) / Decimal(factor_ipc_inicial)
                )
            except:
                ingreso_base = Decimal(smlv)

            if ingreso_base is None or ingreso_base < smlv:
                ingreso_base = Decimal(smlv)

            valor_actualizado = 0
            lucro_cesante_consolidado = 0
            lucro_cesante_futuro = 0

            logger.info(factor_ipc_final)
            logger.info(factor_ipc_inicial)
            logger.info(ingreso_base)

            if (
                accidente.invalidez
                and accidente.grado_invalidez is not None
                and accidente.grado_invalidez > 0
                and accidente.grado_invalidez < 51
            ):
                valor_actualizado = ingreso_base + (ingreso_base * 25 / 100)
                valor_actualizado = Decimal(valor_actualizado) * Decimal(
                    accidente.grado_invalidez / 100
                )

                if valor_actualizado is None or valor_actualizado < smlv:
                    valor_actualizado = Decimal(smlv)

            elif (
                accidente.invalidez
                and accidente.grado_invalidez is not None
                and accidente.grado_invalidez > 50
            ):
                valor_actualizado = ingreso_base + (ingreso_base * 25 / 100)
            elif accidente.fallecido:
                valor_actualizado = ingreso_base + (ingreso_base * 25 / 100)
                valor_actualizado -= valor_actualizado * 25 / 100
            else:
                valor_actualizado = 0

            lucro_cesante_consolidado = valor_actualizado * (
                (
                    (
                        (Decimal(1.0) + Decimal(interes_tecnico))
                        ** Decimal(num_meses_liq)
                    )
                    - Decimal(1.0)
                )
                / Decimal(interes_tecnico)
            )

            lucro_cesante_futuro = valor_actualizado * (
                (
                    (
                        (Decimal(1.0) + Decimal(interes_tecnico))
                        ** Decimal(num_meses_exp)
                    )
                    - Decimal(1.0)
                )
                / (
                    Decimal(interes_tecnico)
                    * (
                        (Decimal(1.0) + Decimal(interes_tecnico))
                        ** Decimal(num_meses_exp)
                    )
                )
            )

            accidente.fecha_liquidacion = fecha_liquidacion
            accidente.lucro_consolidado = lucro_cesante_consolidado
            accidente.lucro_futuro = lucro_cesante_futuro
            accidente.ipc_inicial = factor_ipc_inicial
            accidente.ipc_final = factor_ipc_final
            accidente.num_mes_lcc = num_meses_liq
            accidente.save()

            item = {}
            item["ipc_final"] = factor_ipc_final
            item["ipc_inicial"] = factor_ipc_inicial
            item["lcc"] = num_meses_liq
            item["lucro_cesante_consolidado"] = lucro_cesante_consolidado
            item["lucro_cesante_futuro"] = lucro_cesante_futuro
            item["fecha_liq"] = fecha_liquidacion

            logger.info(item)
            data.append(item)
            return JsonResponse(data, safe=False, status=200)
        except Exception as e:
            logger.error(e)
            data.append({"error": str(e)})

        return JsonResponse(data, safe=False, status=400)


class RegistrarAusentismoView(View):
    def get(self, request):
        context_data = {"form": AusentismoForm()}
        return render(request, "ausentismos/add.html", context_data)


class RegistrarAccidenteView(CreateView):
    model = Accidente
    form_class = AccidenteForm
    template_name = "accidentes/add.html"
    success_message = "Accdiente creado exitosamente"
    success_url = reverse_lazy("accidentes")

    def form_valid(self, form):
        empleado = get_object_or_404(Persona, id=form.instance.empleado.id)
        parametro = get_object_or_404(ParametrosApp, parametro="SMLV")
        niveles = None
        if form.instance.fallecido == True:
            niveles = NivDanoMoral.objects.filter(tipo_dano="M")
        elif form.instance.invalidez == True:
            niveles = NivDanoMoral.objects.filter(
                tipo_dano="I",
                rango_inf__lte=form.instance.grado_invalidez,
                rango_sup__gte=form.instance.grado_invalidez,
            )

        if niveles is not None and niveles.count() > 0:
            for niv in niveles:
                if niv.nivel == 1:
                    form.instance.factor_moral_n1 = niv.valor
                elif niv.nivel == 2:
                    form.instance.factor_moral_n2 = niv.valor
                elif niv.nivel == 3:
                    form.instance.factor_moral_n3 = niv.valor
                elif niv.nivel == 4:
                    form.instance.factor_moral_n4 = niv.valor
                elif niv.nivel == 5:
                    form.instance.factor_moral_n5 = niv.valor
        else:
            form.instance.factor_moral_n1 = 0
            form.instance.factor_moral_n2 = 0
            form.instance.factor_moral_n3 = 0
            form.instance.factor_moral_n4 = 0
            form.instance.factor_moral_n5 = 0

        form.instance.salario_accidentado = empleado.salario
        form.instance.salario_minimo = float(parametro.valor)
        form.instance.valor_moral_n1 = 0
        form.instance.valor_moral_n2 = 0
        form.instance.valor_moral_n3 = 0
        form.instance.valor_moral_n4 = 0
        form.instance.valor_moral_n5 = 0
        form.instance.valor_dano_moral = 0

        return super().form_valid(form)


# Create your views here.
class PersonaListView(SingleTableView):
    model = Persona
    table_class = PersonaTable
    template_name = "personas/infoPersonal.html"


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


"""
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
"""


class DetalleAccidenteView(View):
    def get(self, request, pk):
        context_data = {"accidente": Accidente.objects.get(id=pk)}
        return render(request, "accidentes/detalle.html", context_data)


class PersonaView(View):
    def get(self, request, pk):
        context_data = {"persona": Persona.objects.get(id=pk)}
        return render(request, "personal/infoPersonal.html", context_data)


@login_required()
def home(request):
    return render(request, "index.html")


def ausentismos(request):
    # context_data = {"ausentismos": Ausentismo.objects.all()}
    # return render(request, "ausentismos/index.html", context_data)
    table = AusentismoTable(Ausentismo.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=5)
    return render(request, "ausentismos/index.html", {"ausentismos": table})


@login_required()
def informes(request):
    return render(request, "informes/index.html")


def accidentes(request):
    return render(request, "accidentes/index.html")


@login_required()
def personal(request):
    personas = PersonaTable(Persona.objects.all())
    personas.paginate(page=request.GET.get("page", 1), per_page=5)
    context = {"personas": personas}

    return render(request, "personal/index.html", context)


class CostosView(View):
    def get(self, request, pk):
        accidente = get_object_or_404(Accidente, id=pk)
        f_insumos = CostosAccInsumosMedicosForm(initial={"accidente": accidente})
        f_transporte = CostosAccTransporteForm(initial={"accidente": accidente})
        f_otros = CostosAccOtrosForm(initial={"accidente": accidente})
        f_maquinaria = CostosAccMaquinariaForm(initial={"accidente": accidente})
        f_repuesto = CostosAccRepuestoForm(initial={"accidente": accidente})
        f_manoObra = CostosAccManoObraForm(initial={"accidente": accidente})

        context_data = {
            "accidente": accidente,
            "f_insumos": f_insumos,
            "f_transporte": f_transporte,
            "f_otros": f_otros,
            "f_maquinaria": f_maquinaria,
            "f_manoObra": f_manoObra,
            "f_repuesto": f_repuesto,
            "listInsumosMed": CostosAccInsumosMedicos.objects.filter(accidente=pk),
            "listTransporte": CostosAccTransporte.objects.filter(accidente=pk),
            "listOtros": CostosAccOtros.objects.filter(accidente=pk),
            "listMaquinaria": CostosAccMaquinaria.objects.filter(accidente=pk),
            "listRepuestos": CostosAccRepuestos.objects.filter(accidente=pk),
            "listManoObra": CostosAccManoObra.objects.filter(accidente=pk),
        }
        return render(request, "accidentes/documentar.html", context_data)


class LucroView(View):
    def get(self, request, pk):
        f_dano_emergente = CostosAccDanoEmergenteForm()
        f_dano_moral = DanoMoralForm()
        accidente = get_object_or_404(Accidente, id=pk)
        parametro = get_object_or_404(ParametrosApp, parametro="SMLV")
        niveles = None
        if accidente.fallecido == True:
            niveles = NivDanoMoral.objects.filter(tipo_dano="M")
        elif accidente.invalidez == True:
            niveles = NivDanoMoral.objects.filter(
                tipo_dano="I",
                rango_inf__lte=accidente.grado_invalidez,
                rango_sup__gte=accidente.grado_invalidez,
            )

        smlv = float(parametro.valor)

        salario = accidente.empleado.salario
        if accidente.salario_accidentado is None:

            accidente.salario_accidentado = salario
            accidente.salario_minimo = smlv

            if niveles is not None and niveles.count() > 0:
                for niv in niveles:
                    if niv.nivel == 1:
                        accidente.factor_moral_n1 = niv.valor
                    elif niv.nivel == 2:
                        accidente.factor_moral_n2 = niv.valor
                    elif niv.nivel == 3:
                        accidente.factor_moral_n3 = niv.valor
                    elif niv.nivel == 4:
                        accidente.factor_moral_n4 = niv.valor
                    elif niv.nivel == 5:
                        accidente.factor_moral_n5 = niv.valor
            else:
                accidente.factor_moral_n1 = 0
                accidente.factor_moral_n2 = 0
                accidente.factor_moral_n3 = 0
                accidente.factor_moral_n4 = 0
                accidente.factor_moral_n5 = 0
            accidente.valor_moral_n1 = 0
            accidente.valor_moral_n2 = 0
            accidente.valor_moral_n3 = 0
            accidente.valor_moral_n4 = 0
            accidente.valor_moral_n5 = 0
            accidente.valor_dano_moral = 0

            accidente.save()

        edad = relativedelta(
            accidente.fecha_accidente, accidente.empleado.fecha_nacimiento
        )
        tiempo_expectativa = 0
        try:
            expectativa = (
                ExpectativaVida.objects.filter(edad=edad.years)
                .filter(tipo=accidente.empleado.sexo)
                .get()
            )
            tiempo_expectativa = expectativa.expectativa
        except ObjectDoesNotExist:
            pass

        estado = "LESIONADO"
        if accidente.incapacidad:
            estado = "INCAPACITADO"
        if accidente.invalidez:
            estado = "INVALIDO"
        if accidente.fallecido:
            estado = "FALLECIDO"

        context_data = {
            "accidente": accidente,
            "salario": salario,
            "edad": edad,
            "estado": estado,
            "lcf": tiempo_expectativa * 12,
            "interes_tecnico": interes_tecnico,
            "expectativa": tiempo_expectativa,
            "smlv": smlv,
            "f_dano_emergente": f_dano_emergente,
            "f_dano_moral": f_dano_moral,
            "f_danomaterial": DanoMaterialForm(),
            "list_dano_emergente": CostosAccDanoEmergente.objects.filter(accidente=pk),
        }

        return render(request, "accidentes/lucro.html", context_data)


class AprociacionesView(View):
    def get(self, request, pk):
        f_tiempos_acompanamiento = TiemposAccAcompanamientoForm()
        accidente = get_object_or_404(Accidente, id=pk)

        matrix = []

        r_reemplazos = ReemplazoAccidente.objects.filter(accidente=pk).aggregate(
            total=Sum(F("valor_salarial_real") * F("dias"))
        )["total"]
        r_capacitaciones = CapacitadorAccidente.objects.filter(accidente=pk).aggregate(
            total=Sum(F("salario") / 30 * F("dias"))
        )["total"]

        result = (
            TiemposAccAcompanamiento.objects.filter(accidente=pk)
            .values("tipo_acompanamiento")
            .order_by("tipo_acompanamiento")
            .annotate(dTotal=Sum("total"))
        )
        tipos_acompanamiento = TipoAcompanamiento.objects.all().order_by("id")
        factor_parafiscales = FactorAccParafiscales.objects.all().order_by("id")
        for parafiscal in factor_parafiscales:
            fila = []
            fila.append(parafiscal.descripcion)
            for tipo in tipos_acompanamiento:
                valor = 0
                if tipo.id == 5:
                    result_5 = (
                        TiemposAccAcompanamiento.objects.filter(
                            accidente=pk, tipo_acompanamiento=5
                        )
                        .values("tipo_acompanamiento")
                        .annotate(dTotal=Sum("total"))
                    )
                    valores_adicionales = 0
                    if r_reemplazos is not None:
                        valores_adicionales = r_reemplazos
                    if r_capacitaciones is not None:
                        valores_adicionales += r_capacitaciones

                    for r5 in result_5.iterator():
                        valores_adicionales += r5["dTotal"]
                    valor = parafiscal.factor * valores_adicionales

                for r in result.iterator():
                    if tipo.id == r["tipo_acompanamiento"] and tipo.id != 5:
                        valor = parafiscal.factor * r["dTotal"]

                fila.append(valor)
            matrix.append(fila)

        context_data = {
            "accidente": accidente,
            "f_tiempos_acompanamiento": f_tiempos_acompanamiento,
            "list_acompanamientos": TiemposAccAcompanamiento.objects.filter(
                accidente=pk
            ),
            "matrix": matrix,
            "factor_parafiscal": factor_parafiscales,
            "tipos_acompanamiento": tipos_acompanamiento,
        }

        return render(request, "accidentes/apropiaciones.html", context_data)

    def post(selft, request, *args, **kwargs):
        try:
            accidente = get_object_or_404(Accidente, id=kwargs["pk"])
            form = TiemposAccAcompanamientoForm(request.POST)
            acompanante = get_object_or_404(Persona, id=request.POST["empleado"])
            factor = get_object_or_404(
                FactorTiemposAcompanamiento, id=request.POST["factor"]
            )
            form.instance.salario = acompanante.salario
            form.instance.valor_diario = acompanante.salario / 240
            form.instance.valor_factor = factor.factor
            logger.info(form.instance.tiempo)
            logger.info(request.POST["tiempo"])
            form.instance.tiempo = datetime.strptime(request.POST["tiempo"], "%H:%M")
            tiempo = form.instance.tiempo.hour + form.instance.tiempo.minute / 60
            form.instance.total = (
                (acompanante.salario / 240) * Decimal(tiempo) * factor.factor
            )

            form.instance.accidente = accidente
            # save the data and after fetch the object in instance
            if form.is_valid():
                instance = form.save()
                return HttpResponseRedirect(
                    reverse(
                        "apropiaciones_nomina", kwargs={"pk": instance.accidente.id}
                    )
                )
        except Exception as e:
            logger.error(e)
            messages.error(request, str(e))
        # some error occured
        return HttpResponseRedirect(
            reverse("apropiaciones_nomina", kwargs={"pk": kwargs["pk"]})
        )


class CostosNuevosView(CreateView):
    model = CostosAccInsumosMedicos
    template_name = "accidentes/costo_insumos_med.html"
    form_class = CostosAccInsumosMedicosForm

    def get_context_data(self, **kwargs):
        context = super(CostosNuevosView, self).get_context_data(**kwargs)
        context["acc"] = self.kwargs["acc"]
        return context

    def form_valid(self, form):
        form.instance.accidente = Accidente.objects.get(pk=self.kwargs["acc"])
        context = {"acc": self.kwargs["acc"]}
        self.success_url = reverse_lazy(
            "costos_list", kwargs={"pk": self.kwargs["acc"]}
        )
        return super(CostosNuevosView, self).form_valid(form)


class CostosEditView(UpdateView):
    model = CostosAccInsumosMedicos
    template_name = "catalogos/subcategoria_form.html"
    context_object_name = "obj"
    form_class = CostosAccInsumosMedicosForm
    success_url = reverse_lazy("ausentismo:costos_list")


class AdaptacionCambioView(View):
    def get(self, request, pk):
        accidente = get_object_or_404(Accidente, id=pk)
        f_reemplazo = ReemplazosAccForm()
        f_capacitador = CapacitacionAccForm()
        f_costos_adicionales = CostosAccAdicionalesForm()

        context_data = {
            "accidente": accidente,
            "f_reemplazo": f_reemplazo,
            "f_capacitador": f_capacitador,
            "f_costos_adicionales": f_costos_adicionales,
            "list_reemplazos": ReemplazoAccidente.objects.filter(accidente=pk),
            "list_capacitadores": CapacitadorAccidente.objects.filter(accidente=pk),
            "list_costos": CostosAccAdicionales.objects.filter(accidente=pk),
        }

        return render(request, "accidentes/adaptacion_cambio.html", context_data)


class BalanceView(View):
    def get(self, request, pk):
        accidente = get_object_or_404(Accidente, id=pk)

        balance = {
            "total_valor": 0,
            "total_tiempo": 0,
            "sub_secc_1": 0,
            "sub_lucro": 0,
            "sub_dano_material": 0,
            "sub_dano_moral": 0,
            "sub_adaptacion_valor": 0,
            "sub_adaptacion_tiempo": 0,
            "sub_nomina_valor": 0,
            "sub_nomina_tiempo": 0,
            "sub_apropicaciones_valor": 0,
            "sub_apropiaciones_tiempo": 0,
        }
        balance["otros"] = {
            "costos_insumos_medicos": 0,
            "costo_transporte": 0,
            "otros_costos": 0,
            "dano_material": 0,
            "lucro_cesante": 0,
            "lucro_cesante_futuro": 0,
            "nivel1": 0,
            "nivel2": 0,
            "nivel3": 0,
            "nivel4": 0,
            "nivel5": 0,
            "subtotal_valor": 0,
            "subtotal_tiempo": 0,
        }
        balance["maquinaria"] = {
            "lista_maquinaria": 0,
            "subtotal_valor": 0,
            "subtotal_tiempo": 0,
        }
        balance["material"] = {
            "lista_materia_prima": 0,
            "subtotal_valor": 0,
            "subtotal_tiempo": 0,
        }
        balance["mano_obra"] = {
            "lista_mano_obra_requerida": 0,
            "reemplazos_valor": 0,
            "reemplazos_tiempo": 0,
            "capacitaciones_valor": 0,
            "capacitaciones_tiempo": 0,
            "costos_adicionales_valor": 0,
            "costos_adicionales_tiempo": 0,
            "apro_encontraba_momento_valor": 0,
            "apro_encontraba_momento_tiempo": 0,
            "apro_ayudo_rescate_valor": 0,
            "apro_ayudo_rescate_tiempo": 0,
            "apro_encontraba_area_valor": 0,
            "apro_encontraba_area_tiempo": 0,
            "apro_ayuda_investigacion_valor": 0,
            "apro_ayuda_investigacion_tiempo": 0,
            "apro_ayuda_imple_valor": 0,
            "apro_ayuda_imple_tiempo": 0,
            "parafiscales_valor": 0,
            "parafiscales_tiempo": 0,
            "prestaciones_valor": 0,
            "prestaciones_tiempo": 0,
            "subtotal_valor": 0,
            "subtotal_tiempo": 0,
        }

        valor_1 = 0
        valor_2 = 0
        subtotal_costos = 0
        lucro_dano_emergente = 0
        valor_5 = 0
        valor_6 = 0
        valor_7 = 0
        valor_8 = 0
        valor_9 = 0
        valor_10 = 0
        valor_11 = 0
        valor_12 = 0
        subtotal_adaptacion_cambio = 0
        costo_maquinaria = 0
        costo_materia_prima = 0
        costo_mano_obra = 0

        costo_insumo_medico = 0
        costo_transporte = 0
        costo_otros = 0
        subtotal_lucro = 0
        subtotal_dano_material_futuro = 0
        valor_nivel1 = 0
        valor_nivel2 = 0
        valor_nivel3 = 0
        valor_nivel4 = 0
        valor_nivel5 = 0
        costo_reemplazo = 0
        costo_capacitaciones = 0
        costo_adicionales = 0
        tiempo_reemplazos = 0
        tiempo_capacitaciones = 0
        subtotal_tiempo_adaptacion = 0

        result = (
            TiemposAccAcompanamiento.objects.filter(accidente=accidente.id)
            .values("tipo_acompanamiento")
            .order_by("tipo_acompanamiento")
            .annotate(dTotal=Sum("total"))
        )

        for r in result.iterator():
            if 1 == r["tipo_acompanamiento"]:
                valor_2 = calcular_valor_acompanamiento(Decimal(r["dTotal"]))
            elif 2 == r["tipo_acompanamiento"]:
                valor_9 = calcular_valor_acompanamiento(Decimal(r["dTotal"]))
            elif 3 == r["tipo_acompanamiento"]:
                valor_10 = calcular_valor_acompanamiento(Decimal(r["dTotal"]))
            elif 4 == r["tipo_acompanamiento"]:
                valor_11 = calcular_valor_acompanamiento(Decimal(r["dTotal"]))
            elif 5 == r["tipo_acompanamiento"]:
                valor_12 = calcular_valor_acompanamiento(Decimal(r["dTotal"]))

        v_reemplazos = ReemplazoAccidente.objects.filter(
            accidente=accidente.id
        ).aggregate(total=Sum(F("costo")))["total"]
        v_capacitaciones = CapacitadorAccidente.objects.filter(
            accidente=accidente.id
        ).aggregate(total=Sum(F("costo")))["total"]
        valor_12 += 0 if v_reemplazos is None else v_reemplazos
        valor_12 += 0 if v_capacitaciones is None else v_capacitaciones

        tiempo_dic = {}
        result = TiemposAccAcompanamiento.objects.filter(
            accidente=accidente.id
        ).order_by("tipo_acompanamiento")

        for r in result:
            if tiempo_dic.get(r.tipo_acompanamiento.id) is None:
                tiempo_dic[r.tipo_acompanamiento.id] = (
                    r.tiempo.hour * 60 + r.tiempo.minute
                )
            else:
                tiempo_dic[r.tipo_acompanamiento.id] = tiempo_dic[
                    r.tipo_acompanamiento.id
                ] + (r.tiempo.hour * 60 + r.tiempo.minute)

        t_reemplazos = ReemplazoAccidente.objects.filter(
            accidente=accidente.id
        ).aggregate(total=Sum(F("dias")))["total"]

        tiempo_reemplazos = calcular_tiempo(
            None, 0, 0 if t_reemplazos is None else t_reemplazos
        )

        t_capacitaciones = CapacitadorAccidente.objects.filter(
            accidente=accidente.id
        ).aggregate(total=Sum(F("dias")))["total"]
        tiempo_capacitaciones = calcular_tiempo(
            None, 0, 0 if t_capacitaciones is None else t_capacitaciones
        )

        dias_adicinales = (0 if t_reemplazos is None else t_reemplazos) + (
            0 if t_capacitaciones is None else t_capacitaciones
        )
        subtotal_tiempo_adaptacion = calcular_tiempo(None, 0, dias_adicinales)

        valor_1 = calcular_tiempo(tiempo_dic, 1, 0)
        valor_5 = calcular_tiempo(tiempo_dic, 2, 0)
        valor_6 = calcular_tiempo(tiempo_dic, 3, 0)
        valor_7 = calcular_tiempo(tiempo_dic, 4, 0)
        valor_8 = calcular_tiempo(tiempo_dic, 5, dias_adicinales)

        result = CostosAccInsumosMedicos.objects.filter(
            accidente=accidente.id
        ).aggregate(total=Sum(F("valor") * F("cantidad")))["total"]
        if result is not None:
            subtotal_costos = subtotal_costos + result
            costo_insumo_medico = costo_insumo_medico + result
        result = CostosAccTransporte.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("valor"))
        )["total"]
        if result is not None:
            subtotal_costos = subtotal_costos + result
            costo_transporte = costo_transporte + result
        result = CostosAccOtros.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("valor"))
        )["total"]
        if result is not None:
            subtotal_costos = subtotal_costos + result
            costo_otros = costo_otros + result

        # Reemplazos
        result = ReemplazoAccidente.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("costo"))
        )["total"]
        if result is not None:
            costo_reemplazo = costo_reemplazo + result
            subtotal_adaptacion_cambio = subtotal_adaptacion_cambio + result

        # Capacitaciones
        result = CapacitadorAccidente.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("costo"))
        )["total"]
        if result is not None:
            costo_capacitaciones = costo_capacitaciones + result
            subtotal_adaptacion_cambio = subtotal_adaptacion_cambio + result

        result = CostosAccAdicionales.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("valor"))
        )["total"]
        if result is not None:
            costo_adicionales = costo_adicionales + result
            subtotal_adaptacion_cambio = subtotal_adaptacion_cambio + result

        result = CostosAccDanoEmergente.objects.filter(
            accidente=accidente.id
        ).aggregate(total=Sum(F("valor")))["total"]
        if result is not None:
            lucro_dano_emergente = lucro_dano_emergente + result

        result = CostosAccMaquinaria.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("valor") * F("cantidad"))
        )["total"]
        if result is not None:
            costo_maquinaria = costo_maquinaria + result
            subtotal_costos = subtotal_costos + costo_maquinaria

        result = CostosAccRepuestos.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("valor") * F("cantidad"))
        )["total"]
        if result is not None:
            costo_materia_prima = costo_materia_prima + result
            subtotal_costos = subtotal_costos + costo_maquinaria

        result = CostosAccManoObra.objects.filter(accidente=accidente.id).aggregate(
            total=Sum(F("valor") * F("cantidad"))
        )["total"]
        if result is not None:
            costo_mano_obra = costo_mano_obra + result
            subtotal_costos += costo_maquinaria

        subtotal_lucro = lucro_dano_emergente
        if accidente.lucro_consolidado is not None:
            subtotal_dano_material_futuro = (
                accidente.lucro_consolidado + accidente.lucro_futuro
            )
        else:
            subtotal_dano_material_futuro = 0

        valor_dano = Decimal(0.0)
        valor_nivel1 = valor_dano + (
            Decimal(accidente.valor_moral_n1)
            * Decimal(accidente.salario_minimo)
            * Decimal(accidente.factor_moral_n1)
        )
        valor_nivel2 = valor_dano + (
            Decimal(accidente.valor_moral_n1)
            * Decimal(accidente.salario_minimo)
            * Decimal(accidente.factor_moral_n2)
        )
        valor_nivel3 = valor_dano + (
            Decimal(accidente.valor_moral_n1)
            * Decimal(accidente.salario_minimo)
            * Decimal(accidente.factor_moral_n3)
        )
        valor_nivel4 = valor_dano + (
            Decimal(accidente.valor_moral_n1)
            * Decimal(accidente.salario_minimo)
            * Decimal(accidente.factor_moral_n4)
        )
        valor_nivel5 = valor_dano + (
            Decimal(accidente.valor_moral_n1)
            * Decimal(accidente.salario_minimo)
            * Decimal(accidente.factor_moral_n5)
        )

        subtotal_niveles = (
            valor_nivel1 + valor_nivel2 + valor_nivel3 + valor_nivel4 + valor_nivel5
        )

        context_data = {
            "accidente": accidente,
            "valor_1": valor_1,
            "valor_2": valor_2,
            "subtotal_costos": subtotal_costos,
            "lucro_dano_emergente": lucro_dano_emergente,
            "valor_5": valor_5,
            "valor_6": valor_6,
            "valor_7": valor_7,
            "valor_8": valor_8,
            "valor_9": valor_9,
            "valor_10": valor_10,
            "valor_11": valor_11,
            "valor_12": valor_12,
            "subtotal_adaptacion_cambio": subtotal_adaptacion_cambio,
            "costo_maquinaria": costo_maquinaria,
            "costo_materia_prima": costo_materia_prima,
            "costo_mano_obra": costo_mano_obra,
            "costo_insumo_medico": costo_insumo_medico,
            "costo_transporte": costo_transporte,
            "costo_otros": costo_otros,
            "costo_maquinaria": costo_maquinaria,
            "costo_materia_prima": costo_materia_prima,
            "costo_mano_obra": costo_mano_obra,
            "lucro_cesante": accidente.lucro_consolidado
            if accidente.lucro_consolidado is not None
            else 0,
            "lucro_cesante_futuro": accidente.lucro_futuro
            if accidente.lucro_futuro is not None
            else 0,
            "subtotal_dano_material_futuro": subtotal_dano_material_futuro,
            "accidente_valor_moral_n1": valor_nivel1,
            "accidente_valor_moral_n2": valor_nivel2,
            "accidente_valor_moral_n3": valor_nivel3,
            "accidente_valor_moral_n4": valor_nivel4,
            "accidente_valor_moral_n5": valor_nivel5,
            "subtotal_niveles": subtotal_niveles,
            "costo_reemplazo": costo_reemplazo,
            "costo_capacitaciones": costo_capacitaciones,
            "costo_adicionales": costo_adicionales,
            "tiempo_reemplazos": tiempo_reemplazos,
            "tiempo_capacitaciones": tiempo_capacitaciones,
            "subtotal_tiempo_adaptacion": subtotal_tiempo_adaptacion,
        }

        return render(request, "accidentes/balance.html", context_data)


def calcular_tiempo(dic, indice, dias):
    if (dic is None or dic.get(indice) is None) and (dias is None or dias == 0):
        return "00:00"
    elif dias > 0:
        return str(dias * 8) + ":00"
    else:
        minutos = int(dic.get(indice) % 60)
        if minutos < 10:
            s_minutos = "0" + str(int(dic.get(indice) % 60))
        else:
            s_minutos = str(int(dic.get(indice) % 60))
        return str(int(dic.get(indice) / 60) + (dias * 8)) + ":" + s_minutos


def calcular_valor_acompanamiento(total):
    return Decimal(total) * Decimal(0.5568)
