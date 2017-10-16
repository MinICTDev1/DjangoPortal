# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Landing', '0006_auto_20171013_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submision',
            name='Commncementdate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of team inception'),
        ),
        migrations.AlterField(
            model_name='submision',
            name='company_regDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Company registration date'),
        ),
        migrations.AlterField(
            model_name='submision',
            name='duration',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Duration within the hub'),
        ),
    ]
