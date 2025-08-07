# servico_solicitacoes/solicitacoes/serializers.py

from rest_framework import serializers
from .models import SolicitarServico, ItemSolicitacao
import requests
from django.conf import settings
from django.db import transaction # Import para transações

# --- Serializer para os Itens ---
class ItemSolicitacaoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSolicitacao
        fields = ['produto_id', 'quantidade']

class ItemSolicitacaoSerializer(serializers.ModelSerializer):
    produto = serializers.SerializerMethodField()
    class Meta:
        model = ItemSolicitacao
        fields = ['produto_id', 'quantidade', 'produto']

    def get_produto(self, obj):
      # Este método será chamado pelo serializer principal, que já terá os dados dos produtos
      produtos_data = self.context.get('produtos_data', {})
      return produtos_data.get(str(obj.produto_id))

# --- Serializer para CRIAR a Solicitação ---
class SolicitarServicoCreateSerializer(serializers.ModelSerializer):
    itens = ItemSolicitacaoCreateSerializer(many=True)

    class Meta:
        model = SolicitarServico
        fields = ['servico_id', 'pessoa_id', 'itens']

    def create(self, validated_data):
        # Usamos uma transação para garantir que tudo seja salvo junto ou nada seja salvo
        with transaction.atomic():
            itens_data = validated_data.pop('itens')
            solicitacao = SolicitarServico.objects.create(**validated_data)
            for item_data in itens_data:
                ItemSolicitacao.objects.create(solicitacao=solicitacao, **item_data)
            return solicitacao

# --- Serializer para LER a Solicitação ---
class SolicitarServicoSerializer(serializers.ModelSerializer):
    servico_solicitado = serializers.SerializerMethodField()
    solicitante = serializers.SerializerMethodField()
    itens = serializers.SerializerMethodField()

    class Meta:
        model = SolicitarServico
        fields = ["id", "data_solicitacao", "servico_solicitado", "solicitante", "itens"]

    def get_servico_solicitado(self, obj):
        try:
            url = f"{settings.BASE_URLS['servicos']}servicos/{obj.servico_id}/"
            return requests.get(url).json()
        except requests.exceptions.RequestException:
            return None

    def get_solicitante(self, obj):
        try:
            url = f"{settings.BASE_URLS['pessoas']}pessoas/{obj.pessoa_id}/"
            return requests.get(url).json()
        except requests.exceptions.RequestException:
            return None

    def get_itens(self, obj):
        # 1. Pega todos os IDs dos produtos desta solicitação
        produto_ids = [str(item.produto_id) for item in obj.itens.all()]
        if not produto_ids:
            return []

        # 2. Faz UMA ÚNICA chamada de API para buscar todos os produtos
        try:
            ids_string = ','.join(produto_ids)
            url = f"{settings.BASE_URLS['catalogo']}produtos/?ids={ids_string}"
            response = requests.get(url)
            response.raise_for_status()
            produtos_data = {str(p['id']): p for p in response.json()} # Transforma a lista em um dicionário para busca rápida
        except requests.exceptions.RequestException:
            produtos_data = {}
            
        # 3. Usa o ItemSolicitacaoSerializer para montar a resposta final,
        # passando os dados dos produtos que já buscamos no "contexto"
        serializer = ItemSolicitacaoSerializer(
            obj.itens.all(), 
            many=True,
            context={'produtos_data': produtos_data}
        )
        return serializer.data