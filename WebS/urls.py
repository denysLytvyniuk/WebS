from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import WebS.apps.main.urls as main_urls
import WebS.apps.authentication.urls as auth_urls
import WebS.apps.restapi.urls as rest_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),
    path('', include(auth_urls)),
    path('', include(rest_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
