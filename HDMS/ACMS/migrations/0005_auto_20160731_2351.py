# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACMS', '0004_hmo_list_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmo_list',
            name='address',
            field=models.TextField(default='no address'),
        ),
        migrations.AddField(
            model_name='hmo_list',
            name='hmo_status',
            field=models.BooleanField(default='0', help_text='Check it if HMO is active', verbose_name='Hmo Status'),
        ),
    ]