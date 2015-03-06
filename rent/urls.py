from django.conf.urls import patterns, url

from rent import views

urlpatterns = patterns('',
	url(r'^$', views.year, name='ask'),
	url(r'year/$', views.year, name='ask')
)