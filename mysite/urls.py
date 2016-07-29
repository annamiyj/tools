# -*- coding: utf-8 -*- 
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
#     url(r'^getcode/test/(\d{11})/$', learn_views.getcode_test, name='getcode_test'),
#     url(r'^getcode/online/(\d{11})/$', learn_views.getcode_online, name='getcode_online'),

    url(r'^getverifycode/$', learn_views.getverifycode, name='getverifycode'),
    url(r'^index/$', learn_views.index, name='index'),
    url(r'^getcode/$', learn_views.getcode, name='getcode')
]