# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-04 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20191204_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcounties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Coordinate')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.county')),
            ],
        ),
    ]
