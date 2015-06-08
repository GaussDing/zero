# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('avatar', models.ImageField(default=b'', height_field=100, width_field=100, upload_to=b'')),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(default=b'', max_length=64)),
                ('tagline', models.CharField(default=b'', max_length=64)),
                ('sex', models.BooleanField(default=False)),
                ('work', models.CharField(default=b'', max_length=32)),
                ('skill', models.CharField(default=b'', max_length=127)),
                ('education', models.CharField(default=b'', max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
