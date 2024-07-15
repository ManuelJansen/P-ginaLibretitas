from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('libretas', views.libretas, name='libretas'),
    path('agendas', views.agendas, name='agendas'),
    path('stickers', views.stickers, name='stickers'),
    path('otros', views.otros, name='otros'),
    path('registro', views.registro, name='registro'),
    path('carrito', views.carrito, name='carrito'),
    path('encontrarnos', views.encontrarnos, name='encontrarnos'),
    path('login', views.login, name='login'),

    path('baseDatos', views.baseDatos, name='baseDatos'),

    path('crudCliente', views.crudCliente, name='crudCliente'),
    path('addCliente', views.addCliente, name='addCliente'),
    path('delCliente/<str:pk>', views.delCliente, name='delCliente'),
    path('modCliente/<str:pk>', views.modCliente, name='modCliente'),
    path('clienteUpdate', views.clienteUpdate, name='clienteUpdate'),

    path('crudVentas', views.crudVentas, name='crudVentas'),
    path('addVenta', views.addVenta, name='addVenta'),
    path('delVenta/<str:pk>', views.delVenta, name='delVenta'),
    path('modVenta/<str:pk>', views.modVenta, name='modVenta'),
    path('ventasUpdate', views.ventasUpdate, name='ventasUpdate'),
    
    path('crudDetalle', views.crudDetalle, name='crudDetalle'),
    path('addDetalle', views.addDetalle, name='addDetalle'),

    
]

