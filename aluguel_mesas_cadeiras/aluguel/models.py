from django.db import models

# Create your models here.

class Clientes(models.Model):
    """
    Classe responsavel por salvar as informações dos clientes.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)

class Transação(models.Model):
    """
    Classe responsavel para salvar as informações das transações feitas.

    -- Atributos --
    data_aluguel(datetime): Data que o produto foi alugado
    data_devolução(datetime): Data que o produto foi devolvido
    taxa_de_entrega(float): Taxa de entrega do produto
    valor_total(float): Valor total da transação
    """
    data_aluguel = models.DateTimeField(auto_now_add=True)
    data_devolução = models.DateTimeField(auto_now=True)
    taxa_de_entrega = models.DecimalField(max_digits=7, decimal_places=2)
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    endereco = models.CharField(max_length=100)
    cliente = models.ForeignKey(Clientes, default=None, on_delete=models.CASCADE)
    dano_mesas = models.IntegerField()
    dano_cadeiras = models.IntegerField()

class Mesas(models.Model):
    """
    Classe responsavel por salvar as informações das mesas alugadas.

    -- Atributos --
    estoque(int): Quantidade de mesas disponiveis
    quantidade_alugada(int): Quantidade de mesas alugadas
    transacao(Transação): Transação que a mesa foi alugada
    """
    estoque = models.IntegerField()
    quantidade_alugada = models.IntegerField()
    transacao = models.ForeignKey(Transação, on_delete=models.CASCADE)

class Cadeiras(models.Model):
    """
    Classe responsavel por salvar as informações das cadeiras alugadas.

    -- Atributos --
    estoque(int): Quantidade de cadeiras disponiveis
    quantidade_alugada(int): Quantidade de cadeiras alugadas
    transacao(Transação): Transação que a cadeira foi alugada
    """
    estoque = models.IntegerField()
    quantidade_alugada = models.IntegerField()
    transacao = models.ForeignKey(Transação, on_delete=models.CASCADE)


