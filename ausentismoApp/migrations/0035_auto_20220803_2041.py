# Generated by Django 3.2.14 on 2022-08-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0034_alter_ausentismo_tiempo_ausentismo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ausentismo',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='cargo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ausentismo',
            name='seccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
