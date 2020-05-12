from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeadmin(request):
    return render(request, "index_admin.html")

def adminusuario(request):
    return render(request,'usuario/Admin_Usuario.html')
def listausuario(request):
    return render(request,'usuario/Listado_Usuario.html')

def adminhabit(request):
    return render(request,'habitacion/Admin_Habitacion.html')
def listahabit(request):
    return render(request,'habitacion/Listado_Habitacion.html')

def adminempleado(request):
    return render(request,'empleados/Admin_Empleado.html')
def listaempleado(request):
    return render(request,'empleados/Listado_Empleado.html')

def pedidos(request):
    return render(request,'informes/InformePedido.html')
def productos(request):
    return render(request,'informes/InformeProductos.html')