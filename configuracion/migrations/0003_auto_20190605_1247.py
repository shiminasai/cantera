# Generated by Django 2.1.7 on 2019-06-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20190531_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='texto_1',
            field=models.CharField(max_length=60, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='texto_2',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='texto_3',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Texto'),
        ),
    ]
