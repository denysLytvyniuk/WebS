from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import WebS.apps.main.urls
import WebS.apps.authentication.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(WebS.apps.main.urls.urlpatterns)),
    path('', include(WebS.apps.authentication.urls.urlpatterns)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
