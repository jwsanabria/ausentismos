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

]
