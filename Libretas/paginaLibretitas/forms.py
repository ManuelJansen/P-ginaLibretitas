from django import forms
from .models import detalleVenta, venta
from django.forms import ModelForm

class detalleVentaForm(ModelForm):
    class Meta:
        model = detalleVenta
        fields = ['idVenta', 'idProducto', 'cantidad']
        labels = {'idVenta': 'Id Venta', 'idProducto': 'Producto', 'cantidad': 'Cantidad'}

class ventaForm(ModelForm):
    class Meta:
        model = venta
        fields = ['idVenta', 'rutCliente', 'fechaVenta']
        labels = {'idVenta': 'Id Venta', 'rutCliente': 'Rut Cliente', 'fechaVenta': 'Fecha de Venta'}

