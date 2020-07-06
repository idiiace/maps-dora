# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-27 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polygon', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=250)),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Coordinate')),
            ],
        ),
        migrations.CreateModel(
            name='county',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Coordinate')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.City')),
            ],
        ),
        migrations.CreateModel(
            name='subcounties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=100)),
                ('coordinates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Coordinate')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.county')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='coordinates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Coordinate'),
        ),
        migrations.AddField(
            model_name='city',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Country'),
        ),
    ]
