from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return str(self.nombre)