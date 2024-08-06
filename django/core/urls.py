from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Custom apps
    path('', include('general.urls')),
    path('', include('researchdata.urls')),
    # Django admin
    path('dashboard/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
