from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def inicio(request):
    return render(request,'donia_clarita/inicio.html')
def login(request):
    return render(request,'donia_clarita/login.html')
def administracion(request):
    return render(request,'donia_clarita/administracion.html')
def habitacion(request):
    return render(request,'donia_clarita/habitacion/habitacion.html')
def adminnew(request):
    return render(request,'donia_clarita/admin_new.html')