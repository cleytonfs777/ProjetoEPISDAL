
from datetime import datetime
import re

TABLE_LUV = [('5 - XXS', '12 a 15 cm'), ('6 - XS', '18 a 19 cm'), ('7 - S', '19 a 20 cm'), ('8 - M', '20 a 21,5 cm'),
             ('9 - L', '21,5 a 23 cm'), ('10 - XL', '23 a 25 cm'), ('11 - XXL', '25 a 28 cm'), ('12 - 3X', '28 a 30 cm')]


def proper_case_last_word(s):
    # Realiza o split da string
    words = s.split(" ")
    # Pega a última palavra
    last_word = words[-1]
    # Aplica o método title() para deixar apenas a primeira letra maiúscula
    return last_word.title()


def extrair_medida(input_str):
    # Define o padrão regex: um ou mais dígitos, espaço, 'a', espaço, um ou mais dígitos e ' cm'
    padrao = r'\d+ a \d+cm'

    # Busca pelo padrão na string
    resultado = re.search(padrao, input_str)

    print("dados extraidos de luvs: ", resultado)

    # Retorna o resultado se encontrado, senão retorna None
    return resultado.group(0) if resultado else ''


def separar_lista(input_str):
    # Divide a string com base no separador " - " e remove espaços em branco com strip()
    valores = [valor.strip() for valor in input_str.split(' - ')]
    return valores


def extrair_primeiro_elemento(string):
    # Verifica se existe "/"
    if '/' in string:
        # Retorna o texto antes da primeira "/"
        return string.split('/')[0].strip()
    else:
        # Expressão regular para remover "VETERANOS DO/DA" ou "EXCLUIDOS DO/DA"
        regex = r"(VETERANOS DO|VETERANOS DA|EXCLUIDOS DO|EXCLUIDOS DA)"
        # Remover o padrão da string
        string_modificada = re.sub(regex, '', string).strip()
        # Se após remover o texto a string ainda possuir conteúdo, retorna, senão retorna vazio
        return string_modificada if string_modificada else ''


def separar_nomes(nomes_string):
    # Remover espaços desnecessários e separar os nomes por espaço
    nomes_lista = [nome.strip() for nome in nomes_string.split(',')]

    # Dividir cada nome completo em duas partes: primeiro nome e restante
    nomes_separados = []
    for nome in nomes_lista:
        partes = nome.split()
        primeiro_nome = partes[0]  # O primeiro nome
        sobrenome = ' '.join(partes[1:])  # O restante
        nomes_separados.append([primeiro_nome, sobrenome])

    return nomes_separados[0]


def criar_username(nomes_string):
    # Remover espaços desnecessários e separar os nomes por vírgula
    nomes_lista = [nome.strip() for nome in nomes_string.split(',')]

    usernames = []
    for nome in nomes_lista:
        partes = nome.split()
        # O primeiro nome em letras minúsculas
        primeiro_nome = partes[0].lower()
        ultimo_nome = partes[-1].lower()   # O último nome em letras minúsculas
        username = f"{primeiro_nome}.{ultimo_nome}"  # Concatenar com um ponto
        usernames.append(username)

    return usernames[0]


def dias_desde_data(data_str):
    # Converter a string para um objeto datetime
    data_fornecida = data_str

    # Conveter apenas para anos

    # Obter a data atual
    data_atual = datetime.now()

    # Calcular a diferença em dias
    diferenca = data_atual - data_fornecida

    # Retornar a quantidade de dias
    return diferenca.days


