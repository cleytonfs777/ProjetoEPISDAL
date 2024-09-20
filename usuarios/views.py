from datetime import date
from django.contrib import auth, messages
from django.http import HttpResponse
from django.urls import reverse

from epis.models import BalaclavaEPI, BotaEPI, CapaceteAquaticoEPI, CapaceteEPI, CapaceteVeicularEPI, ConjuntoEPI, LuvaEPI, LuvaVeicularEPI
from populate.read_militares import ler_arquivo_xlsx
from usuarios.utils import *

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


@login_required
def criar_usuario_ficticio_view(request):

    # Criar o usuário fictício com campos herdados de AbstractUser
    usuario = Users.objects.create(
        username='usuario_ficticio',  # Definir o username
        first_name='João',  # Definir o primeiro nome
        last_name='Silva',  # Definir o sobrenome (opcional)
        email='usuario@exemplo.com',  # Definir um email
        numbm='123456',
        postgrad='3sgt',
        date_include='2024-01-01',
        time_service_days=3650,
        status='A',
        sitfunc='2',
        gto='12345',
        ativ_esp='S',
        list_ativ_esp='Motorresgate',
        cob=5,
        unid_lot='Unidade A',
        unid_princ='Unidade B',
        sexo='M',
        priorit='A'
    )

    # Definir a senha padrão 'cbmmg193' usando o método set_password
    usuario.set_password('cbmmg193')
    usuario.save()  # Salvar o usuário após definir a senha

    # Criar EPIs CIURB
    ConjuntoEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca X',
        modelo='Modelo Y',
        anofabricacao=2020,
        plannumber=1,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        jaquetatamanho='Médio',
        jaquetacomplemento=1,
        calcatamanho='Médio',
        calcacomplemento=1
    )

    CapaceteEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca X',
        modelo='Modelo Y',
        anofabricacao=2020,
        plannumber=1,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        cor='Vermelho'
    )

    ciurb_luva = LuvaEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca X',
        modelo='Modelo Y',
        anofabricacao=2020,
        plannumber=1,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        circunferenciamao='19 a 20 cm'
    )

    ciurb_balaclava = BalaclavaEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca X',
        modelo='Modelo Y',
        anofabricacao=2020,
        plannumber=1,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        camadas='Dupla'
    )

    ciurb_bota = BotaEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca X',
        modelo='Modelo Y',
        anofabricacao=2020,
        plannumber=1,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        tamanho=42
    )

    # Criar EPIs Multimissão
    multi_conjunto = ConjuntoEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca X',
        modelo='Modelo Y',
        anofabricacao=2021,
        plannumber=2,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        jaquetatamanho='Grande',
        jaquetacomplemento=2,
        calcatamanho='Grande',
        calcacomplemento=2
    )

    multi_capacete = CapaceteEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Ótimo',
        condicao='P',
        marca='Marca Z',
        modelo='Modelo W',
        anofabricacao=2021,
        plannumber=2,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        cor='Azul'
    )

    multi_luva = LuvaEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Ótimo',
        condicao='P',
        marca='Marca Y',
        modelo='Modelo X',
        anofabricacao=2021,
        plannumber=2,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        circunferenciamao='20 a 21,5 cm'
    )

    multi_bota = BotaEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca A',
        modelo='Modelo B',
        anofabricacao=2021,
        plannumber=2,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        tamanho=43
    )

    # Criar EPIs Salvamento
    salv_capacete_aqu = CapaceteAquaticoEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca B',
        modelo='Modelo C',
        anofabricacao=2022,
        plannumber=3,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        cor='Amarelo'
    )

    salv_capacete_alt = CapaceteVeicularEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Bom',
        condicao='P',
        marca='Marca D',
        modelo='Modelo E',
        anofabricacao=2022,
        plannumber=3,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        cor='Preto'
    )

    salv_luva_veic = LuvaVeicularEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Razoável',
        condicao='P',
        marca='Marca C',
        modelo='Modelo D',
        anofabricacao=2022,
        plannumber=3,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        circunferenciamao='21,5 a 23 cm'
    )

    # Criar EPIs Motorresgate
    motresg_conjunto = ConjuntoEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Ótimo',
        condicao='P',
        marca='Marca E',
        modelo='Modelo F',
        anofabricacao=2023,
        plannumber=4,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        jaquetatamanho='Extra Grande',
        jaquetacomplemento=3,
        calcatamanho='Extra Grande',
        calcacomplemento=3
    )

    motresg_capacete = CapaceteEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Ótimo',
        condicao='P',
        marca='Marca F',
        modelo='Modelo G',
        anofabricacao=2023,
        plannumber=4,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        cor='Branco'
    )

    motresg_luva = LuvaEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Ótimo',
        condicao='P',
        marca='Marca G',
        modelo='Modelo H',
        anofabricacao=2023,
        plannumber=4,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        circunferenciamao='23 a 25 cm'
    )

    motresg_bota = BotaEPI.objects.create(
        user=usuario,
        possui=True,
        estadodeconservacao='Ótimo',
        condicao='P',
        marca='Marca H',
        modelo='Modelo I',
        anofabricacao=2023,
        plannumber=4,
        datapreenchimento=date.today(),
        recebido=True,
        datarecebimento=date.today(),
        tamanho=44
    )

    # Após a criação, redirecionar ou retornar uma mensagem
    return render(request, 'usuario_criado.html', {'usuario': usuario})


