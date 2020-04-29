from django.contrib import admin
from django.urls import path, include
from donia_clarita import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('donia_clarita.urls')),
    path('inicio/', views.inicio, name='index.html'),
    path('login/', views.login, name='login.html'),
    path('administracion/', views.administracion, name='administracion.html'),
    path('habitacion/', views.habitacion, name='habitacion.html'),
    path('adminnew/', views.adminnew, name='adminnew.html'),
]
