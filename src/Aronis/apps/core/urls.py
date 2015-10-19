# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from apps.core.views import home

urlpatterns = patterns(
    '',
    url(r'^', home, name='home'),
)
