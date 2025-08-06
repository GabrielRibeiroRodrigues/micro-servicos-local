# servico_solicitacoes/solicitacoes/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SolicitarServicoViewSet

# Cria um roteador
router = DefaultRouter()
# Registra nossa ViewSet com o roteador
router.register(r'solicitacoes', SolicitarServicoViewSet, basename='solicitarservico')

# As URLs da API são agora determinadas automaticamente pelo roteador.
urlpatterns = [
    path('', include(router.urls)),
]