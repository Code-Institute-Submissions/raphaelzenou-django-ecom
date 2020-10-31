from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('signup/', views.signup, name="signup"),
    path('editprofile/', views.editprofile, name="editprofile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

