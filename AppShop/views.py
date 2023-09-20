from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "AppShop/inicio.html")

def alimentos(request):
    lista = Alimentos.objects.all()
    return render(request, "AppShop/alimentos.html", {"alimentos": lista})

def accesorios(request):
    lista = Accesorios.objects.all()
    return render(request, "AppShop/accesorios.html", {"accesorios": lista})

def juguetes(request):
    lista = Juguetes.objects.all()
    return render(request, "AppShop/juguetes.html", {"juguetes": lista})

def alimento_formulario(request):
    if request.method == 'POST':
        mi_formulario = Alimento_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            alimento = Alimentos(marca=request.POST['marca'], tipo=request.POST['tipo'], mascota=request.POST['mascota'], descripcion=request.POST['descripcion'])
            alimento.save()
        return render(request, "AppShop/inicio.html")
    else:
        mi_formulario = Alimento_Formulario()
        return render(request, "AppShop/alimento_formulario.html", {"mi_formulario": mi_formulario})
    
def accesorios_formulario(request):
    if request.method == 'POST':
        mi_formulario = Accesorios_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            accesorio = Accesorios(marca=request.POST['marca'], tipo=request.POST['tipo'], mascota=request.POST['mascota'], descripcion=request.POST['descripcion'])
            accesorio.save()
        return render(request, "AppShop/inicio.html")
    else:
        mi_formulario = Accesorios_Formulario()
        return render(request, "AppShop/accesorio_formulario.html", {"mi_formulario": mi_formulario})
    
def juguetes_formulario(request):
    if request.method == 'POST':
        mi_formulario = Juguetes_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            juguete = Juguetes(marca=request.POST['marca'], tipo=request.POST['tipo'], mascota=request.POST['mascota'])
            juguete.save()
        return render(request, "AppShop/inicio.html")
    else:
        mi_formulario = Juguetes_Formulario()
        return render(request, "AppShop/juguete_formulario.html", {"mi_formulario": mi_formulario})

def busqueda_mascota(request):
    return render(request, "AppShop/busqueda_mascota.html")

def buscar(request):
    if request.GET["mascota"]:
        mascota = request.GET["mascota"]
        alimentos = Alimentos.objects.filter(mascota=mascota)
        return render(request, "AppShop/resultados_busqueda.html", {"alimentos": alimentos, "mascota": mascota})
    else:
        return HttpResponse("No enviaste info, por favor ingresa algo nuevamente")