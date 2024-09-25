from django.contrib.auth.models import AbstractUser
from django.db import models

# TODO: Adicionar prioridades por categorias


class Users(AbstractUser):
    postgrad_choices = (
        ('sd2cl', 'Sd 2ª Classe BM'),
        ('sd', 'Sd BM'),
        ('cb', 'Cb BM'),
        ('3sgt', '3º Sgt BM'),
        ('2sgt', '2º Sgt BM'),
        ('1sgt', '1º Sgt BM'),
        ('subten', 'Sub Ten BM'),
        ('2ten', '2º Ten BM'),
        ('1ten', '1º Ten BM'),
        ('cap', 'Cap BM'),
        ('maj', 'Maj BM'),
        ('tencel', 'Ten Cel BM'),
        ('cel', 'Cel BM'),
    )

    choices_status = (('A', 'Ativo'),
                      ('I', 'Inativo'),)

    choice_sitfunc = (('1', 'ATIVIDADE MEIO'),
                      ('2', 'ATIVID.FIM NA SEDE'),
                      ('3', 'ATIVID.FIM DESTACADO'),
                      ('4', 'MATRICULADO EM CURSO'),
                      ('5', 'RESERVA NAO REMUNERA'),
                      ('6', 'RES. TEMPO SERVICO'),
                      ('7', 'RES.TEMPO EFET. SERV'),
                      ('8', 'RES.LIMITE IDADE'),
                      ('9', 'RESERVA CARGO ELETIV'),
                      ('10', 'RESERVA CARGO PUBLIC'),
                      ('11', 'REFORMA LIMITE IDADE'),
                      ('12', 'REFORMA INCAP.FISICA'),
                      ('13', 'REFORMA DISCIPLINAR'),
                      ('14', 'EXCLUIDO'),
                      ('15', 'QOR DESIGNADO'),
                      ('16', 'LIC.TRAT.PROP.SAUDE'),
                      ('17', 'LIC.TRAT.PES.FAMILIA'),
                      ('18', 'LIC.INTERESSE PARTIC'),
                      ('19', 'AGREG.FIL.PART.POLIT'),
                      ('20', 'AGREG.EXCEDER QUADRO'),
                      ('21', 'DESERTOR'),
                      ('22', 'AGREG. DISP.ORG.PUBL'),
                      ('23', 'AGREG. EXTRAVIO'),
                      ('24', 'AFAST.AG.TRANSF.INAT'),
                      ('25', 'AG.CARGO PUB.S/VENC.'),
                      ('26', 'AGREG.SUSP.EX.FUNCAO'),
                      ('27', 'AGREG.CUMP SENT PENA'),
                      ('28', 'AG. ELEICAO ANTES 98'),
                      ('29', 'CONDENADO PREST.SERV'),
                      ('30', 'PRESO A DISP JUSTICA'),
                      ('31', 'SUBMETIDO A CJ'),
                      ('32', 'APOSENTADO'),
                      ('33', 'JUIZ / TJM'),
                      ('34', 'F.C.DISP.FUN.PUBLICA'),
                      ('35', 'INAT VENC OUT ORGAOS'),
                      ('36', 'FERIAS'),
                      ('37', 'FC AG. APOSENTADORIA'),
                      ('38', 'LICENCA A GESTANTE'),
                      ('39', 'PERDA DO POSTO/GRAD'),
                      ('40', 'REF.VOLUNT. QOR/QPR'),
                      ('41', 'REF.LIM.IDAD.QOR/QPR'),
                      ('42', 'INAT PRESO/JUSTICA'),
                      ('43', 'F.C.DISP.OUTRO ORGAO'),
                      ('44', 'REFORMA P/ INVALIDEZ'),
                      ('45', 'QPR DESIGNADO'),
                      ('46', 'AG LIC.SAU.SUP 1 ANO'),
                      ('47', 'QUADRO ESPECIALISTA'),
                      ('48', 'CONDENADO/SEM SERVI'),
                      ('49', 'PRESO JUST/SEM SERV'),
                      ('50', 'INATIVA'),
                      ('51', 'ART.12/EC 39/1999'),
                      ('52', 'DISP CAUTELAR'),
                      ('53', 'AG.CARGO PUB.C/VENC.'),
                      ('54', 'PRACA ADIDO.AG.REF'),
                      ('55', 'OFICIAL ADIDO AG REF'),
                      ('56', 'PARCIALMENTE CAPAZ'),
                      ('57', 'INTERD.JUDIC.-ATIVO'),
                      ('58', 'AGR.ELEICAO POS 1998'),
                      ('59', 'AGREGA ENTID. CLASSE'),
                      ('60', 'MAT CURSO FORA CBMMG'),
                      ('61', 'OFICIAL AG. 393 CPPM'),
                      ('62', 'AG.ART.134/L.5301/69'),
                      ('63', 'LIC.MED. NAO HOMOLOG'),
                      ('64', 'AFASTADO JUDIC CBMMG'),
                      ('65', 'REFORMA INTERDIÃO'),
                      ('66', 'EX BM C/PROVENTO JUD'),
                      ('67', 'PESSOAL DA SAUDE'),
                      ('68', 'AGRG. DEC. JUDICIAL'),
                      ('69', 'FUNCIONARIO CIVIL'),
                      ('70', 'FORÇA NACIONAL'),
                      )

    choices_cargo = (('A', 'Administrador'),
                     ('M', 'Militar'))

    choices_nicnarc = (('NI', 'Nic'),
                       ('NA', 'Narc'))

    choice_motoresg = (('S', 'Sim'),
                       ('N', 'Nao'))

    choice_priorit = (('1', '1ª Prioridade'),
                      ('2', '2ª Prioridade'),
                      ('3', '3ª Prioridade'),
                      ('4', '4ª Prioridade'))

    choice_sexo = (('M', 'Masculino'),
                   ('F', 'Feminino'))

    choices_sitfunc = (('1', 'ATIVIDADE MEIO'),
                       ('2', 'ATIVID.FIM NA SEDE'),
                       ('3', 'ATIVID.FIM DESTACADO'),
                       ('4', 'MATRICULADO EM CURSO'),
                       ('5', 'RESERVA NAO REMUNERA'),
                       ('6', 'RES. TEMPO SERVICO'),
                       ('7', 'RES.TEMPO EFET. SERV'),
                       ('8', 'RES.LIMITE IDADE'),
                       ('9', 'RESERVA CARGO ELETIV'),
                       ('10', 'RESERVA CARGO PUBLIC'),
                       ('11', 'REFORMA LIMITE IDADE'),
                       ('12', 'REFORMA INCAP.FISICA'),
                       ('13', 'REFORMA DISCIPLINAR'),
                       ('14', 'EXCLUIDO'),
                       ('15', 'QOR DESIGNADO'),
                       ('16', 'LIC.TRAT.PROP.SAUDE'),
                       ('17', 'LIC.TRAT.PES.FAMILIA'),
                       ('18', 'LIC.INTERESSE PARTIC'),
                       ('19', 'AGREG.FIL.PART.POLIT'),
                       ('20', 'AGREG.EXCEDER QUADRO'),
                       ('21', 'DESERTOR'),
                       ('22', 'AGREG. DISP.ORG.PUBL'),
                       ('23', 'AGREG. EXTRAVIO'),
                       ('24', 'AFAST.AG.TRANSF.INAT'),
                       ('25', 'AG.CARGO PUB.S/VENC.'),
                       ('26', 'AGREG.SUSP.EX.FUNCAO'),
                       ('27', 'AGREG.CUMP SENT PENA'),
                       ('28', 'AG. ELEICAO ANTES 98'),
                       ('29', 'CONDENADO PREST.SERV'),
                       ('30', 'PRESO A DISP JUSTICA'),
                       ('31', 'SUBMETIDO A CJ'),
                       ('32', 'APOSENTADO'),
                       ('33', 'JUIZ / TJM'),
                       ('34', 'F.C.DISP.FUN.PUBLICA'),
                       ('35', 'INAT VENC OUT ORGAOS'),
                       ('36', 'FERIAS'),
                       ('37', 'FC AG. APOSENTADORIA'),
                       ('38', 'LICENCA A GESTANTE'),
                       ('39', 'PERDA DO POSTO/GRAD'),
                       ('40', 'REF.VOLUNT. QOR/QPR'),
                       ('41', 'REF.LIM.IDAD.QOR/QPR'),
                       ('42', 'INAT PRESO/JUSTICA'),
                       ('43', 'F.C.DISP.OUTRO ORGAO'),
                       ('44', 'REFORMA P/ INVALIDEZ'),
                       ('45', 'QPR DESIGNADO'),
                       ('46', 'AG LIC.SAU.SUP 1 ANO'),
                       ('47', 'QUADRO ESPECIALISTA'),
                       ('48', 'CONDENADO/SEM SERVI'),
                       ('49', 'PRESO JUST/SEM SERV'),
                       ('50', 'INATIVA'),
                       ('51', 'ART.12/EC 39/1999'),
                       ('52', 'DISP CAUTELAR'),
                       ('53', 'AG.CARGO PUB.C/VENC.'),
                       ('54', 'PRACA ADIDO.AG.REF'),
                       ('55', 'OFICIAL ADIDO AG REF'),
                       ('56', 'PARCIALMENTE CAPAZ'),
                       ('57', 'INTERD.JUDIC.-ATIVO'),
                       ('58', 'AGR.ELEICAO POS 1998'),
                       ('59', 'AGREGA ENTID. CLASSE'),
                       ('60', 'MAT CURSO FORA CBMMG'),
                       ('61', 'OFICIAL AG. 393 CPPM'),
                       ('62', 'AG.ART.134/L.5301/69'),
                       ('63', 'LIC.MED. NAO HOMOLOG'),
                       ('64', 'AFASTADO JUDIC CBMMG'),
                       ('65', 'REFORMA INTERDIÃO'),
                       ('66', 'EX BM C/PROVENTO JUD'),
                       ('67', 'PESSOAL DA SAUDE'),
                       ('68', 'AGRG. DEC. JUDICIAL'),
                       ('69', 'FUNCIONARIO CIVIL'),
                       ('70', 'FORÇA NACIONAL'),
                       )

    cargo = models.CharField(max_length=1, choices=choices_cargo, default='M')
    numbm = models.CharField(max_length=50, null=True, blank=True)
    postgrad = models.CharField(
        max_length=10, choices=postgrad_choices, null=True, blank=True)
    date_include = models.DateField(null=True, blank=True)
    time_service_days = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=1, choices=choices_status, default='A')
    sitfunc = models.CharField(
        max_length=2, choices=choices_sitfunc, default='2')
    gto = models.CharField(max_length=200, null=True, blank=True)
    ativ_esp = models.CharField(
        max_length=1, choices=choice_motoresg, default='N')
    list_ativ_esp = models.CharField(max_length=200, null=True, blank=True)
    cob = models.IntegerField(null=True, blank=True)
    unid_lot = models.CharField(max_length=100, null=True, blank=True)
    unid_princ = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=choice_sexo, default='M')
    emailfunc = models.EmailField(null=True, blank=True)
    priorit = models.CharField(
        max_length=1, choices=choice_priorit, default='B', null=True, blank=True)

    # CIURB
    ciurb_conjunto = models.OneToOneField(
        'epis.ConjuntoEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='ciurb_conjunto')
    ciurb_capacete = models.OneToOneField(
        'epis.CapaceteEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='ciurb_capacete')
    ciurb_luva = models.OneToOneField(
        'epis.LuvaEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='ciurb_luva')
    ciurb_balaclava = models.OneToOneField(
        'epis.BalaclavaEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='ciurb_balaclava')
    ciurb_bota = models.OneToOneField(
        'epis.BotaEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='ciurb_bota')

    # MULTIMISSAO
    multi_conjunto = models.OneToOneField(
        'epis.ConjuntoEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='multi_conjunto')
    multi_capacete = models.OneToOneField(
        'epis.CapaceteEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='multi_capacete')
    multi_luva = models.OneToOneField(
        'epis.LuvaEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='multi_luva')
    multi_bota = models.OneToOneField(
        'epis.BotaEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='multi_bota')

    # SALVAMENTO
    salv_capacete_aqu = models.OneToOneField(
        'epis.CapaceteAquaticoEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='salv_capacete_aqu')
    salv_capacete_alt = models.OneToOneField(
        'epis.CapaceteVeicularEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='salv_capacete_alt')
    salv_luva_veic = models.OneToOneField(
        'epis.LuvaVeicularEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='salv_luva_veic')

    # MOTORRESGATE
    motresg_conjunto = models.OneToOneField(
        'epis.ConjuntoEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='motresg_conjunto')
    motresg_capacete = models.OneToOneField(
        'epis.CapaceteEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='motresg_capacete')
    motresg_luva = models.OneToOneField(
        'epis.LuvaEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='motresg_luva')
    motresg_bota = models.OneToOneField(
        'epis.BotaEPI', on_delete=models.SET_NULL, null=True, blank=True, related_name='motresg_bota')

    def __str__(self):
        return self.username
