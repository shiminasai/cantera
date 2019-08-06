# Generated by Django 2.1.7 on 2019-08-06 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actualidad', '0003_galeria'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualidad',
            name='aprobado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actualidad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
