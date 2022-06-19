from django.contrib import admin
from django.urls import path
from ausentismoApp import views

urlpatterns = [
    path('', views.home),
    path('ausentismos', views.ausentismos),
    path('informes', views.informes),
    path('accidentes', views.accidentes),
    path('personal', views.personal)
]
