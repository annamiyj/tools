"""zx_tools URL Configuration

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
from home import views as home_views
from hotelseq import  views as hotelseq_views
from newuser import  views as newuser_views
from credituser import  views as credituser_views
from creditlive import  views as creditlive_views
from toBin import views as toBin_views
# from seqTools import views as seqTools_views


urlpatterns = {
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_views.note_read, name="myjob"),
    url(r'^home/$', home_views.note_read, name="myjob"),
    # url(r'^myjob/$', home_views.myjob, name="myjob"),
    url(r'^tools/seqtoname/$', hotelseq_views.seqtoname, name="seqtoname"),
    url(r'^tools/nametoseq/$', hotelseq_views.nametoseq, name="nametoseq"),
    url(r'^tools/hotelseq/$', hotelseq_views.hotelseq, name='hotelseq'),
    url(r'^tools/newuser/$', newuser_views.newuser, name='newuser'),
    url(r'^tools/newuser_uid/$', newuser_views.newuser_uid, name='newuser_uid'),
    url(r'^tools/newuser_uidadd/$', newuser_views.newuser_uidadd, name='newuser_uidadd'),
    url(r'^tools/newuser_uiddel/$', newuser_views.newuser_uiddel, name='newuser_uiddel'),
    url(r'^tools/newuser_userid/$', newuser_views.newuser_userid, name='newuser_userid'),
    url(r'^tools/newuser_useridadd/$', newuser_views.newuser_useridadd, name='newuser_useridadd'),
    url(r'^tools/newuser_useriddel/$', newuser_views.newuser_useriddel, name='newuser_useriddel'),
    url(r'^tools/credituser/$', credituser_views.credituser, name='credituser'),
    url(r'^tools/credituser_select/$', credituser_views.credituser_select, name='credituser_select'),
    url(r'^tools/credituser_update/$', credituser_views.credituser_update, name='credituser_update'),
    url(r'^tools/creditlive/$', creditlive_views.creditlive, name='creditlive'),
    url(r'^tools/creditliv/del/$', creditlive_views.creditlive_del, name='creditlive_del'),
    url(r'^tools/identity/$',home_views.identity_search,name='identity'),
    url(r'^tools/toBin/search/$',toBin_views.toBin,name='toBin'),
    url(r'^tools/toBin/', toBin_views.toBin_home, name='toBin_home'),
    url(r'^myjob/$', home_views.note_read, name='note_read'),
    url(r'^tools/note/$', home_views.note_write, name='note_write')
}