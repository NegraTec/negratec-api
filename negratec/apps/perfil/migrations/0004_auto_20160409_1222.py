# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_auto_20160327_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagem',
            field=models.ImageField(default='negratec/media', null=True, upload_to='negratec/media'),
        ),
    ]