def formatar_data_para_iso(data):
    # Verificar se o dado já está no formato 'YYYY-MM-DD'
    if isinstance(data, str):
        try:
            # Tentar converter a string diretamente para uma data
            # Verificar se já está no formato correto
            datetime.strptime(data, "%Y-%m-%d")
            return data  # Se já está no formato 'YYYY-MM-DD', retornar diretamente
        except ValueError:
            try:
                # Se não estiver no formato 'YYYY-MM-DD', tentar converter do formato 'DD/MM/YYYY'
                data_formatada = datetime.strptime(data, "%d/%m/%Y").date()
                return data_formatada.isoformat()  # Converter para formato ISO 'YYYY-MM-DD'
            except ValueError:
                return None  # Se não conseguir converter, retorna None
    elif isinstance(data, datetime):
        # Se for um objeto datetime, converter para formato ISO
        return data.date().isoformat()
    else:
        return None  # Retornar None se não for nem string nem datetime


@login_required
def popular_lista_usuarios_view(request):

    lista_usuarios = ler_arquivo_xlsx()
    print("LISTA DE USUÁRIOS")
    print(lista_usuarios)

    for usuario in lista_usuarios:
        print("USUARIO DO SISTEMA")
        print(usuario)

        nomefull = separar_nomes(usuario[3])

        atividade = 'I' if usuario[6] == 'Inativo' else 'A'
        situacao = situacao_func(usuario[7])

        cob_unip_unilot = cob_princ_lot(usuario[13])

        "quero uma função que recebe uma string e converte todas as letras"

        # 31 - Marca ou não possui - NÃO POSSUI ou "" (UPPERCASE) # 32 - Ano de Fabricação # 33 - Estado de Conservacao (PROPERCASE) # 17 - Tamanho da jaqueta # 18 - Tamanho da calça
        # Dados de 27 a 30 dizem respeito a capacete
        # Dados de 37 a 39, e 16 (Tamanho da luva) dizem respeito a luva
        # Dados de 40 a 42 dizem respeito a balaclava
        # Dados de 34 a 36, e 14 dizem respeito a bota
        classif_ciurb = [usuario[31], usuario[32],
                         usuario[33], usuario[17], usuario[18], usuario[27], usuario[28], usuario[29], usuario[30], usuario[37], usuario[38], usuario[39], usuario[16], usuario[40], usuario[41], usuario[42], usuario[34], usuario[35], usuario[36], usuario[14]]

        # Dados de 21 a 23 dizem respeito a conjunto de multimissão
        # Dados de 16 diz respeito a tamanho de luva(incendio)
        # Dados de 24 a 26 dizem respeito a bota multimissao # 14 tamano coturno
        classif_multimiss = [usuario[21],
                             usuario[22], usuario[23], usuario[16], usuario[24], usuario[25], usuario[26], usuario[14]]
        # Dados de 43 a 46 dizem respeito a capacete de salvamento em altura
        # Dados de 47 a 49 dizem respeito a luva de salvamento veicular
        classif_salvamento = [usuario[43],
                              usuario[44], usuario[45], usuario[46], usuario[47], usuario[48], usuario[49], usuario[15]]

        # Dados de 16 diz respeito ao tamanho da luva
        classif_motorresgate = [usuario[16], usuario[14]]

        # GERANDO DICIONARIOS DE CADA GRUPO DE EPI
        result_ciurb = generate_ciurb_epi(classif_ciurb)
        result_multimiss = generate_multimiss_epi(classif_multimiss)
        result_salvamento = generate_salvamento_epi(classif_salvamento)
        result_motorresgate = generate_motorresgate_epi(classif_motorresgate)

        # Verifica se o usuario já existe
        username = criar_username(usuario[3])

        if Users.objects.filter(username=username).exists():
            print("Usuario já existe")
            continue  # Pular a criação e retornar

        # Criar o usuário fictício com campos herdados de AbstractUser
        usuario = Users.objects.create(
            username=str(criar_username(usuario[3])),  # Definir o username
            first_name=converter_propercase(
                nomefull[0]),  # Definir o primeiro nome
            # Definir o sobrenome (opcional)
            last_name=converter_propercase(nomefull[1]),
            email=f"{criar_username(usuario[3])}@bombeiros.mg.gov.br",
            numbm=usuario[0],
            postgrad=converter_funtion(usuario[1]),
            date_include=usuario[4],
            time_service_days=dias_desde_data(usuario[4]),
            status=atividade,
            sitfunc=situacao,
            gto='',
            ativ_esp='N',
            list_ativ_esp='',
            cob=cob_unip_unilot[0],
            unid_lot=cob_unip_unilot[1],
            unid_princ=cob_unip_unilot[2],
            sexo=usuario[11] if usuario[11] == 'M' or usuario[11] == 'F' else 'M',
            priorit='',
        )

        # Definir a senha padrão 'cbmmg193' usando o método set_password
        # filipe.oliveira
        usuario.set_password('cbmmg193')
        usuario.save()  # Salvar o usuário após definir a senha

        # Criar EPIs CIURB
        ConjuntoEPI.objects.create(
            user=usuario,
            possui=result_ciurb['possui_conj_ciurb'],
            estadodeconservacao=result_ciurb['estadodeconservacao_conj'],
            condicao='P',
            marca=result_ciurb['marca_conj'],
            modelo=result_ciurb['modelo_conj'],
            anofabricacao=obter_valor(result_ciurb, 'ano_fab_conj', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            jaquetatamanho=result_ciurb['jaquetatamanho'],
            jaquetacomplemento=result_ciurb['jaquetacomplemento'],
            calcatamanho=result_ciurb['calcatamanho'],
            calcacomplemento=result_ciurb['calcacomplemento'],
        )

        CapaceteEPI.objects.create(
            user=usuario,
            possui=result_ciurb['possui_cap_ciurb'],
            estadodeconservacao=result_ciurb['estadodeconservacao_cap'],
            condicao='P',
            marca=result_ciurb['marca_cap'],
            modelo=result_ciurb['modelo_cap'],
            anofabricacao=obter_valor(result_ciurb, 'ano_fab_cap', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            cor=result_ciurb['cor_cap'],
        )

        ciurb_luva = LuvaEPI.objects.create(
            user=usuario,
            possui=result_ciurb['possui_luv_ciurb'],
            estadodeconservacao=result_ciurb['estadodeconservacao_luv'],
            condicao='P',
            marca=result_ciurb['marca_luv'],
            modelo=result_ciurb['modelo_luv'],
            anofabricacao=obter_valor(result_ciurb, 'ano_fab_luv', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            circunferenciamao=result_ciurb['circunferenciamao'],
        )

        ciurb_balaclava = BalaclavaEPI.objects.create(
            user=usuario,
            possui=result_ciurb['possui_bal_ciurb'],
            estadodeconservacao=result_ciurb['estadodeconservacao_bal_ciurb'],
            condicao='P',
            marca=result_ciurb['marca_bal_ciurb'],
            modelo=result_ciurb['modelo_bal_ciurb'],
            anofabricacao=obter_valor(result_ciurb, 'ano_fab_bal_ciurb', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            camadas=result_ciurb['camadas_bal_ciurb'],
        )

        ciurb_bota = BotaEPI.objects.create(
            user=usuario,
            possui=result_ciurb['possui_bot_ciurb'],
            estadodeconservacao=result_ciurb['estadodeconservacao_bot_ciurb'],
            condicao='P',
            marca=result_ciurb['marca_bot_ciurb'],
            modelo=result_ciurb['modelo_bot_ciurb'],
            anofabricacao=obter_valor(result_ciurb, 'ano_fab_bot_ciurb', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            tamanho=obter_valor(result_ciurb, 'numero_bot_cirurb', 39),
        )

        # Criar EPIs Multimissão
        multi_conjunto = ConjuntoEPI.objects.create(
            user=usuario,
            possui=result_multimiss['possui_conj_mult'],
            estadodeconservacao=result_multimiss['estadodeconservacao_conj'],
            condicao='P',
            marca=result_multimiss['marca_conj'],
            modelo=result_multimiss['modelo_conj'],
            anofabricacao=0,
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            jaquetatamanho='',
            jaquetacomplemento=0,
            calcatamanho='',
            calcacomplemento=0,
        )

        multi_capacete = CapaceteEPI.objects.create(
            user=usuario,
            possui=result_multimiss['possui_cap_mult'],
            estadodeconservacao=result_multimiss['estadodeconservacao_cap'],
            condicao='P',
            marca=result_multimiss['marca_cap'],
            modelo=result_multimiss['modelo_cap'],
            anofabricacao=0,
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            cor=result_multimiss['cor_cap'],
        )

        multi_luva = LuvaEPI.objects.create(
            user=usuario,
            possui=result_multimiss['possui_luv_mult'],
            estadodeconservacao=result_multimiss['estadodeconservacao_luv'],
            condicao='P',
            marca=result_multimiss['marca_luv'],
            modelo=result_multimiss['modelo_luv'],
            anofabricacao=0,
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            circunferenciamao=result_multimiss['circunferenciamao_luv'],
        )

        multi_bota = BotaEPI.objects.create(
            user=usuario,
            possui=result_multimiss['possui_bot_mult'],
            estadodeconservacao=result_multimiss['estadodeconservacao_bot'],
            condicao='P',
            marca=result_multimiss['marca_bot'],
            modelo=result_multimiss['modelo_bot'],
            anofabricacao=0,
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            tamanho=obter_valor(result_multimiss, 'tamanho_bot', 39),
        )

        # Criar EPIs Salvamento
        salv_capacete_aqu = CapaceteAquaticoEPI.objects.create(
            user=usuario,
            possui=result_salvamento['possui_cap_aqu'],
            estadodeconservacao=result_salvamento['estadodeconservacao_cap_aqu'],
            condicao='P',
            marca=result_salvamento['marca_cap_aqu'],
            modelo=result_salvamento['modelo_cap_aqu'],
            anofabricacao=obter_valor(
                result_salvamento, 'ano_fab_cap_aqu', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            cor=result_salvamento['cor_cap_aqu'],
        )

        salv_capacete_alt = CapaceteVeicularEPI.objects.create(
            user=usuario,
            possui=result_salvamento['possui_cap_alt'],
            estadodeconservacao=result_salvamento['estadodeconservacao_cap_alt'],
            condicao='P',
            marca=result_salvamento['marca_cap_alt'],
            modelo=result_salvamento['modelo_cap_alt'],
            anofabricacao=obter_valor(
                result_salvamento, 'ano_fab_cap_alt', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            cor=result_salvamento['cor_cap_alt'],
        )

        salv_luva_veic = LuvaVeicularEPI.objects.create(
            user=usuario,
            possui=result_salvamento['possui_luv_veic'],
            estadodeconservacao=result_salvamento['estadodeconservacao_luv_veic'],
            condicao='P',
            marca=result_salvamento['marca_luv_veic'],
            modelo=result_salvamento['modelo_luv_veic'],
            anofabricacao=obter_valor(
                result_salvamento, 'ano_fab_luv_veic', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            circunferenciamao=result_salvamento['circunferenciamao_luv_veic'],
        )

        # Criar EPIs Motorresgate
        motresg_conjunto = ConjuntoEPI.objects.create(
            user=usuario,
            possui=result_motorresgate['possui_conj_motoresg'],
            estadodeconservacao=result_motorresgate['estadodeconservacao_conj_motoresg'],
            condicao='P',
            marca=result_motorresgate['marca_conj_motoresg'],
            modelo=result_motorresgate['modelo_conj_motoresg'],
            anofabricacao=obter_valor(
                result_salvamento, 'ano_fab_conj_motoresg', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            jaquetatamanho='',
            jaquetacomplemento=0,
            calcatamanho='',
            calcacomplemento=0,
        )

        motresg_capacete = CapaceteEPI.objects.create(
            user=usuario,
            possui=result_motorresgate['possui_cap_motoresg'],
            estadodeconservacao=result_motorresgate['estadodeconservacao_cap_motoresg'],
            condicao='P',
            marca=result_motorresgate['marca_cap_motoresg'],
            modelo=result_motorresgate['modelo_cap_motoresg'],
            anofabricacao=obter_valor(
                result_salvamento, 'ano_fab_cap_motoresg', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            cor=result_motorresgate['cor_cap_motoresg'],
        )

        motresg_luva = LuvaEPI.objects.create(
            user=usuario,
            possui=result_motorresgate['possui_luv_motoresg'],
            estadodeconservacao=result_motorresgate['estadodeconservacao_luv_motoresg'],
            condicao='P',
            marca=result_motorresgate['marca_luv_motoresg'],
            modelo=result_motorresgate['modelo_luv_motoresg'],
            anofabricacao=obter_valor(
                result_salvamento, 'ano_fab_luv_motoresg', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            circunferenciamao=result_motorresgate['circunferenciamao_luv_motoresg'],
        )

        motresg_bota = BotaEPI.objects.create(
            user=usuario,
            possui=result_motorresgate['possui_bot_motoresg'],
            estadodeconservacao=result_motorresgate['estadodeconservacao_bot_motoresg'],
            condicao='P',
            marca=result_motorresgate['marca_bot_motoresg'],
            modelo=result_motorresgate['modelo_bot_motoresg'],
            anofabricacao=obter_valor(
                result_salvamento, 'ano_fab_bot_motoresg', 0),
            plannumber='',
            datapreenchimento=date.today(),
            recebido=False,
            datarecebimento=date.today(),
            tamanho=obter_valor(
                result_motorresgate, 'tamanho_bot_motoresg', 0),
        )

    return HttpResponse("Usuarios criados com sucesso!!")


@login_required
def listar_usuarios_view(request):
    # Listar todos os usuários
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
    usuarios = Users.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios, 'gtos': gtos})
