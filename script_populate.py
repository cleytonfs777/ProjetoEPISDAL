import os
import django
from usuarios.models import Users
from epis.models import ConjuntoEPI, CapaceteEPI, LuvaEPI, BalaclavaEPI, BotaEPI, CapaceteAquaticoEPI, CapaceteVeicularEPI, LuvaVeicularEPI
from datetime import date

# Configurar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


def criar_usuario_ficticio():
    # Criar o usuário fictício
    usuario = Users.objects.create(
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
        emailfunc='usuario@exemplo.com',
        priorit='A'
    )

    # Criar EPIs CIURB
    ciurb_conjunto = ConjuntoEPI.objects.create(
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

    ciurb_capacete = CapaceteEPI.objects.create(
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

    print("Usuário fictício e EPIs criados com sucesso!")


if __name__ == '__main__':
    criar_usuario_ficticio()
