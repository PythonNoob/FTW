from django.conf.urls import patterns, url

from contact import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),       
    url(r'^(?P<grupa_id>\d+)/$', views.kompanii, name='kompanii'),
    url(r'^(?P<grupa_id>\d+)/kompanija/$', views.lica, name='lica')

)