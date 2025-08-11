from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import sys

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('park.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# для просмотра SQL-запросов при помощи django-debug-toolbar
# if settings.DEBUG and 'test' not in sys.argv:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns

