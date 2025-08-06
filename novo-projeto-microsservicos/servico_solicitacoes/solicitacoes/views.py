# servico_solicitacoes/solicitacoes/views.py

import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SolicitarServico
# Importe os dois serializers que criamos
from .serializers import SolicitarServicoSerializer, SolicitarServicoCreateSerializer

class SolicitarServicoViewSet(viewsets.ModelViewSet):
    """
    Uma ViewSet para ver e criar Solicitações de Serviço.
    """
    queryset = SolicitarServico.objects.all()

    # Este método mágico escolhe o serializer certo para a ação!
    def get_serializer_class(self):
        if self.action == 'create':
            return SolicitarServicoCreateSerializer  # Usa o serializer simples para POST
        return SolicitarServicoSerializer  # Usa o serializer completo para GET

    # Sobrescrevemos o método 'retrieve' para buscar dados dos outros serviços
    def retrieve(self, request, *args, **kwargs):
        solicitacao = self.get_object() # Pega a solicitação do nosso banco

        try:
            # --- Início da Comunicação entre Microsserviços ---
            url_servico = f"http://servico-servicos:8000/api/servicos/{solicitacao.servico_id}/"
            servico_data = requests.get(url_servico).json()

            url_pessoa = f"http://servico-pessoas:8000/api/pessoas/{solicitacao.pessoa_id}/"
            pessoa_data = requests.get(url_pessoa).json()

            url_produto = f"http://servico-catalogo:8000/api/produtos/{solicitacao.produto_id}/"
            produto_data = requests.get(url_produto).json()
            # --- Fim da Comunicação ---

            # Monta a resposta final e completa para o usuário
            response_data = {
                'id': solicitacao.id,
                'data_solicitacao': solicitacao.data_solicitacao,
                'servico_solicitado': servico_data,
                'solicitante': pessoa_data,
                'produto_associado': produto_data
            }
            return Response(response_data)

        except requests.exceptions.RequestException as e:
            return Response(
                {'error': f'Falha ao buscar dados externos: {e}'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )