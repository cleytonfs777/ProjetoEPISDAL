# Generated by Django 5.0.6 on 2024-09-25 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epis', '0006_alter_balaclavaepi_plannumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capaceteaquaticoepi',
            name='cor',
            field=models.CharField(choices=[('B', 'Branco'), ('A', 'Amarelo'), ('V', 'Vermelho')], max_length=20),
        ),
    ]
