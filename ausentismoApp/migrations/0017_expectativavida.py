# Generated by Django 3.2.14 on 2022-07-17 23:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0016_factoripc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpectativaVida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(150)])),
                ('tipo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('B', 'No binario')], max_length=1)),
                ('expectativa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Expectativa de vida',
                'verbose_name_plural': 'Expectativas de vida',
            },
        ),
    ]
