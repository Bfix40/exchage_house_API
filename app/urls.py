from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('v1/', include('core.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

