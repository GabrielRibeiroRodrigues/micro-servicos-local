from rest_framework import generics
from .models import Servico
from .serializers import ServicoSerializer

class ServicoListCreateView(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
