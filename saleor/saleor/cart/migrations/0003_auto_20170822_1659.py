# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-22 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170206_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('open', 'Open - currently active'), ('payment', 'Waiting for payment'), ('saved', 'Saved - for items to be purchased later'), ('ordered', 'Submitted - an order was placed'), ('checkout', 'Checkout - processed in checkout'), ('canceled', 'Canceled - canceled by user')], default='open', max_length=32, verbose_name='order status'),
        ),
    ]
