from django.core.management.base import BaseCommand
from usuarios.models import GTO


class Command(BaseCommand):
    help = 'Add predefined GTO names to the database'

    def handle(self, *args, **kwargs):
        gto_names = [
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
            "Salvamento Veicular",
        ]

        for name in gto_names:
            GTO.objects.get_or_create(nome=name)

        self.stdout.write(self.style.SUCCESS(
            'Nomes de GTO adicionados com sucesso!'))
