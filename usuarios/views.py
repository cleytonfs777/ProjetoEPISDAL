from django.contrib import auth, messages
from django.http import HttpResponse
from django.urls import reverse

from .models import Users

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserCreationForm
from epis.forms import (
    ConjuntoEPIForm, CapaceteEPIForm, LuvaEPIForm, BalaclavaEPIForm,
    BotaEPIForm, CapaceteAquaticoEPIForm, CapaceteVeicularEPIForm,
    LuvaVeicularEPIForm
)
from .models import Users


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

choices_postgrad = (('sd2cl', 'Sd 2ª Classe BM'),
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


def is_admin(user):
    return user.is_authenticated and user.cargo == 'A'


def authenticate_username_or_email(username, password):
    try:
        user = Users.objects.get(username=username)
    except Users.DoesNotExist:
        try:
            user = Users.objects.get(email=username)
        except Users.DoesNotExist:
            return None

    if user.check_password(password):
        return user


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return render(request, 'login.html')
    elif request.method == "POST":
        username_or_email = request.POST.get('username')
        senha = request.POST.get('password')

        print(username_or_email, senha)

    user = authenticate_username_or_email(username_or_email, senha)

    if not user:
        messages.add_message(request, messages.ERROR,
                             "O usuário e/ou a senha estão incorretos")
        return redirect(reverse('login'))

    auth.login(request, user)
    return redirect(reverse('home'))


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


@login_required
def home(request):
    user = request.user
    gtos = [
        "Atendimento a Tentativa de Suicídio",
        "Atendimento Pré-Hospitalar",
        "Busca e Resgate em Estruturas Colapsadas",
        "Busca, Resgate e Salvamento com Cães",
        "Classificação Internacional",
        "Incêndio Florestal",
        "Incêndio Urbano",
        "Investigação de Incêndio",
        "Mergulho Autônomo / Salvamento Aquático",
        "Movimentos de Massas, Enchentes e Inundações",
        "Produtos Perigosos",
        "Proteção e Defesa Civil",
        "Salvamento em Altura",
        "Salvamento Terrestre",
        "Salvamento Veicula"
    ]

    return render(request, 'home.html', {'user': user, 'choices_sitfunc': choices_sitfunc, 'gtos': gtos})


@login_required
@user_passes_test(is_admin)
def create_user_and_epis(request):
    if request.method == 'POST':
        return HttpResponse('OK')

    else:
        gtos = [
            "Atendimento a Tentativa de Suicídio",
            "Atendimento Pré-Hospitalar",
            "Busca e Resgate em Estruturas Colapsadas",
            "Busca, Resgate e Salvamento com Cães",
            "Classificação Internacional",
            "Incêndio Florestal",
            "Incêndio Urbano",
            "Investigação de Incêndio",
            "Mergulho Autônomo / Salvamento Aquático",
            "Movimentos de Massas, Enchentes e Inundações",
            "Produtos Perigosos",
            "Proteção e Defesa Civil",
            "Salvamento em Altura",
            "Salvamento Terrestre",
            "Salvamento Veicula"
        ]
        return render(request, 'create_user.html', {'choices_postgrad': choices_postgrad, 'choices_sitfunc': choices_sitfunc, 'gtos': gtos})
