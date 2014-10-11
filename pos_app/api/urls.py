from django.conf.urls import patterns, url
from pos_app.api.views import UserListCreate, CategoryListCreate, CategoryDetail, SubCategoryListCreate, \
    SubCategoryDetail, UnitTypeDetail, UnitTypeListCreate, ProductListCreate, ProductDetail

urlpatterns = patterns('',  # nopep8
    # Category
    url(r'^categories/$', CategoryListCreate.as_view(), name='category'),
    url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view(), name='category-detail'),

    # Subcategory
    url(r'^subcategories/$', SubCategoryListCreate.as_view(), name='subcategory'),
    url(r'^subcategories/(?P<pk>[0-9]+)/$', SubCategoryDetail.as_view(), name='subcategory-detail'),

    # User
    url(r'^users/$', UserListCreate.as_view(), name='user'),

    # Unit Type
    url(r'^unit-types/$', UnitTypeListCreate.as_view(), name='unit-type'),
    url(r'^unit-types/(?P<pk>[0-9]+)/$', UnitTypeDetail.as_view(), name='unit-type-detail'),

    # Product
    url(r'^products/$', ProductListCreate.as_view(), name='product'),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name='product-detail'),
)
