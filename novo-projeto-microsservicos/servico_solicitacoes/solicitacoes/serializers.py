from rest_framework import serializers
from .models import SolicitarServico
import requests
from django.conf import settings

class SolicitarServicoSerializer(serializers.ModelSerializer):
    servico_solicitado = serializers.SerializerMethodField()
    solicitante = serializers.SerializerMethodField()
    produto_associado = serializers.SerializerMethodField()

    class Meta:
        model = SolicitarServico
        fields = ["id", "servico_id", "pessoa_id", "produto_id", "data_solicitacao", "servico_solicitado", "solicitante", "produto_associado"]
        read_only_fields = ["data_solicitacao", "servico_solicitado", "solicitante", "produto_associado"]

    def get_servico_solicitado(self, obj):
        try:
            response = requests.get(f"{settings.BASE_URLS["servicos"]}servicos/{obj.servico_id}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def get_solicitante(self, obj):
        try:
            response = requests.get(f"{settings.BASE_URLS["pessoas"]}pessoas/{obj.pessoa_id}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def get_produto_associado(self, obj):
        try:
            response = requests.get(f"{settings.BASE_URLS["catalogo"]}produtos/{obj.produto_id}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def create(self, validated_data):
        return SolicitarServico.objects.create(**validated_data)


