from django.urls import path
from .views import CategoriaListCreateView, CategoriaDetailView, ProdutoListCreateView, ProdutoDetailView

urlpatterns = [
    path("categorias/", CategoriaListCreateView.as_view(), name="categoria-list-create"),
    path("categorias/<int:pk>/", CategoriaDetailView.as_view(), name="categoria-detail"),
    path("produtos/", ProdutoListCreateView.as_view(), name="produto-list-create"),
    path("produtos/<int:pk>/", ProdutoDetailView.as_view(), name="produto-detail"),
]

