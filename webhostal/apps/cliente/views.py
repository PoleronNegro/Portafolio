from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homecli(request):
    return render(request, "index_cli.html")

def detallecontrato(request):
    return render(request,'contratovigente/detalle_contrato.html')
