# Generated by Django 4.2.11 on 2024-03-26 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastroUsuario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastro", name="data_nascimento", field=models.DateField(),
        ),
    ]