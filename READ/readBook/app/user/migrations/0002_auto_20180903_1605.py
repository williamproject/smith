# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userread',
            name='icon',
            field=models.ImageField(default='', upload_to='icon', verbose_name='用户头像'),
        ),
    ]
