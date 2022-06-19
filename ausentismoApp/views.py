from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Inicio")

def ausentismos(request):
    return HttpResponse("ausentismos")

def informes(request):
    return HttpResponse("informes")

def accidentes(request):
    return HttpResponse("accidentes")

def personal(request):
    return HttpResponse("personal")