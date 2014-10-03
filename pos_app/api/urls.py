from django.conf.urls import patterns, url
from pos_app.api.views import UserListCreate, CategoryListCreate

urlpatterns = patterns('',  # nopep8
    # User
    url(r'^users/$', UserListCreate.as_view(), name='user'),
    url(r'^categories/$', CategoryListCreate.as_view(), name='category'),
)
