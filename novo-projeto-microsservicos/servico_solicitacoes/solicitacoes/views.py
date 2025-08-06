from rest_framework import generics
from .models import SolicitarServico
from .serializers import SolicitarServicoSerializer

class SolicitarServicoListCreateView(generics.ListCreateAPIView):
    queryset = SolicitarServico.objects.all()
    serializer_class = SolicitarServicoSerializer

class SolicitarServicoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SolicitarServico.objects.all()
    serializer_class = SolicitarServicoSerializer
