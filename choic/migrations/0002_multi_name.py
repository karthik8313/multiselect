# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multi',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
