# Generated by Django 2.1.7 on 2019-09-23 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_galeria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Galeria',
            new_name='GaleriaEventos',
        ),
    ]