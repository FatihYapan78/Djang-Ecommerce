# Generated by Django 5.0.1 on 2024-02-08 15:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "Appcommerce",
            "0007_alter_adres_adres_alter_adres_il_alter_adres_ilce_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profil",
            name="adres",
        ),
        migrations.RemoveField(
            model_name="profil",
            name="image",
        ),
    ]
