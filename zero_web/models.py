#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified : xilin.ding (ddydlp@gmail.com)

from django.db import models


class User(models.Model):
    """
    用户信息
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    avatar = models.ImageField(width_field=100, height_field=100, default='')
    password = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=64, default='')
    tagline = models.CharField(max_length=64, default='')
    sex = models.BooleanField(default=False)
    work = models.CharField(max_length=32, default='')
    skill = models.CharField(max_length=127, default='')
    education = models.CharField(max_length=32, default='')
    pass