from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('process/', views.checkout_process, name="checkout_process"),
    path('success/', views.checkout_success, name="checkout_success"),
    path('failure/', views.checkout_failure, name="checkout_failure"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

