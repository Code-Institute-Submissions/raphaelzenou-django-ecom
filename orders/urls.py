from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout

urlpatterns = [
    path('cart/', views.cart, name="cart"),
    path('update_cart/', views.update_cart, name="update_cart"),
    path('list/', views.orders, name="orders"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

