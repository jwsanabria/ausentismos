# Generated by Django 3.2.14 on 2022-07-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0026_auto_20220723_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='accidente',
            name='ipc_final',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='accidente',
            name='ipc_inicial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='accidente',
            name='num_mes_lcc',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
