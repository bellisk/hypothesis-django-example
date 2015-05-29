# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relatednessFactor', models.FloatField()),
                ('baseSubscription', models.ForeignKey(to='example.StockSubscription')),
            ],
        ),
    ]
