from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^web/', include('zero_web.urls'), name='web'),
                       url(r'^admin/', include(admin.site.urls)))
