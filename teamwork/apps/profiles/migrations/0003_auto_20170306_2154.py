# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
