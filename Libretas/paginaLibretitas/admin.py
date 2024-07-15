from django.contrib import admin
from .models import producto, cliente, venta, detalleVenta
# Register your models here.

admin.site.register(producto)
admin.site.register(cliente)
admin.site.register(venta)
admin.site.register(detalleVenta)
