# Generated by Django 2.1.7 on 2019-08-20 21:18

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20190723_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='foto_galerias_audios',
            field=sorl.thumbnail.fields.ImageField(blank=True, help_text='1350x230', null=True, upload_to='configuracion/'),
        ),
    ]