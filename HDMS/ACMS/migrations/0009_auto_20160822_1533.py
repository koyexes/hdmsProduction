# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ACMS', '0008_patient_date_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='hmo_id',
            new_name='hmo',
        ),
    ]