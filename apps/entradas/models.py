from django.db import models

from apps.productos.models import Producto

# Create your models here.

class Entrada(models.Model):
    fecha = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=30)
    valor = models.CharField(max_length=30)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha)