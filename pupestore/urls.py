from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, reverse_lazy

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('django.contrib.auth.urls')),

    # path('customers/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('customers/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    # path('customers/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('customers/', include('django.contrib.auth.urls')),

    path('customers/', include('customers.urls')),

    path('', include('storemain.urls')),
    path('store/', include('storemain.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('checkout/', include('checkout.urls')),
]
