from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto_capture_app/', include('auto_capture_app.urls')),
    path('auto_capture_app/', include('django.contrib.auth.urls')),
]