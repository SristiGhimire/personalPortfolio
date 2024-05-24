from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('dashboard/', include('app2.urls')),
    path('login/', include('useraccount.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
