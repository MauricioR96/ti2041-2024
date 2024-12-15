from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from productos.api import ProductoViewSet, TokenView, ProductoListView, ProductoDetailView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
 
# Enrutador para ViewSet
router = DefaultRouter()
router.register(r'api/productos', ProductoViewSet, basename='productos')
 
# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Gestión de Productos API",
        default_version='v1',
        description="API RESTful para gestionar productos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@productos.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productos.urls')),  # Rutas de la aplicación productos
    path('api/token/', TokenView.as_view(), name='token_obtain'),
    path('api/productos/', ProductoListView.as_view(), name='producto_list'),
    path('api/productos/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('', include(router.urls)),
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]