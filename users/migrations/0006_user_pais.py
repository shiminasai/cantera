# Generated by Django 2.1.7 on 2019-08-21 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0002_auto_20190624_1011'),
        ('users', '0005_auto_20190723_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organizaciones.Pais'),
        ),
    ]
