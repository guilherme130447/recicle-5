from django.contrib.auth.models import User
from django.db import models

TIPO_CHOICES = (
    ("coletor", "Coletor"),
    ("consumidor", "Consumidor"),
    ("colaborador", "Colaborador"),
)


class ItemModel(models.Model):

    nome = models.CharField(verbose_name="Item", max_length=50)

    descricao = models.CharField(
        verbose_name="Descrição do item", blank=True, max_length=50
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return self.item_name


class EnderecoModel(models.Model):
    empresa = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    itens_trabalhados = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Coletor"
        verbose_name_plural = "Coletores"

    def __str__(self):

        return f"Coletor(a): {self.empresa}"


class Endereco(models.Model):

    logradouro = models.CharField(verbose_name="Logradouro", max_length=255, blank=True)

    numero = models.CharField(
        verbose_name="Número", max_length=5, default="s/n", blank=True
    )

    complemento = models.CharField(
        verbose_name="Complemento", max_length=255, blank=True
    )

    bairro = models.CharField(verbose_name="Bairro", max_length=50, blank=True)

    cidade = models.CharField(verbose_name="Cidade", max_length=50, blank=True)

    estado = models.CharField(verbose_name="Estado", max_length=2, blank=True)

    cep = models.CharField(verbose_name="CEP", max_length=8, blank=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.bairro}, {self.cidade}"


class PessoaModel(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    tipo = models.CharField(
        verbose_name="Tipo de usuário",
        max_length=11,
        choices=TIPO_CHOICES,
        default="consumidor",
    )

    endereco = models.OneToOneField(
        Endereco, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        abstract = True


class ColetorModel(PessoaModel):

    coleta_a_domicilio = models.BooleanField(
        verbose_name="Coleta a domicílio", default=False
    )

    coleta_em_toda_cidade = models.BooleanField(
        verbose_name="Coleta em toda a cidade", default=False
    )

    trabalha_descarte = models.BooleanField(
        verbose_name="Trabalha com descarte", default=False
    )

    trabalha_doacao = models.BooleanField(
        verbose_name="Trabalha com doação", default=False
    )

    itens_trabalhados = models.ManyToManyField(ItemModel)

    tipo = models.CharField(
        verbose_name="Tipo de usuário",
        max_length=11,
        choices=TIPO_CHOICES,
        default="coletor",
    )

    class Meta:
        verbose_name = "Coletor"
        verbose_name_plural = "Coletores"

    def __str__(self):
        return f"Coletor(a): {self.usuario.username}"


class Consumidor(PessoaModel):

    favoritos = models.ManyToManyField(EnderecoModel)

    class Meta:
        verbose_name = "Consumidor"
        verbose_name_plural = "Consumidores"

    def __str__(self):
        return f"Consumidor(a): {self.user.username}"


class Colaborador(PessoaModel):

    tipo = models.CharField(
        verbose_name="Tipo de usuário",
        max_length=11,
        choices=TIPO_CHOICES,
        default="colaborador",
    )

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return f"Colaborador(a): {self.user.username}"
