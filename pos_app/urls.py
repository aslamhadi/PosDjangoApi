from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

from pos_app.front_end.views import home_view
from pos_app.account.views import login_view, register_view


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-token-auth-jwt/', obtain_jwt_token),
    url(r'^api/', include('pos_app.api.urls', namespace='api')),
    url(r'^$', home_view, name='home'),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
