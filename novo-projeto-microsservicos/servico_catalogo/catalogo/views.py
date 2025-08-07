from rest_framework import generics
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework import viewsets
    
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    # Adicione ou modifique este método
    def get_queryset(self):
        """
        Permite filtrar produtos por uma lista de IDs.
        Exemplo: /api/produtos/?ids=1,3,5
        """
        queryset = Produto.objects.all()
        ids = self.request.query_params.get('ids')
        if ids is not None:
            # Pega a string '1,3,5', quebra em uma lista ['1','3','5'] e filtra
            id_list = ids.split(',')
            queryset = queryset.filter(pk__in=id_list)
        return queryse
