from django.contrib import admin
from django.urls import path
from ausentismoApp import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('ausentismos', FilteredAusentismoListView.as_view(), name="ausentismo"),
    path('informes', views.informes, name="informes"),
    path('accidentes', FilteredAccidenteListView.as_view(), name="accidentes"),
    path('personal', views.personal, name="personal"),
    path('person-detail/<int:pk>/', PersonaView.as_view(),name='persona_view'),
    path('ausentismos/add', RegistrarAusentismoView.as_view(), name="ausentismo_add_view"),
    path('personal/search', BuscarPersonaView.as_view(), name="busqueda_persona_view"),
    path('accidentes/add', RegistrarAccidenteView.as_view(), name="accidente_add_view"),

    path('accidentes/documentar/<int:pk>', CostosView.as_view(), name='costos_list'),
    path('accidentes/lucro/<int:pk>', LucroView.as_view(), name='lucro_cesante'),
    path('accidentes/lucro/liquidar', LiquidacionView.as_view(), name="liquidacion_view"),
    path('accidentes/costos_medicos/new', CostosNuevosView.as_view(), name='costos_new'),
    path('accidentes/costos_medicos/edit/<int:pk>', CostosEditView.as_view(), name='costos_edit'),
    path('accidentes/lucro/dano_emergente/<int:pk>', views.postDanoEmergente, name = "dano_emergente_view"),
    path('accidentes/costos/mano_obra/<int:pk>', views.postManoObra, name = "ajax_mano_obra"),
    path('accidentes/costos/repuesto/<int:pk>', views.postRepuesto, name = "ajax_repuesto"),
    path('accidentes/costos/maquinaria/<int:pk>', views.postMaquinaria, name = "ajax_maquinaria"),
    path('accidentes/costos/otros/<int:pk>', views.postOtros, name = "ajax_otros"),
    path('accidentes/costos/transporte/<int:pk>', views.postTransporte, name = "ajax_transporte"),
    path('accidentes/costos/insumo_medico/<int:pk>', views.postInsumo, name = "ajax_insumo"),
    path('accidentes/apropiaciones/<int:pk>', AprociacionesView.as_view(), name='apropiaciones_nomina'),
    path('accidentes/adaptacion/<int:pk>', AdaptacionCambioView.as_view(), name='adaptacion_cambio'),
    path('accidentes/adaptacion/adicionales/<int:pk>', views.postAdicionales, name='ajax_adicionales'),
    path('accidentes/adaptacion/reemplazo/<int:pk>', views.postReemplazo, name='ajax_reemplazo'),
    path('accidentes/adaptacion/capacitador/<int:pk>', views.postCapacitador, name='ajax_capacitador'),
    path('accidentes/balance/<int:pk>', BalanceView.as_view(), name='balance'),
    path('accidentes/lucro/dano_moral/<int:pk>', views.postDanoMoral, name='ajax_dano_moral'),
    path('accidentes/costos/remove/<int:pk>', views.postRemoveRow, name='ajax_remove_row'),
    path('accidentes/apropiaciones/remove/<int:pk>', views.postRemoveAcompanamiento, name='ajax_remove_apropiacion')
]
