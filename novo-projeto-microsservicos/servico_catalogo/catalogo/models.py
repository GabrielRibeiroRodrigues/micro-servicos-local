from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_categoria

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto
