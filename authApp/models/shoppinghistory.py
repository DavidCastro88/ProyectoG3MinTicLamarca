from django.db import models
from .user import User
from datetime import datetime,date

class HistorialdeCompras(models.Model):
    Id_Compra = models.AutoField(primary_key=True, null=False)
    id=models.ForeignKey(User,on_delete=models.CASCADE)
    Valor = models.FloatField(null=False, blank=False)  
    Estado = models.CharField(max_length=50, null=False, blank=False) 
    FechadeCompra = models.DateTimeField(auto_now_add=True)