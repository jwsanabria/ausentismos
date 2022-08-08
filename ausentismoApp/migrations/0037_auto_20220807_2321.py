# Generated by Django 3.2.14 on 2022-08-08 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0036_ausentismo_sede'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factoripc',
            options={'verbose_name': 'Factor IPC', 'verbose_name_plural': 'Factores IPC'},
        ),
        migrations.AlterModelOptions(
            name='factortiemposacompanamiento',
            options={'verbose_name': 'Factor tiempo acompañamiento', 'verbose_name_plural': 'Factores acompañamiento'},
        ),
        migrations.AlterModelOptions(
            name='motivoausentismo',
            options={'verbose_name': 'motivo ausentismo', 'verbose_name_plural': 'motivos ausentismo'},
        ),
        migrations.AlterModelOptions(
            name='nivdanomoral',
            options={'verbose_name': 'Niveles de daño moral', 'verbose_name_plural': 'Niveles de daño moral'},
        ),
        migrations.AlterModelOptions(
            name='parametrosapp',
            options={'verbose_name': 'Parámetro de la aplicación', 'verbose_name_plural': 'Parámetros de la aplicación'},
        ),
        migrations.AlterModelOptions(
            name='tipoacompanamiento',
            options={'verbose_name': 'Tipo acompañamiento', 'verbose_name_plural': 'Tipos de acompañamiento'},
        ),
        migrations.AddField(
            model_name='capacitadoraccidente',
            name='costo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='reemplazoaccidente',
            name='costo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
