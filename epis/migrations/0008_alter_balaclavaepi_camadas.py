# Generated by Django 5.0.6 on 2024-09-25 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epis', '0007_alter_capaceteaquaticoepi_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balaclavaepi',
            name='camadas',
            field=models.CharField(choices=[('S', 'Simples'), ('D', 'Dupla'), ('T', 'Tripla')], max_length=10),
        ),
    ]
