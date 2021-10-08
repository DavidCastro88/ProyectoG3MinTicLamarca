from authApp.models.shoppinghistory import HistorialdeCompras
from rest_framework import serializers

class HistorialdeComprasSerializer(serializers.Serializer):
    class Meta:
        model=HistorialdeCompras
        fields=["Id_compra","Valor","Estado","Fecha de compra"]

