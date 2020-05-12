from django.urls import path
from . import views

urlpatterns = [
    path('', views.web, name='inicio.html'),
    path('login/', views.logins, name='login.html'),
]