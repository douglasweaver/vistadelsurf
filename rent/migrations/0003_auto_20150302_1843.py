# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=40)),
                ('rate', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('startdate', models.DateField(blank=True)),
                ('enddate', models.DateField(blank=True)),
                ('level', models.CharField(max_length=6, default='Street', choices=[('Garden', 'Garden Level'), ('Street', 'Street Level'), ('Top', 'Top Floor')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='enddate',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='remind',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='snippet',
        ),
        migrations.AddField(
            model_name='booking',
            name='level',
            field=models.CharField(max_length=6, default='Street', choices=[('Garden', 'Garden Level'), ('Street', 'Street Level'), ('Top', 'Top Floor')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booking',
            name='startdate',
            field=models.DateField(blank=True, default=datetime.datetime(2015, 3, 2, 18, 43, 51, 708330, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
