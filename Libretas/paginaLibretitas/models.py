from django.db import models

# Create your models here.

class producto(models.Model):
    idProducto     = models.CharField(primary_key=True, max_length=2)
    tipoProducto   = models.CharField(max_length=40, null=False)
    nombreProducto = models.CharField(max_length=100, null=False)
    precioProducto = models.CharField(max_length=5, null=False)
    imagenProducto = models.ImageField(upload_to='imagenes/', null=False)
    stockProducto  = models.IntegerField()

    def __str__(self):
        return f"{self.nombreProducto}"


class cliente(models.Model):
    rutCliente             = models.CharField(primary_key=True, max_length=20)
    nombreCliente          = models.CharField(max_length=100)
    emailCliente           = models.EmailField(unique=True, max_length=50)
    direccionCliente       = models.CharField(max_length=100)
    fechaNacimientoCliente = models.DateField(blank=False, null=False)
    contraseña             = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.rutCliente}"

class venta(models.Model):
    idVenta    = models.CharField(primary_key=True, max_length=2)
    rutCliente = models.ForeignKey('cliente', on_delete=models.CASCADE, db_column='rutCliente')
    fechaVenta = models.DateField(blank=False, null=False)

    def __str__(self):
        return f"{self.idVenta}"

    

class detalleVenta(models.Model):
    idVenta    = models.ForeignKey('venta', on_delete=models.CASCADE, db_column='idVenta')
    idProducto = models.ForeignKey('producto', on_delete=models.CASCADE, db_column='idProducto')
    cantidad   = models.IntegerField()

    