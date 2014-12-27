from django.conf.urls import patterns, include, url
from django.contrib import admin

from pos_app.front_end.views import home_view
from pos_app.account.views import login_view, register_view


urlpatterns = patterns('',  # nopep8

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('pos_app.api.urls', namespace='api')),
    url(r'^$', home_view, name='home'),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
)
