from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "index.html")

def ausentismos(request):
    return render(request, "ausentismos/index.html")

def informes(request):
    return render(request, "informes/index.html")

def accidentes(request):
    return render(request, "accidentes/index.html")

def personal(request):
    return render(request, "personal/index.html")