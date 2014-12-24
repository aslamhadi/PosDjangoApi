from django.conf.urls import patterns, include, url
from django.contrib import admin
from pos_app.front_end import views


urlpatterns = patterns('',  # nopep8

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('pos_app.api.urls', namespace='api')),
    url(r'^$', views.home_view, name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register_view, name='register'),
)