def situacao_func(sit):
    print(f"Situação Funcional: {sit}")
    situacoes = (('1', 'ATIVIDADE MEIO'),
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
    select_sit = [tg_sit[0] for tg_sit in situacoes if tg_sit[1] == str(sit)]
    print(f"Situação Selecionada: {select_sit}")
    dado_tratado = int(select_sit[0])
    print(f"Tipo de dado: {type(dado_tratado)}")
    return dado_tratado


def cob_princ_lot(unidade):
    rel_cobs = (('1', '10BBM'), ('5', '11 BBM-SF24'), ('5', '11BBM'), ('2', '12BBM'), ('1', '1BBM'), ('6', '1CIA IND'), ('1', '1COB'), ('1', '2BBM'), ('3', '2CIA IND'), ('2', '2COB'), ('1', '3BBM'), ('3', '3COB'), ('3', '4BBM'), ('4', '4COB'), ('2', '5BBM'), ('1', '5CIA IND'), ('5', '5COB'), ('5', '6BBM'), ('4', '6CIA IND'), ('6', '6COB'), ('4', '7BBM'), ('6', '7C IND'), ('6', '7CIA IND'), ('2', '8BBM'), ('6', '9BBM'), ('0', 'AAS'), ('0', 'ABM'), ('0', 'AJGERAL'), ('0', 'BEMAD'), ('0', 'BOA'), ('0', 'CAT'), ('0', 'CCBM'), ('0', 'CEB'), ('0', 'CG'), ('0', 'CHEFE DO ESTADO-MAIOR'), ('0', 'COBOM CIAD'), ('0', 'COMANDO-GERAL'), ('0', 'CSM'), ('0', 'DAI'), ('0', 'DAT'), ('0', 'DAT1'), ('0', 'DAT2'), ('0', 'DAT3'), ('0', 'DLF'), ('0', 'DRH'), ('0', 'DRH GABINETE'), ('0', 'DRH1'), ('0', 'DRH2'), ('0', 'DRH4'), ('0', 'DRH5'),
                ('0', 'EMBM'), ('0', 'EXCLUIDOS DO CBMMG'), ('0', 'NÃO ENCONTRADO'), ('1', 'SF 24 1BBM'), ('1', 'SF 24 2BBM'), ('3', 'SF 24 2CIA IND'), ('1', 'SF 24 3BBM'), ('3', 'SF 24 4BBM'), ('2', 'SF 24 5BBM'), ('6', 'SF 24 7 CIA IND'), ('4', 'SF 24 7BBM'), ('2', 'SF 24 8BBM'), ('0', 'SF 24 AJ.GERAL'), ('6', 'VETERANOS DA 1CIA IND'), ('3', 'VETERANOS DA 2CIA IND'), ('1', 'VETERANOS DA 5CIA IND'), ('4', 'VETERANOS DA 6CIA IND'), ('6', 'VETERANOS DA 7CIA IND'), ('1', 'VETERANOS DA RMBH'), ('1', 'VETERANOS DO 10BBM'), ('5', 'VETERANOS DO 11BBM'), ('2', 'VETERANOS DO 12BBM'), ('1', 'VETERANOS DO 1BBM'), ('1', 'VETERANOS DO 2BBM'), ('1', 'VETERANOS DO 3BBM'), ('3', 'VETERANOS DO 4BBM'), ('2', 'VETERANOS DO 5BBM'), ('5', 'VETERANOS DO 6BBM'), ('4', 'VETERANOS DO 7BBM'), ('5', 'VETERANOS DO 8BBM'), ('6', 'VETERANOS DO 9BBM'),)
    # Encontra a unidade principal
    unit_lot = extrair_primeiro_elemento(unidade)

    # Encontra o cob
    unit_cob = [cob[0] for cob in rel_cobs if cob[1] == unit_lot]
    unit_cob = unit_cob[0] if len(unit_cob) > 0 else '0'

    return [unit_cob, unit_lot, unidade]


# Função que retorna os dados para preechimentos do model EPI
def generate_ciurb_epi(dados):
    # CONJUNTO DE COMBATE A INCENDIO ********************************************
    possui_conj_ciurb = False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    marca_conj = dados[0] if possui_conj_ciurb else ''
    modelo_conj = dados[0] if possui_conj_ciurb else ''
    ano_fab_conj = dados[1] if possui_conj_ciurb else ''
    estadodeconservacao_conj = dados[2] if possui_conj_ciurb else ''

    # SEPARAÇÃO DE JAQUETA E CALÇA
    kit_jaqueta = separar_lista(dados[3])
    kit_calca = separar_lista(dados[4])

    # AJUSTES DE KITS
    jaquetatamanho = kit_jaqueta[0] if kit_jaqueta[0] != '' else ''
    jaquetacomplemento = kit_jaqueta[1] if kit_jaqueta[1] != '' else ''
    calcatamanho = kit_calca[0] if kit_calca[0] != '' else ''
    calcacomplemento = kit_calca[1] if kit_calca[1] != '' else ''

    # CAPACETES DE COMBATE A INCENDIO ********************************************
    possui_cap_ciurb = False if dados[5] == 'NÃO POSSUI' or dados[5] == '' else True
    marca_cap = dados[5] if possui_cap_ciurb else ''
    modelo_cap = dados[5] if possui_cap_ciurb else ''
    cor_cap = dados[6] if possui_cap_ciurb else ''
    ano_fab_cap = dados[7] if possui_cap_ciurb else ''
    estadodeconservacao_cap = dados[8] if possui_cap_ciurb else ''

    # LUVAS DE COMBATE A INCENDIO ********************************************
    possui_luv_ciurb = False if dados[9] == 'NÃO POSSUI' or dados[9] == '' else True
    marca_luv = dados[9] if possui_luv_ciurb else ''
    modelo_luv = dados[9] if possui_luv_ciurb else ''
    ano_fab_luv = dados[10] if possui_luv_ciurb else ''
    estadodeconservacao_luv = dados[11] if possui_luv_ciurb else ''
    medida_luv = extrair_medida(dados[12])
    circunferenciamao = medida_luv if medida_luv else ''

    # BALACLAVAS DE COMBATE A INCENDIO ********************************************
    tipo_camada = proper_case_last_word(dados[13])
    possui_bal_ciurb = False if dados[13] == 'NÃO POSSUI' or dados[13] == '' else True
    # marca_bal_ciurb = tipo_camada if tipo_camada else ''
    marca_bal_ciurb = ''
    # modelo_bal_ciurb = tipo_camada if tipo_camada else ''
    modelo_bal_ciurb = ''
    camadas_bal_ciurb = tipo_camada if tipo_camada else ''
    ano_fab_bal_ciurb = dados[14] if dados[14] else ''
    estadodeconservacao_bal_ciurb = dados[15] if dados[15] else ''

    # BOTA DE COMBATE A INCENDIO ********************************************
    possui_bot_ciurb = False if dados[16] == 'NÃO POSSUI' or dados[16] == '' else True
    marca_bot_ciurb = dados[16] if possui_bot_ciurb else ''
    modelo_bot_ciurb = dados[16] if possui_bot_ciurb else ''
    ano_fab_bot_ciurb = dados[17] if dados[17] else ''
    estadodeconservacao_bot_ciurb = dados[18] if dados[18] else ''
    numero_bot_cirurb = dados[19] if dados[19] else ''

    return {
        'possui_conj_ciurb': possui_conj_ciurb,
        'marca_conj': marca_conj,
        'modelo_conj': modelo_conj,
        'ano_fab_conj': ano_fab_conj,
        'estadodeconservacao_conj': estadodeconservacao_conj,
        'jaquetatamanho': jaquetatamanho,
        'jaquetacomplemento': jaquetacomplemento,
        'calcatamanho': calcatamanho,
        'calcacomplemento': calcacomplemento,
        'possui_cap_ciurb': possui_cap_ciurb,
        'marca_cap': marca_cap,
        'modelo_cap': modelo_cap,
        'cor_cap': cor_cap,
        'ano_fab_cap': ano_fab_cap,
        'estadodeconservacao_cap': estadodeconservacao_cap,
        'possui_luv_ciurb': possui_luv_ciurb,
        'marca_luv': marca_luv,
        'modelo_luv': modelo_luv,
        'ano_fab_luv': ano_fab_luv,
        'estadodeconservacao_luv': estadodeconservacao_luv,
        'circunferenciamao': circunferenciamao,
        'possui_bal_ciurb': possui_bal_ciurb,
        'marca_bal_ciurb': marca_bal_ciurb,
        'modelo_bal_ciurb': modelo_bal_ciurb,
        'camadas_bal_ciurb': camadas_bal_ciurb,
        'ano_fab_bal_ciurb': ano_fab_bal_ciurb,
        'estadodeconservacao_bal_ciurb': estadodeconservacao_bal_ciurb,
        'possui_bot_ciurb': possui_bot_ciurb,
        'marca_bot_ciurb': marca_bot_ciurb,
        'modelo_bot_ciurb': modelo_bot_ciurb,
        'ano_fab_bot_ciurb': ano_fab_bot_ciurb,
        'estadodeconservacao_bot_ciurb': estadodeconservacao_bot_ciurb,
        'numero_bot_cirurb': numero_bot_cirurb
    }


def generate_multimiss_epi(dados):

    # CONJUNTO DE MULTIMISSÃO ********************************************
    possui_conj_mult = False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    marca_conj = dados[0] if possui_conj_mult else ''
    modelo_conj = dados[0] if possui_conj_mult else ''
    ano_fab_conj = dados[1] if possui_conj_mult else ''
    estadodeconservacao_conj = dados[2] if possui_conj_mult else ''

    # CAPACETE DE MULTIMISSÃO ********************************************
    # possui_cap_mult = False if dados[3] == 'NÃO POSSUI' or dados[3] == '' else True
    possui_cap_mult = False
    # marca_cap = dados[3] if possui_cap_mult else ''
    marca_cap = ''
    # modelo_cap = dados[3] if possui_cap_mult else ''
    modelo_cap = ''
    # cor_cap = dados[4] if possui_cap_mult else ''
    cor_cap = ''
    # ano_fab_cap = dados[5] if possui_cap_mult else ''
    ano_fab_cap = ''
    # estadodeconservacao_cap = dados[6] if possui_cap_mult else ''
    estadodeconservacao_cap = ''

    # LUVA DE MULTIMISSÃO ********************************************
    # possui_luv_mult = False if dados[7] == 'NÃO POSSUI' or dados[7] == '' else True
    possui_luv_mult = False
    # marca_luv = dados[7] if possui_luv_mult else ''
    marca_luv = ''
    # modelo_luv = dados[8] if possui_luv_mult else ''
    modelo_luv = ''
    # ano_fab_luv = dados[9] if possui_luv_mult else ''
    ano_fab_luv = ''
    # estadodeconservacao_luv = dados[10] if possui_luv_mult else ''
    estadodeconservacao_luv = ''
    # circunferenciamao_luv = dados[9] if possui_luv_mult else ''
    medida_luv = extrair_medida(dados[3])
    circunferenciamao_luv = medida_luv if medida_luv else ''

    # BOTA DE MULTIMISSÃO ********************************************
    possui_bot_mult = False if dados[4] == 'NÃO POSSUI' or dados[4] == '' else True
    marca_bot = dados[4] if possui_bot_mult else ''
    modelo_bot = dados[4] if possui_bot_mult else ''
    ano_fab_bot = dados[5] if possui_bot_mult else ''
    estadodeconservacao_bot = dados[6] if possui_bot_mult else ''
    tamanho_bot = dados[7] if possui_bot_mult else ''

    return {
        # conjunto de multimissao
        'possui_conj_mult': possui_conj_mult,
        'marca_conj': marca_conj,
        'modelo_conj': modelo_conj,
        'ano_fab_conj': ano_fab_conj,
        'estadodeconservacao_conj': estadodeconservacao_conj,
        # capacete de multimissao
        'possui_cap_mult': possui_cap_mult,
        'marca_cap': marca_cap,
        'modelo_cap': modelo_cap,
        'cor_cap': cor_cap,
        'ano_fab_cap': ano_fab_cap,
        'estadodeconservacao_cap': estadodeconservacao_cap,
        # luva de multimissao
        'possui_luv_mult': possui_luv_mult,
        'marca_luv': marca_luv,
        'modelo_luv': modelo_luv,
        'ano_fab_luv': ano_fab_luv,
        'estadodeconservacao_luv': estadodeconservacao_luv,
        'circunferenciamao_luv': circunferenciamao_luv,
        # bota de multimissao
        'possui_bot_mult': possui_bot_mult,
        'marca_bot': marca_bot,
        'modelo_bot': modelo_bot,
        'ano_fab_bot': ano_fab_bot,
        'estadodeconservacao_bot': estadodeconservacao_bot,
        'tamanho_bot': tamanho_bot
    }


def generate_salvamento_epi(dados):

    # CAPACETE SALVAMENTO AQUATICO
    # possui_cap_aqu = False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    possui_cap_aqu = False
    # marca_cap_aqu = dados[0] if possui_cap_aqu else ''
    marca_cap_aqu = ''
    # modelo_cap_aqu = dados[0] if possui_cap_aqu else ''
    modelo_cap_aqu = ''
    # cor_cap_aqu = dados[1] if possui_cap_aqu else ''
    cor_cap_aqu = ''
    # ano_fab_cap_aqu = dados[2] if possui_cap_aqu else ''
    ano_fab_cap_aqu = ''
    # estadodeconservacao_cap_aqu = dados[3] if possui_cap_aqu else ''
    estadodeconservacao_cap_aqu = ''

    # CAPACETE SALVAMENTO ALTURA
    possui_cap_alt = False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    marca_cap_alt = dados[0] if possui_cap_alt else ''
    modelo_cap_alt = dados[0] if possui_cap_alt else ''
    cor_cap_alt = dados[1] if possui_cap_alt else ''
    ano_fab_cap_alt = dados[2] if possui_cap_alt else ''
    estadodeconservacao_cap_alt = dados[3] if possui_cap_alt else ''

    # LUVA SALVAMENTO VEICULAR
    possui_luv_veic = False if dados[4] == 'NÃO POSSUI' or dados[4] == '' else True
    marca_luv_veic = dados[4] if possui_luv_veic else ''
    modelo_luv_veic = dados[4] if possui_luv_veic else ''
    ano_fab_luv_veic = dados[5] if possui_luv_veic else ''
    estadodeconservacao_luv_veic = dados[6] if possui_luv_veic else ''
    medida_luv_veic = extrair_medida(dados[7])
    circunferenciamao_luv_veic = medida_luv_veic if possui_luv_veic else ''

    return {
        # capacete aquatico
        'possui_cap_aqu': possui_cap_aqu,
        'marca_cap_aqu': marca_cap_aqu,
        'modelo_cap_aqu': modelo_cap_aqu,
        'cor_cap_aqu': cor_cap_aqu,
        'ano_fab_cap_aqu': ano_fab_cap_aqu,
        'estadodeconservacao_cap_aqu': estadodeconservacao_cap_aqu,
        # capacete altura
        'possui_cap_alt': possui_cap_alt,
        'marca_cap_alt': marca_cap_alt,
        'modelo_cap_alt': modelo_cap_alt,
        'cor_cap_alt': cor_cap_alt,
        'ano_fab_cap_alt': ano_fab_cap_alt,
        'estadodeconservacao_cap_alt': estadodeconservacao_cap_alt,
        # luva veicular
        'possui_luv_veic': possui_luv_veic,
        'marca_luv_veic': marca_luv_veic,
        'modelo_luv_veic': modelo_luv_veic,
        'ano_fab_luv_veic': ano_fab_luv_veic,
        'estadodeconservacao_luv_veic': estadodeconservacao_luv_veic,
        'circunferenciamao_luv_veic': circunferenciamao_luv_veic
    }


def converter_funtion(dados):
    lista = [('sd2cl', 'SOLDADO DE 2 CLASSE'),
             ('sd', 'SOLDADO DE 1 CLASSE'),
             ('cb', 'CABO'),
             ('3sgt', '3 SARGENTO'),
             ('2sgt', '2 SARGENTO'),
             ('1sgt', '1 SARGENTO'),
             ('subten', 'SUBTENENTE'),
             ('2ten', '2 TENENTE'),
             ('1ten', '1 TENENTE'),
             ('cap', 'CAPITAO'),
             ('maj', 'MAJOR'),
             ('tencel', 'TENENTE CORONEL'),
             ('cel', 'CORONEL'),]

    for i in lista:
        if i[1] == dados:
            return i[0]


def generate_motorresgate_epi(dados):

    # CONJUNTO DE MOTORRESGATE
    # possui_conj_motoresg =  False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    possui_conj_motoresg = False
    # marca_conj_motoresg = dados[0] if possui_conj_motoresg else ''
    marca_conj_motoresg = ''
    # modelo_conj_motoresg = dados[0] if possui_conj_motoresg else ''
    modelo_conj_motoresg = ''
    # ano_fab_conj_motoresg = dados[0] if possui_conj_motoresg else ''
    ano_fab_conj_motoresg = ''
    # estadodeconservacao_conj_motoresg = dados[0] if possui_conj_motoresg else ''
    estadodeconservacao_conj_motoresg = ''

    # CAPACETE DE MOTORRESGATE
    # possui_cap_motoresg =  False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    possui_cap_motoresg = False
    # marca_cap_motoresg = dados[0] if possui_cap_motoresg else ''
    marca_cap_motoresg = ''
    # modelo_cap_motoresg = dados[0] if possui_cap_motoresg else ''
    modelo_cap_motoresg = ''
    # ano_fab_cap_motoresg = dados[0] if possui_cap_motoresg else ''
    ano_fab_cap_motoresg = ''
    # cor_cap_motoresg = dados[0] if possui_cap_motoresg else ''
    cor_cap_motoresg = 'branco'
    # estadodeconservacao_cap_motoresg = dados[0] if possui_cap_motoresg else ''
    estadodeconservacao_cap_motoresg = ''

    # LUVA DE MOTORRESGATE
    # possui_luv_motoresg =  False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    possui_luv_motoresg = False
    # marca_luv_motoresg = dados[0] if possui_luv_motoresg else ''
    marca_luv_motoresg = ''
    # modelo_luv_motoresg = dados[0] if possui_luv_motoresg else ''
    modelo_luv_motoresg = ''
    # ano_fab_luv_motoresg = dados[0] if possui_luv_motoresg else ''
    ano_fab_luv_motoresg = ''
    # estadodeconservacao_luv_motoresg = dados[0] if possui_luv_motoresg else ''
    estadodeconservacao_luv_motoresg = ''
    # circunferenciamao_luv_motoresg = dados[0] if possui_luv_motoresg else ''
    medida_luv = extrair_medida(dados[0])
    circunferenciamao_luv_motoresg = medida_luv if medida_luv else ''

    # BOTA DE MOTORRESGATE
    # possui_bot_motoresg =  False if dados[0] == 'NÃO POSSUI' or dados[0] == '' else True
    possui_bot_motoresg = False
    # marca_bot_motoresg = dados[0] if possui_bot_motoresg else ''
    marca_bot_motoresg = ''
    # modelo_bot_motoresg = dados[0] if possui_bot_motoresg else ''
    modelo_bot_motoresg = ''
    # ano_fab_bot_motoresg = dados[0] if possui_bot_motoresg else ''
    ano_fab_bot_motoresg = ''
    # estadodeconservacao_bot_motoresg = dados[0] if possui_bot_motoresg else ''
    estadodeconservacao_bot_motoresg = ''
    # Tamanho da Bota
    tamanho_bot_motoresg = dados[1] if dados[1] else ''

    return {
        # conjunto motorresgate
        'possui_conj_motoresg': possui_conj_motoresg,
        'marca_conj_motoresg': marca_conj_motoresg,
        'modelo_conj_motoresg': modelo_conj_motoresg,
        'ano_fab_conj_motoresg': ano_fab_conj_motoresg,
        'estadodeconservacao_conj_motoresg': estadodeconservacao_conj_motoresg,
        # capacete motorresgate
        'possui_cap_motoresg': possui_cap_motoresg,
        'marca_cap_motoresg': marca_cap_motoresg,
        'modelo_cap_motoresg': modelo_cap_motoresg,
        'ano_fab_cap_motoresg': ano_fab_cap_motoresg,
        'estadodeconservacao_cap_motoresg': estadodeconservacao_cap_motoresg,
        'cor_cap_motoresg': cor_cap_motoresg,
        # luva motorresgate
        'possui_luv_motoresg': possui_luv_motoresg,
        'marca_luv_motoresg': marca_luv_motoresg,
        'modelo_luv_motoresg': modelo_luv_motoresg,
        'ano_fab_luv_motoresg': ano_fab_luv_motoresg,
        'circunferenciamao_luv_motoresg': circunferenciamao_luv_motoresg,
        'estadodeconservacao_luv_motoresg': estadodeconservacao_luv_motoresg,
        # bota motorresgate
        'possui_bot_motoresg': possui_bot_motoresg,
        'marca_bot_motoresg': marca_bot_motoresg,
        'modelo_bot_motoresg': modelo_bot_motoresg,
        'ano_fab_bot_motoresg': ano_fab_bot_motoresg,
        'estadodeconservacao_bot_motoresg': estadodeconservacao_bot_motoresg,
        'tamanho_bot_motoresg': tamanho_bot_motoresg

    }


if __name__ == '__main__':
    # print(separar_nomes("FILIPE HENRIQUE DE OLIVEIRA"))
    print(converter_funtion("2 SARGENTO"))
