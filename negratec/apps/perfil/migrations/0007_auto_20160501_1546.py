# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-01 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_auto_20160501_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='eventos',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='github',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='linkedin',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='lutas',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='outras_redes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='stacks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='twitter',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
