
from urllib import request
from urllib.request import Request
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm, CustomUserCreationForm, ContactoForm, ReparacionForm
from .models import Producto, Registro, RegistroReparacion,Contacto
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Reserva.Carrito import Carrito
#from django.core.paginator import Paginator
from django.views.generic import ListView, View
from django.http import HttpResponse
from .utils import render_to_pdf
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def clases_golf(request):
    return render(request,'reserva/clasesgolf.html')

def somos(request):
    return render(request, 'somos.html')


    
def registrar_hora(request):
    data = {
        'form': ReservaForm()
    }
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Formulario enviado con éxito, pronto nos contactaremos contigo :)")
        else:
            data["form"] = formulario

    return render(request, 'reserva/registrar_hora.html', data)

def base(request):
    return render(request, 'base.html')

def home(request):
    busqueda = request.POST.get("buscar")
    print(busqueda)

    lista = []

    if busqueda != None and busqueda != '0':
        lista.append(('categoria', int(busqueda)))

    productos = Producto.objects.all()

    if len(lista) > 0:
        productos = Producto.objects.filter(
            *lista
        )

    data = {
        'productos': productos
    }

    return render(request, 'home.html', data)

def infoclases(request):
    return render(request, 'reserva/clasesgolf.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")

        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def contacto(request):
    data = {
        "form": ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            messages.success(request, "MEnsaje enviado con éxito, pronto nos contactaremos contigo :)")
        else:
            data["form"] = formulario

    return render(request, 'reserva/contacto.html', data)

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "home.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("home")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("home")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("home")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("home")

def checkout_carrito(request):
    return render(request, 'checkout.html')


#----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------



def reparacion(request):
    data = {
        'form': ReparacionForm()
    }
    if request.method == 'POST':
        formulario = ReparacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro guardado")
        else:
            data["form"] = formulario
    return render(request, 'reserva/reparacion.html', data)


def list_reparacion(request):
    registros = RegistroReparacion.objects.all

    data = {
        'entity': registros,  
    }
    return render(request, 'reserva/list_reparacion.html', data)


def mod_registro(request, id):
    registro = get_object_or_404(RegistroReparacion, id=id)
    data = {
        'form': ReparacionForm(instance=registro)
    }
    if request.method == 'POST':
        formulario = ReparacionForm(data=request.POST, instance=registro)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="list_reparacion")
        data["form"] = formulario
    return render(request, 'reserva/mod_registro.html', data)


def eliminar_registro(request, id):
    registro = get_object_or_404(RegistroReparacion, id=id)
    registro.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_reparacion")


def list_solicitud(request):
    solicitudes = Registro.objects.all

    data = {
        'solicitudes': solicitudes
    }

    return render(request, 'reserva/list_solicitud.html', data)


def list_contacto(request):
    contactos = Contacto.objects.all
    data = {
        'contactos': contactos
    }
    return render(request, 'reserva/list_contacto.html', data)



#PDF REPORTE
class RegistroPdf(View):
    def get(self, request, *args, **kwargs):
        entity = RegistroReparacion.objects.all()
        data = {
            'entity' : entity,
        }
        pdf = render_to_pdf('reserva/registro_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def eliminar_solicitud(request, id):
    solicitud = get_object_or_404(RegistroReparacion, id=id)
    solicitud.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="list_solicitud")

