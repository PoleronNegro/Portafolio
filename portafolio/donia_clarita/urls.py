from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('vista/',views.vista,name="vista"),
    path('MenuUsuarios/', views.MenuUsuarios, name='MenuUsuarios'),
    path('adminnew/', views.adminnew, name='adminnew'),
    path('Empleado/',views.Empleado,name='Empleado'),
    path('Empresas/',views.ModEmpresas,name='Empresas'),
    path('Productos/',views.ModProductos,name='Productos'),
    path('Huespedes/',views.ModHuespedes,name='Huespedes'),
    path('Proveedores/',views.ModProveedores,name='Proveedores'),
    path('Pedidos/',views.ModPedidos,name='Pedidos'),
    path('Contratos/',views.ModContratos,name='Contratos'),
    path('Proveedor/',views.Proveedor,name='Proveedor'),
    path('Producto/',views.ModProducto,'Producto'),
]