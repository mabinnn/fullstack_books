# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Books',
        ),
    ]