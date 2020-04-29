from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', views.login, name='login'),
    path('habitacion/',  views.habitacion, name='habitacion.html'),
]