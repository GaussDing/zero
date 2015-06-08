#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified : xilin.ding (ddydlp@gmail.com)

"""
照片首页
"""
from django.shortcuts import render_to_response

from zero_web.models import User

__author__ = 'linpeng'
__revision__ = '0.1'


def login(request):
    """
    登陆界面
    :param request:
    :return:
    """
    return render_to_response('web/login.html', {'list': 'hello, world!'})
    pass


def user_info(request):
    pass