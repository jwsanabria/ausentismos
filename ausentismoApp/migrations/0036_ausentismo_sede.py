# Generated by Django 3.2.14 on 2022-08-04 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ausentismoApp', '0035_auto_20220803_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='ausentismo',
            name='sede',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]