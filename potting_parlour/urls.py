from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", include('core.urls')),
    path("plants/", include('plants.urls')),
    path("basket/", include('basket.urls')),
    path("profile/", include('profiles.urls')),
    path("checkout/", include('checkout.urls')),
    path("tracker/", include('tracker.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
