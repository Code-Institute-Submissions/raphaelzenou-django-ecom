from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
]

# https://docs.djangoproject.com/en/1.11/ref/views/#serving-files-in-development
# https://docs.djangoproject.com/en/3.1/howto/static-files/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

