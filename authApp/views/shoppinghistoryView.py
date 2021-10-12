from authApp.models.shoppinghistory import HistorialdeCompras
from authApp.serializers.shoppinghistorySerializer import HistorialdeComprasSerializer
from rest_framework import generics

class HistorialListCreateView(generics.ListCreateAPIView):
    queryset = HistorialdeCompras.objects.all()
    serializer_class = HistorialdeComprasSerializer

class HistorialRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialdeCompras.objects.all()
    serializer_class = HistorialdeComprasSerializer