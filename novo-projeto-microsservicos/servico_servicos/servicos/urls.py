from django.urls import path
from .views import ServicoListCreateView, ServicoDetailView

urlpatterns = [
    path("servicos/", ServicoListCreateView.as_view(), name="servico-list-create"),
    path("servicos/<int:pk>/", ServicoDetailView.as_view(), name="servico-detail"),
]

