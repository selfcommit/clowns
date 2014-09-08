from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'hello.views.home'),
    url(r'^stackbot/$', 'hello.views.stackbot'),
    url(r'^slash_stackbot/$', 'hello.views.slash_stackbot'),
)
