from django.core.management.base import BaseCommand
# Importe o modelo do usuário conforme sua aplicação
from usuarios.models import Users


class Command(BaseCommand):
    help = 'Apaga todos os usuários, exceto os que possuem cargo de Administrador'

    def handle(self, *args, **kwargs):
        # Filtra os usuários que não são Administradores
        usuarios_para_deletar = Users.objects.exclude(cargo='A')

        # Exibe a quantidade de usuários que serão deletados
        total_para_deletar = usuarios_para_deletar.count()
        self.stdout.write(f'{total_para_deletar} usuários serão deletados.')

        # Deleta os usuários
        usuarios_para_deletar.delete()

        # Mensagem final
        self.stdout.write(self.style.SUCCESS(
            f'{total_para_deletar} usuários foram deletados com sucesso.'))
