from django.contrib import admin
from django.urls import path
from ausentismoApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ausentismos', views.ausentismos, name="ausentismo"),
    path('informes', views.informes, name="informes"),
    path('accidentes', views.accidentes, name="accidentes"),
    path('personal', views.personal, name="personal"),
    path('personas/', views.PersonaListView.as_view(), name="personal")
]
