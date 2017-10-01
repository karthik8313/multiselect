# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='multi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('En', 'English'), ('Tm', 'Tamil'), ('Kn', 'Kannada'), ('Tl', 'Telugu')], max_length=30)),
            ],
        ),
    ]