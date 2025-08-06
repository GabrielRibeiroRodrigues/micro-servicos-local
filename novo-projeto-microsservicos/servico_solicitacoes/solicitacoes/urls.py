from django.urls import path
from .views import SolicitarServicoListCreateView, SolicitarServicoDetailView

urlpatterns = [
    path("solicitacoes/", SolicitarServicoListCreateView.as_view(), name="solicitacao-list-create"),
    path("solicitacoes/<int:pk>/", SolicitarServicoDetailView.as_view(), name="solicitacao-detail"),
]

