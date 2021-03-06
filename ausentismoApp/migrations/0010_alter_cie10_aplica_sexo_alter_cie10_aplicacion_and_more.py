# Generated by Django 4.0.5 on 2022-07-10 21:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0009_cie10_aplica_sexo_cie10_categoria_cie10_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cie10',
            name='aplica_sexo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='aplicacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='capitulo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='categoria',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='edad_maxima',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='edad_minima',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='estandar_gel',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='estandar_msps',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='extra_v',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='fecha_actualizacion',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='grupo',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='grupo_mortalidad',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='publico_privado',
            field=models.CharField(blank=True, choices=[('Pri', 'Privada'), ('Pub', 'Publica')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='subcategoria',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='subgrupo',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='usuario_responsable',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cie10',
            name='valor_registro',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
