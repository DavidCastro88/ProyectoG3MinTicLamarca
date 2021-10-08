from django.db import models
from .user import User


class Tokens(models.Model):
    Idtoken=models.AutoField(primary_key=True , null=False)
    id=models.ForeignKey(User,on_delete=models.CASCADE)
    NombreCompleto=models.CharField(max_length=50, null=False)
    Telefono=models.CharField(max_length=50, null=False)
    email = models.EmailField( max_length = 100)
    RAZONES= [
        (1,"Producto"),
        (2,"Entrega"),
        (3, "Otra")]
    razon=models.IntegerField(null=False, blank=False, choices=RAZONES,default=3)
    comentario=models.TextField(null=False, blank=False, max_length=500)
