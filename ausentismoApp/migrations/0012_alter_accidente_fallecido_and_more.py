# Generated by Django 4.0.5 on 2022-07-11 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0011_costosaccinsumosmedicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accidente',
            name='fallecido',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='accidente',
            name='incapacidad',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='accidente',
            name='invalidez',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
