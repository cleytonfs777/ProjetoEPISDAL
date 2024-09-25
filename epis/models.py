from django.db import models


class EPIBase(models.Model):
    possui = models.BooleanField(default=False)
    estadodeconservacao = models.CharField(max_length=10, choices=[
        ('Ótimo', 'Ótimo'), ('Bom', 'Bom'), ('Razoável', 'Razoável'), ('Ruim', 'Ruim')
    ])
    condicao = models.CharField(max_length=2, choices=[
        ('P', 'Procede'), ('NP', 'Não Procede')
    ])
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anofabricacao = models.IntegerField(null=True, blank=True)
    plannumber = models.CharField(max_length=30, null=True, blank=True)
    datapreenchimento = models.DateField(null=True, blank=True)
    recebido = models.BooleanField(default=False, null=True, blank=True)
    datarecebimento = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class ConjuntoEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    jaquetatamanho = models.CharField(max_length=20, choices=[
        ('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande'),
        ('1º Extra Grande', '1º Extra Grande'), ('2º Extra Grande', '2º Extra Grande'),
        ('3º Extra Grande', '3º Extra Grande')
    ])
    jaquetacomplemento = models.IntegerField(
        choices=[(i, str(i)) for i in range(5)])
    calcatamanho = models.CharField(max_length=20, choices=[
        ('Pequeno', 'Pequeno'), ('Médio', 'Médio'), ('Grande', 'Grande'),
        ('1º Extra Grande', '1º Extra Grande'), ('2º Extra Grande', '2º Extra Grande'),
        ('3º Extra Grande', '3º Extra Grande')
    ])
    calcacomplemento = models.IntegerField(
        choices=[(i, str(i)) for i in range(5)])


class CapaceteEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    cor = models.CharField(max_length=50)


class LuvaEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    circunferenciamao = models.CharField(max_length=30, choices=[
        ('12 a 15 cm', '12 a 15 cm'), ('18 a 19 cm', '18 a 19 cm'),
        ('19 a 20 cm', '19 a 20 cm'), ('20 a 21,5 cm', '20 a 21,5 cm'),
        ('21,5 a 23 cm', '21,5 a 23 cm'), ('23 a 25 cm', '23 a 25 cm'),
        ('25 a 28 cm', '25 a 28 cm'), ('28 a 30 cm', '28 a 30 cm')
    ])


class BalaclavaEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    camadas = models.CharField(max_length=10, choices=[
        ('S', 'Simples'), ('D', 'Dupla'), ('T', 'Tripla')
    ])


class BotaEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    tamanho = models.IntegerField(choices=[(i, str(i)) for i in range(35, 51)])


class CapaceteAquaticoEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    cor = models.CharField(max_length=20, choices=[
        ('B', 'Branco'), ('A', 'Amarelo'), ('V', 'Vermelho')
    ])


class CapaceteVeicularEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    cor = models.CharField(max_length=50)


class LuvaVeicularEPI(EPIBase):
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True)
    circunferenciamao = models.CharField(max_length=30, choices=[
        ('12 a 15 cm', '12 a 15 cm'), ('18 a 19 cm', '18 a 19 cm'),
        ('19 a 20 cm', '19 a 20 cm'), ('20 a 21,5 cm', '20 a 21,5 cm'),
        ('21,5 a 23 cm', '21,5 a 23 cm'), ('23 a 25 cm', '23 a 25 cm'),
        ('25 a 28 cm', '25 a 28 cm'), ('28 a 30 cm', '28 a 30 cm')
    ])


class Mensagem(models.Model):
    choices_tipo = (
        ('p', 'Planejamento'),
        ('a', 'Aquisição'),
        ('t', 'Transporte'),
        ('g', 'Geral'),
    )
    msg = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.BooleanField(default=False)
    lida = models.BooleanField(default=False)
    user = models.ForeignKey(
        'usuarios.Users', on_delete=models.CASCADE, null=True, blank=True, related_name='mensagens')

    def __str__(self):
        return self.assunto
