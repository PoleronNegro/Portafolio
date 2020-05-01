from django.shortcuts import render
from django.shortcuts import redirect
from donia_clarita.models import Usuarios
from donia_clarita.forms import UsuariosForm  

# Create your views here.

def inicio(request):
    return render(request,'donia_clarita/inicio.html')

def login(request):
    return render(request,'donia_clarita/login.html')

def administracion(request):
    return render(request,'donia_clarita/administracion.html')

def vista(request):
    return render(request,'donia_clarita/Modulo_Administrador/MenuUsuarios.html')

def MenuUsuarios(request):
    if request.method == "POST":
        usu = Usuarios.objects.create()
        usu.NombreUsuario=request.POST['nombre_usuario']
        usu.Contrasenia=request.POST['passwd_usuario']
        usu.tipo_usuario=request.POST['id_tipo_usuario']
        usu.tipo_estado=request.POST['id_estado_usuario']
        usu.save()
        usua = Usuarios.objects.all()
        return render(request,'donia_clarita/Modulo_Administrador/adminnew.html',{'usua':usua})
    else:
        form = UsuariosForm()
        return render(request, 'donia_clarita/Modulo_Administrador/MenuUsuarios.html',{'usua':usua})

def adminnew(request):
    return render(request,'donia_clarita/Modulo_Administrador/admin_new.html')

def Empleado(request):
    return render(request,'donia_clarita/Modulo_Empleado/Empleado.html')

def ModEmpresas(request):
    return render(request,'donia_clarita/Modulo_Empleado/Empresas.html')

def ModProductos(request):
    return render(request,'donia_clarita/Modulo_Empleado/Productos.html')

def ModHuespedes(request):
    return render(request,'donia_clarita/Modulo_Empleado/Huespedes.html')

def ModProveedores(request):
    return render(request,'donia_clarita/Modulo_Empleado/Proveedores.html')

def ModPedidos(request):
    return render(request,'donia_clarita/Modulo_Empleado/Pedidos.html')

def ModContratos(request):
    return render(request,'donia_clarita/Modulo_Empleado/Contratos.html')

def ModGestionContratos(request):
    return render(request,'donia_clarita/Modulo_Empleado/GestionContratos.html')

def Proveedor(request):
    return render(request,'donia_clarita/Modulo_Proveedor/Proveedor.html')

def ModProducto(request):
    return render(request,'donia_clarita/Modulo_Proveedor/Productos.html')