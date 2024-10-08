# Generated by Django 5.0.6 on 2024-09-18 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epis', '0004_balaclavaepi_user_botaepi_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balaclavaepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='balaclavaepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='balaclavaepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='balaclavaepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='botaepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='botaepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='botaepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='botaepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteaquaticoepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteaquaticoepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteaquaticoepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteaquaticoepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteveicularepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteveicularepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteveicularepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capaceteveicularepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='conjuntoepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conjuntoepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conjuntoepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conjuntoepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='luvaepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='luvaepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='luvaepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='luvaepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='luvaveicularepi',
            name='anofabricacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='luvaveicularepi',
            name='datapreenchimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='luvaveicularepi',
            name='plannumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='luvaveicularepi',
            name='recebido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
