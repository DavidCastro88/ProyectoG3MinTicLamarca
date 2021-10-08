from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)  
    precio = models.FloatField(null=False, blank=False)
    