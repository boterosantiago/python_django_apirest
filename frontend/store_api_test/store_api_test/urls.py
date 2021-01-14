from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store_api_test.views import home, products, register, register_product, privacy_policy, product_detail
from django.conf.urls import handler404

handler404 = handler404 = 'store_api_test.views.not_found_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('products/', products),
    path('register/', register),
    path('register_product/', register_product),
    path('privacy_policy/', privacy_policy),
    path('product_detail/<int:code>', product_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)