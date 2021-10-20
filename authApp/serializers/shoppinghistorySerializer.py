from authApp.models.shoppinghistory import HistorialdeCompras
from rest_framework import serializers

class HistorialdeComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model=HistorialdeCompras
        fields=["id","Valor","Estado"]

