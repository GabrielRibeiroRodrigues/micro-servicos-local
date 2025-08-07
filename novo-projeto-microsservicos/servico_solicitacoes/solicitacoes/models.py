# servico_solicitacoes/solicitacoes/models.py

from django.db import models

class SolicitarServico(models.Model):
    servico_id = models.IntegerField()
    pessoa_id = models.IntegerField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    # O campo produto_id foi REMOVIDO daqui.

class ItemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(SolicitarServico, related_name='itens', on_delete=models.CASCADE)
    produto_id = models.IntegerField()
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Produto {self.produto_id} na Solicitacao {self.solicitacao.id}"