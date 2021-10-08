from authApp.models.tokens import Tokens
from rest_framework import serializers

class tokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tokens
        fields = ["Idtoken","NombreCompleto","Telefono","email","razon","comentario"]
