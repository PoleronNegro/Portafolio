from django.contrib import admin
from django.urls import path, include
from donia_clarita import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('donia_clarita.urls')),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('habitacion/', views.habitacion, name='habitacion'),
    path('adminnew/', views.adminnew, name='adminnew'),
]
