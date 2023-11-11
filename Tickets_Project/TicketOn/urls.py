from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('eventos/<nombre_evento>/<evento_slug>',views.detalles_evento,name="detalles_evento")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)