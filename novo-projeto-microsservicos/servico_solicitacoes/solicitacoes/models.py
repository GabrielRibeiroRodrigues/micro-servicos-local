from django.db import models

class SolicitarServico(models.Model):
    servico_id = models.IntegerField()
    pessoa_id = models.IntegerField()
    produto_id = models.IntegerField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação {self.id} - Serviço: {self.servico_id}, Pessoa: {self.pessoa_id}, Produto: {self.produto_id}"
