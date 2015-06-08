#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified : xilin.ding (ddydlp@gmail.com)

from django.conf.urls import url, patterns

from .views import *

urlpatterns = patterns('',
    url(ur'^login$', home.login, name='index')
)