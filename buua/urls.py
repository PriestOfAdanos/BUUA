from django.conf.urls import include, url
from django.contrib import admin
# from shop import urls as shop_urls
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as authentication_views
# from shop.views import signup as signup_view


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include(shop_urls)),
    # url(r'^login/$', authentication_views.login, name='login'),
    # url(r'^logout/$', authentication_views.logout, name='logout'),
    # url(r'^signup/$', signup_view, name='signup'),
]# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
