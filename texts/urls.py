from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.texts_list),
    url(r'^(?P<text_id>\w+)/$', views.texts_detail, name='detail'),
)
