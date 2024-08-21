from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates a superuser if not exists'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="adminsdal").exists():
            User.objects.create_superuser(
                username="adminsdal",
                email="adminsdal@example.com",
                password="mudarasenha193"
            )
            self.stdout.write(self.style.SUCCESS(
                'Superuser "adminsdal" created'))
        else:
            self.stdout.write(self.style.WARNING(
                'Superuser "adminsdal" already exists'))
