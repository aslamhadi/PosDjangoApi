from django.conf.urls import patterns, url
from pos_app.api.views import UserListCreate

urlpatterns = patterns('',  # nopep8
    # User
    url(r'^users/$', UserListCreate.as_view(), name='user'),
)
