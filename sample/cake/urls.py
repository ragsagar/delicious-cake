from django.conf.urls import patterns, include, url

from .resources import (
    CakeListResource, CakeDetailResource, CakeListResourceExtra,)


urlpatterns = patterns('',
    url(r'^cake/(?P<pk>\d+)/$', CakeDetailResource.as_view(),
        name='cake-detail'),
    url(r'^cake/$', CakeListResource.as_view(), name='cake-list'),
    url(r'^cake/extra/$', CakeListResourceExtra.as_view(),
        name='cake-list-extra'),)