from urllib.request import Request
from django.shortcuts import render

from Tiendita.models import Producto

# Create your views here.


def homeplanty(request):
    return render(request, 'homeplanty.html')



def formulario(request):
    return render(request, 'formulario.html')


def listaproductos(request):
    listado = Producto.objects.all()
    return render(request, 'ListaProductos.html', {'listado': listado})


