from django.contrib import admin
from django.urls import path
from ausentismoApp import views
from .views import PersonaView, RegistrarAusentismoView, BuscarPersonaView, FilteredAusentismoListView, RegistrarAccidenteView, FilteredAccidenteListView

urlpatterns = [
    path('', views.home, name="home"),
    path('ausentismos', FilteredAusentismoListView.as_view(), name="ausentismo"),
    path('informes', views.informes, name="informes"),
    path('accidentes', FilteredAccidenteListView.as_view(), name="accidentes"),
    path('personal', views.personal, name="personal"),
    path('person-detail/<int:pk>/', PersonaView.as_view(),name='persona_view'),
    path('ausentismos/add', RegistrarAusentismoView.as_view(), name="ausentismo_add_view"),
    path('personal/search', BuscarPersonaView.as_view(), name="busqueda_persona_view"),
    path('accidentes/add', RegistrarAccidenteView.as_view(), name="accidente_add_view")
]
