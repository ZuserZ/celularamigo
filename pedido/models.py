from django.db import models
from django.db import models
from cliente.models import Cliente
from produto.models import Produto  # Se necessário

# Create your models here.

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.TextField()  # Lista de produtos em formato texto ou JSON
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - Cliente {self.cliente.nome}"
