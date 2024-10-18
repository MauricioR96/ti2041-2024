# productos/urls.py
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('registro/', views.registrar_producto, name='registrar_producto'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
    path('consulta/', views.consulta, name='consulta_productos'),
]