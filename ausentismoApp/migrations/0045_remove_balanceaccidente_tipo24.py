# Generated by Django 3.2.14 on 2023-03-21 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ausentismoApp", "0044_balanceaccidente"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="balanceaccidente",
            name="tipo24",
        ),
    ]
