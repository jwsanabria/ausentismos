from django.contrib import admin
from django.urls import path
from ausentismoApp import views
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name="home"),
    path('ausentismos', login_required(FilteredAusentismoListView.as_view()), name="ausentismo"),
    path('informes', views.informes, name="informes"),
    path('accidentes', login_required(FilteredAccidenteListView.as_view()), name="accidentes"),
    path('personal', views.personal, name="personal"),
    path('person-detail/<int:pk>/', login_required(PersonaView.as_view()),name='persona_view'),
    path('ausentismos/add', login_required(RegistrarAusentismoView.as_view()), name="ausentismo_add_view"),
    path('personal/search', login_required(BuscarPersonaView.as_view()), name="busqueda_persona_view"),
    path('accidentes/add', login_required(RegistrarAccidenteView.as_view()), name="accidente_add_view"),

    path('accidentes/documentar/<int:pk>', login_required(CostosView.as_view()), name='costos_list'),
    path('accidentes/lucro/<int:pk>', login_required(LucroView.as_view()), name='lucro_cesante'),
    path('accidentes/lucro/liquidar', login_required(LiquidacionView.as_view()), name="liquidacion_view"),
    path('accidentes/costos_medicos/new', login_required(CostosNuevosView.as_view()), name='costos_new'),
    path('accidentes/costos_medicos/edit/<int:pk>', login_required(CostosEditView.as_view()), name='costos_edit'),
    path('accidentes/lucro/dano_emergente/<int:pk>', views.postDanoEmergente, name = "dano_emergente_view"),
    path('accidentes/costos/mano_obra/<int:pk>', views.postManoObra, name = "ajax_mano_obra"),
    path('accidentes/costos/repuesto/<int:pk>', views.postRepuesto, name = "ajax_repuesto"),
    path('accidentes/costos/maquinaria/<int:pk>', views.postMaquinaria, name = "ajax_maquinaria"),
    path('accidentes/costos/otros/<int:pk>', views.post_otros, name ="ajax_otros"),
    path('accidentes/costos/transporte/<int:pk>', views.postTransporte, name = "ajax_transporte"),
    path('accidentes/costos/insumo_medico/<int:pk>', views.post_insumo, name ="ajax_insumo"),
    path('accidentes/apropiaciones/<int:pk>', login_required(AprociacionesView.as_view()), name='apropiaciones_nomina'),
    path('accidentes/adaptacion/<int:pk>', login_required(AdaptacionCambioView.as_view()), name='adaptacion_cambio'),
    path('accidentes/adaptacion/adicionales/<int:pk>', views.post_adicionales, name='ajax_adicionales'),
    path('accidentes/adaptacion/reemplazo/<int:pk>', views.postReemplazo, name='ajax_reemplazo'),
    path('accidentes/adaptacion/capacitador/<int:pk>', views.post_capacitador, name='ajax_capacitador'),
    path('accidentes/balance/<int:pk>', login_required(BalanceView.as_view()), name='balance'),
    path('accidentes/lucro/dano_moral/<int:pk>', views.post_dano_moral, name='ajax_dano_moral'),
    path('accidentes/costos/remove/<int:pk>', views.post_remove_row, name='ajax_remove_row'),
    path('accidentes/apropiaciones/remove/<int:pk>', views.post_remove_acompanamiento, name='ajax_remove_apropiacion'),
    path('accidentes/detalle/<int:pk>', login_required(DetalleAccidenteView.as_view()), name='detalle_accidente'),
    path('ausentismo/registrar', views.post_guardar_ausentismo, name='ajax_guardar_ausentismo'),
]
