from django.contrib import admin
from django.urls import path, include
from donia_clarita import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('donia_clarita.urls')),
]
