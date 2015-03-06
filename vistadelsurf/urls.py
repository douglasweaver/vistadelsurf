from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^rent/', include('rent.urls',namespace="rent")),
    url(r'^admin/', include(admin.site.urls)),
)