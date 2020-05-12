from django.urls import path
from . import views

urlpatterns = [
    path('administrador/', views.homeadmin, name='index_admin.html'),

    path('adminusuario/',  views.adminusuario, name='adminusuario.html'),
    path('listadousuario/',  views.listausuario, name='listadousuario.html'),

    path('adminhabitacion/',  views.adminhabit, name='Admin_Habitacion.html'),
    path('listahabitacion/',  views.listahabit, name='Listado_Habitacion.html'),

    path('adminempleado/',  views.adminempleado, name='Admin_Empleado.html'),
    path('listaempleado/',  views.listaempleado, name='Listado_Empleado.html'),

    path('pedidos/',  views.pedidos, name='InformePedido.html'),
    path('productos/',  views.productos, name='InformeProductos.html'),


]