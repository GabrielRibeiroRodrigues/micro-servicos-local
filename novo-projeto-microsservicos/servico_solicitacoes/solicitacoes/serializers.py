# servico_solicitacoes/solicitacoes/serializers.py

from rest_framework import serializers
from .models import SolicitarServico
import requests
from django.conf import settings

# --- NOVO SERIALIZER APENAS PARA CRIAÇÃO (POST) ---
# Este serializer é simples e aceita apenas os IDs para criar uma nova solicitação.
class SolicitarServicoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitarServico
        fields = ["servico_id", "pessoa_id", "produto_id"]


# --- SERIALIZER PRINCIPAL PARA LEITURA (GET) ---
# Este serializer é focado em exibir os dados completos, buscando as informações nos outros microsserviços.
class SolicitarServicoSerializer(serializers.ModelSerializer):
    servico_solicitado = serializers.SerializerMethodField()
    solicitante = serializers.SerializerMethodField()
    produto_associado = serializers.SerializerMethodField()

    class Meta:
        model = SolicitarServico
        # Note que não mostramos mais os IDs crus, apenas os objetos completos.
        fields = ["id", "data_solicitacao", "servico_solicitado", "solicitante", "produto_associado"]

    def get_servico_solicitado(self, obj):
        try:
            # CORREÇÃO: Usar aspas simples ' ' dentro da f-string.
            url = f"{settings.BASE_URLS['servicos']}servicos/{obj.servico_id}/"
            response = requests.get(url)
            response.raise_for_status()  # Lança um erro para respostas 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException:
            return {"error": f"Serviço com id {obj.servico_id} não encontrado ou indisponível."}

    def get_solicitante(self, obj):
        try:
            # CORREÇÃO: Usar aspas simples ' ' dentro da f-string.
            url = f"{settings.BASE_URLS['pessoas']}pessoas/{obj.pessoa_id}/"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return {"error": f"Pessoa com id {obj.pessoa_id} não encontrada ou indisponível."}

    def get_produto_associado(self, obj):
        try:
            # CORREÇÃO: Usar aspas simples ' ' dentro da f-string.
            url = f"{settings.BASE_URLS['catalogo']}produtos/{obj.produto_id}/"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return {"error": f"Produto com id {obj.produto_id} não encontrado ou indisponível."}