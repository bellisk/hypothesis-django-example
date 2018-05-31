# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='relatedsubscription',
            name='baseSubscription',
        ),
        migrations.RemoveField(
            model_name='summary',
            name='subscriptions',
        ),
        migrations.AddField(
            model_name='stocksubscription',
            name='value',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='RelatedSubscription',
        ),
        migrations.DeleteModel(
            name='Summary',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='subscriptions',
            field=models.ManyToManyField(related_name='portfolios', to='example.StockSubscription'),
        ),
    ]
