from django.conf.urls import patterns, url
from pos_app.api.views import UserListCreate, CategoryListCreate, CategoryDetail, SubCategoryListCreate, SubCategoryDetail, UnitTypeDetail, UnitTypeListCreate, ProductListCreate, ProductDetail, SubCategoryInCategory, GetProductsByName, Logout, CreatePayment, ImportCategoryCsv

urlpatterns = patterns('',  # nopep8
    # Account
    url(r'^logout/$', Logout.as_view(), name='logout'),

    # Category
    url(r'^categories/$', CategoryListCreate.as_view(), name='category'),
    url(r'^categories/import_csv/$', ImportCategoryCsv.as_view(), name='category-import-csv'),
    url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view(), name='category-detail'),

    # Subcategory
    url(r'^subcategories/$', SubCategoryListCreate.as_view(), name='subcategory'),
    url(r'^subcategories/(?P<pk>[0-9]+)/$', SubCategoryDetail.as_view(), name='subcategory-detail'),
    url(r'^subcategories/category/(?P<pk>[0-9]+)/$', SubCategoryInCategory.as_view(), name='subcategory-in-category'),

    # User
    url(r'^users/$', UserListCreate.as_view(), name='user'),

    # Unit Type
    url(r'^unit-types/$', UnitTypeListCreate.as_view(), name='unit-type'),
    url(r'^unit-types/(?P<pk>[0-9]+)/$', UnitTypeDetail.as_view(), name='unit-type-detail'),

    # Payment
    url(r'^payments/create/$', CreatePayment.as_view(), name='create-payment'),

    # Product
    url(r'^products/$', ProductListCreate.as_view(), name='product'),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name='product-detail'),
    url(r'^products/name/(?P<name>.+)/$', GetProductsByName.as_view(), name='product-by-name'),
)
