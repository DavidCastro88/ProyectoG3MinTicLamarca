from authApp.models.tokens import Tokens
from authApp.serializers.tokensSerializer import tokenSerializer
from rest_framework import generics

class TokenListCreateView(generics.ListCreateAPIView):
    queryset = Tokens.objects.all()
    serializer_class = tokenSerializer

class TokenRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tokens.objects.all()
    serializer_class = tokenSerializer