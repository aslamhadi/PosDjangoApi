from django.conf.urls import url

from pos_app.api.views import UserListCreate, CategoryListCreate, CategoryDetail, SubCategoryListCreate, \
    SubCategoryDetail, UnitTypeDetail, UnitTypeListCreate, ProductCreate, ProductList, ProductDetail, \
    SubCategoryInCategory, GetProductsByName, Logout, CreatePayment, ImportCategoryCsv, FactoryDetail, \
    FactoryListCreate, EmbalaseListCreate, EmbalaseDetail, GetEmbalaseByName, DoctorList, DoctorDetail, \
    DoctorCreateUpdate, PaymentList, PaymentDetail, CreatePrescription, PaymentProductDetail, GetPaymentProductsById

urlpatterns = [
    # Account
    url(r'^logout/$', Logout.as_view(), name='logout'),

    # Category
    url(r'^categories/$', CategoryListCreate.as_view(), name='category'),
    url(r'^categories/import_csv/$', ImportCategoryCsv.as_view(), name='category-import-csv'),
    url(r'^categories/(?P<pk>[^/]+)/$', CategoryDetail.as_view(), name='category-detail'),

    # Doctor
    url(r'^doctors/$', DoctorList.as_view(), name='doctor'),
    url(r'^doctors/create/$', DoctorCreateUpdate.as_view(), name='doctor-create'),
    url(r'^doctors/(?P<pk>[^/]+)/$', DoctorDetail.as_view(), name='doctor-detail'),

    # Embalase
    url(r'^embalases/$', EmbalaseListCreate.as_view(), name='embalase'),
    url(r'^embalases/name/(?P<name>.+)/$', GetEmbalaseByName.as_view(), name='product-by-name'),
    url(r'^embalases/(?P<pk>[^/]+)/$', EmbalaseDetail.as_view(), name='embalase-detail'),

    # Factory
    url(r'^factories/$', FactoryListCreate.as_view(), name='factory'),
    url(r'^factories/(?P<pk>[^/]+)/$', FactoryDetail.as_view(), name='factory-detail'),

    # Subcategory
    url(r'^subcategories/$', SubCategoryListCreate.as_view(), name='subcategory'),
    url(r'^subcategories/category/(?P<pk>[^/]+)/$', SubCategoryInCategory.as_view(), name='subcategory-in-category'),
    url(r'^subcategories/(?P<pk>[^/]+)/$', SubCategoryDetail.as_view(), name='subcategory-detail'),

    # User
    url(r'^users/$', UserListCreate.as_view(), name='user'),

    # Unit Type
    url(r'^unit-types/$', UnitTypeListCreate.as_view(), name='unit-type'),
    url(r'^unit-types/(?P<pk>[^/]+)/$', UnitTypeDetail.as_view(), name='unit-type-detail'),

    # Payment
    url(r'^payments/create/$', CreatePayment.as_view(), name='create-payment'),
    url(r'^payments/$', PaymentList.as_view(), name='payment'),
    url(r'^payments/(?P<pk>[^/]+)/$', PaymentDetail.as_view(), name='payment-detail'),

    # Payment Product
    url(r'^payment-products/(?P<pk>[^/]+)/$', PaymentProductDetail.as_view(), name='payment-product-detail'),
    url(r'^payment-products/payment/(?P<payment>[^/]+)/$', GetPaymentProductsById.as_view(), name='payment-product-by-payment-id'),

    # Prescription
    url(r'^prescriptions/create/$', CreatePrescription.as_view(), name='create-prescription'),

    # Product
    url(r'^products/$', ProductList.as_view(), name='product'),
    url(r'^products/create/$', ProductCreate.as_view(), name='product-create'),
    url(r'^products/name/(?P<name>.+)/$', GetProductsByName.as_view(), name='product-by-name'),
    url(r'^products/(?P<pk>[^/]+)/$', ProductDetail.as_view(), name='product-detail'),
]
