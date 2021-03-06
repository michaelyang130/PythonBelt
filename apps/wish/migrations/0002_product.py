# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('dated_added', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shareditem', models.ManyToManyField(related_name='shareditem', to='wish.User')),
                ('useritem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useritem', to='wish.User')),
            ],
        ),
    ]
