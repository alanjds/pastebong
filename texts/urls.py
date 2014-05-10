from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.texts_list),
    url(r'^(?P<text_id>\w+)/$', views.texts_detail, name='detail'),
    url(r'^(?P<text_id>\w+)/_ajax_data/$', views.ajax_data, name='detail'),
)
