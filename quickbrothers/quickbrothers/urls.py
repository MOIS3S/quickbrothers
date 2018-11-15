from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core.urls import core_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # core of path
    path('', include(core_patterns)),
]

# Error 404 y 500 personalizados
handler404 = 'core.views.handler404'
handler500 = 'core.views.handler500'

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
