from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('productos/detalle/<str:nombre_producto>', views.producto_detalle, name='productos_detalle')

]