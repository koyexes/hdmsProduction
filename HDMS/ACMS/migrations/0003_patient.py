# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 00:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
         migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ACMS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('othername', models.CharField(default='NIL', max_length=20, null=True)),
                ('card_no', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('phone_number', models.CharField(default='NIL', max_length=15)),
                ('address', models.CharField(default='NIL', max_length=50)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('origin', models.CharField(default='NIL', max_length=10)),
                ('added_by', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hmo_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ACMS.hmo_list', verbose_name='hmo_id')),
            ],
        ),
    ]
