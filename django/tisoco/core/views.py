from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def producto_detalle(request, nombre_producto):
    return HttpResponse(
        f"""
            <h1>Bienvenid@ {nombre_producto} </h1>
            <p>Detalle del producto</p>
        """
    )
# Create your views here.
