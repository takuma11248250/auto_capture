from django.urls import path
from . import views

app_name = 'auto_capture_app'

urlpatterns = [
	path('', views.index, name='index'),
    path('getcapture/', views.get_capture_query, name='get_capture_query'),
]