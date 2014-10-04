from django.conf.urls import patterns, url
from pos_app.api.views import UserListCreate, CategoryListCreate, CategoryDetail

urlpatterns = patterns('',  # nopep8
    # User
    url(r'^users/$', UserListCreate.as_view(), name='user'),
    url(r'^categories/$', CategoryListCreate.as_view(), name='category'),
    url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view(), name='category-detail'),
)
