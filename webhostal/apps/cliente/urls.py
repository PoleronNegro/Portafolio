from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.homecli, name='index_cli.html'),

    path('detallecontrato/',  views.detallecontrato, name='detalle_contrato.html'),
    

]