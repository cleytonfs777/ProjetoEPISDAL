# Generated by Django 5.0.6 on 2024-07-24 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epis', '0001_initial'),
        ('usuarios', '0007_alter_users_sitfunc'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='balaclava',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='epis.balaclava'),
        ),
        migrations.AddField(
            model_name='users',
            name='capacete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='epis.capacete'),
        ),
        migrations.AddField(
            model_name='users',
            name='conjunto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='epis.conjunto'),
        ),
        migrations.AddField(
            model_name='users',
            name='luva',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='epis.luva'),
        ),
    ]
