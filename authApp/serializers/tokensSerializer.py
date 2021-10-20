from authApp.models.tokens import Tokens
from rest_framework import serializers

class tokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tokens
        fields = ["id","NombreCompleto","Telefono","email","razon","comentario"]
