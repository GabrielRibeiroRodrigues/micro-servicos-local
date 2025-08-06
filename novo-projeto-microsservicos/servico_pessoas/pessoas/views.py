from rest_framework import generics
from .models import Pessoa
from .serializers import PessoaSerializer

class PessoaListCreateView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
