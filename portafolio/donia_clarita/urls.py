from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login, name='login'),
    path('administracion/', views.administracion, name='administracion'),
    path('habitacion/', views.habitacion, name='habitacion'),
    path('adminnew/', views.adminnew, name='adminnew'),
]