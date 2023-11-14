from django.contrib import admin
from django.urls import path, include

# Para el manejo de archivos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('TicketOn.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Rutas de autenticación de Django
    path('accounts/', include('allauth.urls')),   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
