# Generated by Django 4.0.5 on 2022-06-20 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0003_alter_persona_celuar_contacto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='celuar_contacto',
            field=models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
