# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-22 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_order_language_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordernote',
            name='content',
            field=models.CharField(max_length=250, verbose_name='content'),
        ),
    ]
