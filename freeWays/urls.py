from django.contrib import admin
from django.conf import settings
from django.urls import path,include


urlpatterns = [
    path('operation/', include('operation.urls')),  # Incluir las rutas de la aplicación 'operation'
    path('admin/', admin.site.urls),
    path('security/', include('security.urls')),  # Incluir las rutas de la aplicación 'security'
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    