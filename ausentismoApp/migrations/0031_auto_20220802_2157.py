# Generated by Django 3.2.14 on 2022-08-03 02:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0030_parametrosapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ausentismo',
            name='hora_final',
        ),
        migrations.RemoveField(
            model_name='ausentismo',
            name='hora_inicial',
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='horas_ausentismo',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='periodo_ausentismo',
            field=models.CharField(blank=True, choices=[('D', 'Día'), ('H', 'Hora')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='salario_ausentismo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='valor_ausentismo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True),
        ),
        migrations.AlterField(
            model_name='ausentismo',
            name='tiempo_ausentismo',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
