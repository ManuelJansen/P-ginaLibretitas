from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.shortcuts import render
from .models import producto, cliente, venta, detalleVenta

from .forms import detalleVentaForm, ventaForm
# Create your views here.

def index(request):
    productos = producto.objects.all()
    context={"productos":productos}
    return render(request, 'index.html', context)
def libretas(request):
    productos = producto.objects.all()
    context={"productos":productos}
    return render(request, 'libretas.html', context)
def agendas(request):
    productos = producto.objects.all()
    context={"productos": productos}
    return render(request, 'agendas.html', context)
def stickers(request):
    productos = producto.objects.all()
    context={"productos": productos}
    return render(request, 'stickers.html', context)
def otros(request):
    productos = producto.objects.all()
    context={"productos": productos}
    return render(request, 'otros.html', context)
def carrito(request):
    context={}
    return render(request, 'carrito.html', context)
def encontrarnos(request):
    context={}
    return render(request, 'encontrarnos.html', context)
def registro(request):
    context={}
    return render(request, 'registro.html', context)
def login(request):
    context={}
    return render(request, 'login.html', context)

@login_required
def baseDatos(request):
    context={}
    if request.user.is_authenticated:
        request.session["usuario"]=request.user.username
        usuario=request.session["usuario"]
        context={'usuario': usuario}
    return render(request, 'baseDatos.html', context)

@login_required
def crudCliente(request):
    clientes = cliente.objects.all()
    context={"clientes":clientes}
    return render(request, 'crudCliente/clientes_list.html', context)
def addCliente(request):
    try:
        if request.method != "POST":
            context={}
            return render(request, 'crudCliente/add_cliente.html', context)
        else:
            rut=request.POST["rut"]
            nombre=request.POST["nombre"]
            fechaNac=request.POST["fechaNac"]
            email=request.POST["email"]
            direccion=request.POST["direccion"]
            contraseña=request.POST["contraseña"]

            obj=cliente.objects.create(
                rutCliente=rut, 
                nombreCliente=nombre,
                emailCliente=email,
                direccionCliente=direccion,
                fechaNacimientoCliente=fechaNac,
                contraseña=contraseña
            )

            obj.save()
            context={'mensaje': "Ya estás registrado!"}
            return render(request, 'crudCliente/add_cliente.html', context)
    except:
        context={'mensaje': "Comprueba los datos ingresados"}
        return render(request, 'crudCliente/add_cliente.html', context)
def delCliente(request, pk):
    context={}
    try:
        cliente1 = cliente.objects.get(rutCliente=pk)

        cliente1.delete()
        mensaje="Bien, datos eliminados..."
        clientes = cliente.objects.all()
        context = {'clientes': clientes, 'mensaje':mensaje}
        return render(request, 'crudCliente/clientes_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        clientes = cliente.objects.all()
        context = {'clientes':clientes, 'mensaje': mensaje}
        return render(request, 'crudCliente/clientes_list.html', context)
def modCliente(request, pk):
    if pk != "":
        cliente1=cliente.objects.get(rutCliente=pk)

        context={'cliente1': cliente1}
        if cliente1:
            return render(request, 'crudCliente/mod_Cliente.html', context)
        else:
            context={'mensaje': "Error, rut no existe..."}
            return render(request, 'crudCliente/clientes_list.html', context)
def clienteUpdate(request):
    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        fechaNac=request.POST["fechaNac"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]

        cliente1 = cliente()
        cliente1.rutCliente=rut
        cliente1.nombreCliente=nombre
        cliente1.fechaNacimientoCliente=fechaNac
        cliente1.emailCliente=email
        cliente1.direccionCliente=direccion
        cliente1.save()

        context={'mensaje': "Ok, datos actualizados...", 'cliente1':cliente1}
        return render(request, 'crudCliente/mod_Cliente.html', context)
    else:
        clientes=cliente.objects.all()
        context={'clientes', clientes}
        return render(request, 'crudCliente/clientes_list.html', context)
    
@login_required
def crudVentas(request):
    ventas=venta.objects.all()
    context={'ventas': ventas}
    return render(request, 'crudVenta/ventas_list.html', context)
def addVenta(request):
    context={}
    if request.method == "POST":
        form = ventaForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                form=ventaForm()
                context={'mensaje': "Venta agregada", 'form': form}
                return render(request, 'crudVenta/add_Venta.html', context)
        except:
            form=ventaForm()
            context={'mensaje': "Error al agregar venta, veifique los datos", 'form': form}
            return render(request, 'crudVenta/add_Venta.html', context)
    else:
        form = ventaForm()
        context={'form': form}
        return render(request, 'crudVenta/add_Venta.html', context)
    
def delVenta(request, pk):
    context={}
    try:
        venta1=venta.objects.get(idVenta=pk)
        venta1.delete()
        mensaje="Venta eliminada..."
        ventas=venta.objects.all()
        context={'ventas' :ventas, 'mensaje': mensaje}
        return render(request, 'crudVenta/ventas_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        ventas=venta.objects.all()
        context={'ventas': ventas, 'mensaje': mensaje}
        return render(request, 'crudVentas/ventas_list.html', context)
def modVenta(request, pk):
    if pk != "":
        venta1=venta.objects.get(idVenta=pk)
        clientes=cliente.objects.all()

        print(type(venta1.rutCliente.nombreCliente))

        context={'venta1': venta1, 'clientes': clientes}
        if venta1:
            return render(request, 'crudVenta/mod_Venta.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'crudVenta/ventas_list.html', context)
def ventasUpdate(request):
    if request.method == "POST":
        idVen=request.POST["idVen"]
        rutCli=request.POST["rutCli"]
        fechaVen=request.POST["fechaVen"]

        objCliente=cliente.objects.get(rutCliente = rutCli)

        venta1 = venta()
        venta1.idVenta=idVen
        venta1.rutCliente=objCliente
        venta1.fechaVenta=fechaVen
        venta1.save()

        clientes=cliente.objects.all()
        context={'mensaje': "Ok, venta actualizada...", 'clientes': clientes, 'venta1': venta1}
        return render(request, 'crudVenta/mod_Venta.html', context)
    else:
        ventas = venta.objects.all()
        context={'ventas': ventas}
        return render(request, 'crudVenta/ventas_list.html', context)
    
@login_required
def crudDetalle(request):
    detalles=detalleVenta.objects.all()
    context={'detalles': detalles}
    print("enviando datos detalle_lis")
    return render(request, 'crudDetalleVenta/detalle_list.html', context)
def addDetalle(request):
    context={}
    if request.method == "POST":
        form = detalleVentaForm(request.POST)
        if form.is_valid:
            form.save()
            form=detalleVentaForm()
            context={'mensaje': "Detalle agregado", 'form': form}
            return render(request, 'crudDetalleVenta/add_Detalle.html', context)
    else:
        form = detalleVentaForm()
        context={'form': form}
        return render(request, 'crudDetalleVenta/add_Detalle.html', context)
    
