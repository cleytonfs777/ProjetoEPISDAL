# Generated by Django 5.0.6 on 2024-07-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_gto_users_cob_users_date_include_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_include',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
