# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsm_utility', '0008_gsmusers_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordtoken',
            name='mail_sent',
            field=models.BooleanField(default=False),
        ),
    ]
