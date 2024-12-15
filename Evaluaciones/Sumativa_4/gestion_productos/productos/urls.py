# productos/urls.py
from django.urls import path
from . import views
 
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.lista_productos, name='lista_productos'),
    path('registro/', views.registrar_producto, name='registrar_producto'),
    path('resultado/', views.resultado_producto, name='resultado_producto'),
    path('consulta/', views.consulta, name='consulta_productos'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'), 
    path('actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
]