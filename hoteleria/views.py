from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Habitacionm
from .forms import HabitacionForm
from .models import Pasajerom
from .forms import PasajeroForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    return render(request,'paginas/inicio.html')


def habitacion(request):
    habitacion = Habitacionm.objects.all()
    return render(request,'habitacion/index.html',{'habitacion':habitacion})


def crearhab(request):
    formulario = HabitacionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('habitacion')
    return render(request,'habitacion/crear.html', {'formulario': formulario})


def editarhab(request,id):
    habitacion = Habitacionm.objects.get(id=id)
    formulario = HabitacionForm(request.POST or None, request.FILES or None, instance=habitacion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('habitacion')
    return render(request, 'habitacion/editar.html', {'formulario': formulario})

def eliminarhab(request,id):
    habitacion = Habitacionm.objects.get(id=id)
    habitacion.delete()
    return redirect('habitacion')


def pasajeroindex(request):
    pasajerot = Pasajerom.objects.all()
    return render(request,'pasajeros/index.html',{'pasajerot': pasajerot})


def crearpas(request):
    formulario = PasajeroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pasajeroindex')
    return render(request,'pasajeros/crear.html', {'formulario': formulario})


def eliminarpas(request,id):
    pasajero = Pasajerom.objects.get(id=id)
    pasajero.delete()
    return redirect('pasajeroindex')

def editarpas(request,id):
    pasajero = Pasajerom.objects.get(id=id)
    formulario = PasajeroForm(request.POST or None, request.FILES or None, instance=pasajero)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('pasajeroindex')
    return render(request, 'pasajeros/editar.html', {'formulario': formulario})


def habpas(request):
    habitacion = Pasajerom.objects.all().values('nhabitacionpas','nombrepasajero').order_by('nhabitacionpas')
    return render(request,'extras/habpas.html',{'habitacion':habitacion})


