from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from pos_app.front_end import views

class SimpleStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import authenticate, login
        if request.user.is_anonymous():
            # Auto-login the User for Demonstration Purposes
            user = authenticate()
            login(request, user)
        return super(SimpleStaticView, self).get(request, *args, **kwargs)


urlpatterns = patterns('',  # nopep8

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('pos_app.api.urls', namespace='api')),
    url(r'^$', views.home_view, name='home'),
    # url(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(), name='example'),
    # url(r'^$', TemplateView.as_view(template_name='base.html')),
)

# urlpatterns += patterns('django.contrib.staticfiles.views',  # nopep8
#     url(r'', 'serve', {'path': '/base.html'}),
# )
