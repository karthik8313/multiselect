# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 12:16
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('choic', '0002_multi_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='multi',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('a', 'apple'), ('m', 'mango'), ('o', 'orrange')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]