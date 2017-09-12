# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulncode_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vulnerabilityreference',
            unique_together=set([('vulnerability', 'source', 'reference_id', 'url')]),
        ),
    ]