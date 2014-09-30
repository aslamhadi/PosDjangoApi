from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',  # nopep8

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('pos_app.api.urls', namespace='api')),
)
